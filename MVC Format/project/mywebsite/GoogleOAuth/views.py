from flask import (Blueprint,render_template,redirect,url_for,session,Flask)
import json
from datetime import timedelta
import os
from authlib.integrations.flask_client import OAuth

google_blueprint = Blueprint('GoogleOAuth', __name__)

app = Flask(__name__)

# ====================Change me  =======================================
global client_id
global client_secret

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

# ======================================================================


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


@google_blueprint.route('/login')
def login():
    print("HERE 1111111")
    google = oauth.create_client('google')  # create the google oauth client
    print("52 .............")
    redirect_uri = url_for('GoogleOAuth.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@google_blueprint.route('/authorize')
def authorize():
    print('herer')
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    print("toekn")
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    session['profile'] = user_info
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/')


@google_blueprint.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')
