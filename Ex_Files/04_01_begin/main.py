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
    if not request.args.get("surname"):
        return jsonify(laureates)
    for laureate in laureates:
        if request.args.get("surname").lower().strip() in laureate["surname"].lower():
            return jsonify(laureate)

    return jsonify({"error": "Not found"}), 404
    # return jsonify(laureates)


app.run(debug=True)
