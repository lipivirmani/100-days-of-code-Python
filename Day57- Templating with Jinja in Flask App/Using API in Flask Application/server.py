from flask import Flask, render_template
import datetime
import random
import requests

app = Flask(__name__)


@app.route('/')
def home():

    return "Hello ! To know your info add/guess/'your name' to the URL  "

@app.route('/guess/<name>')
def guess(name):
    gender_url= f"https://api.genderize.io?name={name}"
    gender_resp= requests.get(gender_url)
    gender_data= gender_resp.json()
    gender= gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_resp = requests.get(age_url)
    age_data= age_resp.json()
    age = age_data["age"]
    return render_template("guess.html",pers_name=name,gender=gender,age=age)



if __name__ == "__main__":
    app.run(debug=True)
