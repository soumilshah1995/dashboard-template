from flask import (Blueprint,render_template,redirect,url_for)
home_blueprint = Blueprint('Home', __name__, template_folder='templates/Home')
from mywebsite.GoogleOAuth.views import isLoggedIN


@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    flag , name, picture = isLoggedIN()
    return render_template('Home.html', flag=flag, name=name, picture=picture)


@home_blueprint.route('/route1', methods=['GET', 'POST'])
def getData():
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
