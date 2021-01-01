try:
    from flask import Flask, redirect, url_for, session,render_template
    import os
    from datetime import timedelta
    from authlib.integrations.flask_client import OAuth
    import json
    print("All Modules are loaded ...")
except Exception as e:
    print("Modules are Missing : {} ".format(e))


# App config
app = Flask(__name__)

# ====================Change me  =======================================
global client_id
global client_secret

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

# Session config
app.secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
# ======================================================================


# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=client_id,
    client_secret=client_secret,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)

def isLoggedIN():
    try:
        user = dict(session).get('profile', None)
        if user:
            return True, user.get("given_name"), user.get("picture")
        else:
            return False, "" , ""
    except Exception as e:
        return False, "" , ""


@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)



@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/')



@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')



@app.route('/route1')
def route1():

    languages = ["python", "java script" , "c++"]
    score = [10,7,6]




    _ = []
    for key, value in dict(zip(languages, score)).items():
        __ = {
            "name"      : key,
            "y"         : int(value),
            "drilldown" : key
        }
        _.append(__)

    return {
        "res":_
    }

@app.route("/")
def hello():
    flag,name,picture = isLoggedIN()
    return render_template("Home.html", flag=flag, name=name, picture=picture)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)