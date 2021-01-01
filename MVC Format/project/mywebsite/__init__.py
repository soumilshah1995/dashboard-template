try:
    print("here")
    import os
    from flask import Flask
    from flask import Flask, request, \
        render_template, redirect, url_for, \
        session, send_file
    from datetime import timedelta

    print("ok")
except Exception as e:
    print("Some Modules are Missing {}".format(e))

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
basedir = os.path.abspath(os.path.dirname(__file__))

from mywebsite.Home.views import home_blueprint
from mywebsite.GoogleOAuth.views import google_blueprint

app.register_blueprint(home_blueprint, url_prefix="/")
app.register_blueprint(google_blueprint, url_prefix="/google")

