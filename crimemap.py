from flask import Flask
from flask import render_template
from flask import request
import json
import datetime
#import dateparser
import string
# Workaround for local development (with db mock).
import dbconfig
if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()
categories = ['mugging', 'break-in']


@app.route("/")
def home(error_message=None):
    crimes = DB.get_all_crimes()
    # Serializing our crimes dict to JSON string.
    crimes = json.dumps(crimes)
    return render_template("home.html", crimes=crimes, categories=categories, error_message=error_message)


@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("userinput")
        DB.add_input(data)
    except Exception as e:
        print(e)
    return home()


@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return home()


@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    if category not in categories:
        return home()
    date = request.form.get("date")
    '''
    date = format_date(request.form.get("date"))
    if not date:
        return home("Invalid date. Please use yyyy-mm-dd format")
        '''
    try:
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
    except ValueError:
        return home()
    description = sanitize_string(request.form.get("description"))
    # -- Debug output
    print("category = " + category)
    print("date = " + date)
    print("latitude = " + latitude)
    print("longitude = " + longitude)
    print("description = " + description)
    # We need to implement add_crime method for DBHelper class instance.
    DB.add_crime(category, date, latitude, longitude, description)
    return home()

'''
def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date, "%Y-%m-%d")
    except TypeError:
        return None
'''

def sanitize_string(user_input):
    white_list = string.letters + string.digits + " !?$.,;:-'()&"
    return filter(lambda x: x in white_list, user_input)


if __name__ == '__main__':
    app.run(port=5000, debug=True)