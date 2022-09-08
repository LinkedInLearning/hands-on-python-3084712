import csv
from pprint import pprint
import random
from flask import Flask

import requests  # todo install requests, Flask

app = Flask(__name__)

response = requests.get("https://api.github.com/emojis")
response_values = response.json().values()
emoji_list = list(response_values)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def emoji():
    emoji = random.choice(emoji_list)
    return f'<img src="{emoji}" style="margin: 45vw"/>'


app.run(debug=True)
