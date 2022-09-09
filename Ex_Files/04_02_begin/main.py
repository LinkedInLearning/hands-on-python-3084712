import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate():
    # template found in templates/laureate.html
    # TODO: LinkedIn learners start here.
    results = []
    if not request.args.get("surname"):
        return jsonify(results)

    # TODO: iterate laureates.
    for laureate in laureates:
        if request.args.get("surname").lower().strip() in laureate["surname"].lower():
            results.append(laureate)
    return jsonify(results)


app.run(debug=True)
