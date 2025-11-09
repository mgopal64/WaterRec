from flask import Flask, render_template
import requests
from flask import jsonify
from dotenv import load_dotenv
import os
from utils import receive_data as rd
from utils import fao_penman as fp
from utils import threshold as th

load_dotenv()
api_key = os.getenv("api")

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
    return render_template("data.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route('/')
def get_weather():
    try:
        # returns data from weather api
        data = rd.recieve_data(api_key)

        # FAO Penman-Monteith calculation
        response = fp.fao_penman_debug(data)

        # Returns boolean based off of threshold
        return th.should_water(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()