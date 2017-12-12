from flask import Flask
from flask import render_template
from flask import request
# Workaround for local development (with db mock).
import dbconfig
if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()


@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print(e)
        data = None
    return render_template("home.html", data=data)


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
    date = request.form.get("date")
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    description = request.form.get("description")
    # -- Debug output
    print("category = " + category)
    print("date = " + date)
    print("latitude = " + latitude)
    print("longitude = " + longitude)
    print("description = " + description)
    # We need to implement add_crime method for DBHelper class instance.
    DB.add_crime(category, date, latitude, longitude, description)
    return home()


if __name__ == '__main__':
    app.run(port=5000, debug=True)