from flask import Flask, render_template, send_from_directory, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/pages/data.html')
def data():
    return send_from_directory('static/pages', 'data.html')

# backend calls weather API 
@app.route('/api/weather')
def get_weather():
    try:
        # Ambient Weather API endpoint
        url = "https://rt.ambientweather.net/v1/devices"
        
        params = {
            'apiKey': 'eba6cc95d6b849a59125f46c1a49581fa027a00c4643440185efdec6edbddd97',
            'applicationKey': 'dfdd92b6b41d40debae8600d60428f77bf5a39871ba54381883417df45d6d9ed'
        }
        
        response = requests.get(url, params=params)
        
        # Return the JSON response
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": f"API returned status {response.status_code}"}), response.status_code
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5500)