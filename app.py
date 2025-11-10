from flask import Flask, send_from_directory
from flask import jsonify
from utils import receive_data as rd
from utils import fao_penman as fp
from utils import threshold as th

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['DEBUG'] = True

@app.route("/")
def home():
    return app.send_static_file("index.html")
    # return send_from_directory("static", "index.html")

@app.route("/pages/data.html")
def data():
    return send_from_directory("static", "pages/data.html")

@app.route('/api/weather', methods=['GET'])
def get_weather():
    try:
        # returns data from weather api
        data = rd.receive_data()

        # FAO Penman-Monteith calculation
        response = fp.fao_penman_debug(data)

        # Returns boolean based off of threshold
        should_water = th.should_water(response)
        return jsonify(should_water)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # returns data from weather api
        data = rd.receive_data()
        data["fao_penman"] = fp.fao_penman_debug(data)
        return data

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5050)