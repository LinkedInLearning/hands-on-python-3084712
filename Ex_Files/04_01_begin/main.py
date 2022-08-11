import csv
from flask import Flask, render_template, request, redirect, url_for, jsonify


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
    results = []
    if not request.args.get("surname"):
        return jsonify(results)
    for laureate in laureates:
        if request.args.get("surname").lower().strip() in laureate["surname"].lower():
            results.append(laureate)
    return jsonify(results)

    # return jsonify({"error": "Not found"}), 404
    # return jsonify(laureates)


app.run(debug=True)
