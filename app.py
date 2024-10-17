import requests
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')

@app.route('/weather', methods=['GET'])
def get_weather():
    city_name = request.args.get('city')
    if not city_name:
        return jsonify({"error": "Por favor, proporcione una ciudad"}), 400
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        clima = response.json()
        formatted_response = {
            "Ubicación": clima.get("name"),
            "Temperatura": f"{clima['main']['temp']}°C",
            "Sensación Térmica": f"{clima['main']['feels_like']}°C",
            "Temperatura Mínima": f"{clima['main']['temp_min']}°C",
            "Temperatura Máxima": f"{clima['main']['temp_max']}°C",
            "Presión": f"{clima['main']['pressure']} hPa",
            "Humedad": f"{clima['main']['humidity']}%",
            "Viento": {
                "Velocidad": f"{clima['wind']['speed']} m/s",
                "Dirección": f"{clima['wind']['deg']}°"
            },
            "Tiempo": clima['weather'][0]['description'],
            "Visibilidad": f"{clima['visibility']} metros",
            "Amanecer": clima['sys']['sunrise'],
            "Atardecer": clima['sys']['sunset']
        }
        return jsonify(formatted_response)
    else:
        return jsonify({"error": f"Error: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
