import csv
from flask import Flask, render_template, jsonify


app = Flask(__name__)

with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return "your code here!"


@app.route("/laureates/")
def laureate():
    return "your code here!"


app.run(debug=True)
