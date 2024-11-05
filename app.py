<<<<<<< HEAD
import time
import var, requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
historial = []
=======
import var
>>>>>>> cb5e07ed6759a586210fbe1ce7f022c94c7b904f

menu()
def menu():
    op = ""
<<<<<<< HEAD
    while op != "s":
        print(" * * * Menú Principal * * *")
        print("-----------------------------------")
        print("a. Elegir ciudad\nb. Cambiar de unidad\nc. Ver historial\nd. Clima de los próximos 5 días\nS. Salir de la aplicación")
        op = input("Elija su opción: ").lower()
        
        if op == "a":
            get_weather()
        elif op == "b":
            var.Unidades()
            var.Medida()
        elif op == "c":
            mostrar_historial()
        elif op == "d":
            get_weather_forecast()
        elif op == "s":
            despedida = "Saliendo . . ."
            for caracter in despedida:
                print(caracter, end=" ")
                time.sleep(0.5)
        else:
            print("Dato inválido, vuelva a intentar")

            print("Dato inválido, vuelva a intentar")

def get_weather():
    var.ciudad()
    medida = var.medida
    units = var.units
    ciudad = var.city
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        clima = response.json()
        lat, lon = clima['coord']['lat'], clima['coord']['lon']
        resultado = f"""Ubicación: {clima.get("name")}
        Temperatura: {clima['main']['temp']}{medida}
        Sensación Térmica: {clima['main']['feels_like']} {medida}
        Temperatura Mínima: {clima['main']['temp_min']} {medida}
        Temperatura Máxima: {clima['main']['temp_max']} {medida}
        Presión: {clima['main']['pressure']} hPa
        Humedad: {clima['main']['humidity']}%
        Viento: Velocidad: {clima['wind']['speed']} m/s Dirección: {clima['wind']['deg']}°
        Tiempo: {clima['weather'][0]['description']}
        Visibilidad: {clima['visibility']} metros"""
        
        print(resultado)
        historial.append(resultado)
        return lat, lon  # Devuelve las coordenadas para el historial
    elif response.status_code == 404:
        print("La ciudad ingresada no existe, por favor ingrese una ciudad válida")
        get_weather()
=======
while op != "s":
    print(" * * * Menú Principal * * *")
    print("-----------------------------------")
    print("a. Elegir ciudad\nb. Cambiar de unidad\nc. Ver historial\nd. Clima de los próximos 5 días\nS. Salir de la aplicación")
    op = input("Elija su opción: ").lower()
        
    if op == "a":
        var.get_weather()
    elif op == "b":
        var.Unidades()
    elif op == "c":
        var.mostrar_historial()
    elif op == "d":
        var.get_weather_forecast()
    elif op == "s":
        despedida = "Saliendo . . ."
        for caracter in despedida:
            print(caracter, end=" ")
>>>>>>> cb5e07ed6759a586210fbe1ce7f022c94c7b904f
    else:
        print("Dato inválido, vuelva a intentar")








<<<<<<< HEAD
def get_weather_forecast():
    var.ciudad()
    medida = var.medida
    units = var.units
    ciudad = var.city
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        clima = response.json()
        print(f"Pronóstico para los próximos 5 días en {clima.get('city').get('name')}:\n")

        # Recorremos el pronóstico en intervalos de 3 horas
        for entry in clima['list']:
            fecha = entry['dt_txt']
            temp = entry['main']['temp']
            temp_min = entry['main']['temp_min']
            temp_max = entry['main']['temp_max']
            feels_like = entry['main']['feels_like']
            pressure = entry['main']['pressure']
            humidity = entry['main']['humidity']
            weather_desc = entry['weather'][0]['description']
            wind_speed = entry['wind']['speed']
            wind_deg = entry['wind']['deg']
            visibility = entry.get('visibility', 'No disponible')

            # Formato de salida para cada intervalo de 3 horas
            resultado = f"""
            Fecha y hora: {fecha}
            Temperatura: {temp}{medida} (Sensación Térmica: {feels_like}{medida})
            Temperatura Mínima: {temp_min}{medida} - Máxima: {temp_max}{medida}
            Presión: {pressure} hPa
            Humedad: {humidity}%
            Viento: Velocidad {wind_speed} m/s, Dirección: {wind_deg}°
            Visibilidad: {visibility} metros
            Tiempo: {weather_desc}
            """
            print(resultado)
            
        historial.append(f"Pronóstico de 5 días para {ciudad}")
    elif response.status_code == 404:
        print("La ciudad ingresada no existe, por favor ingrese una ciudad válida")
        get_weather_forecast()
    else:
        print(f"Error: {response.status_code}")


def mostrar_historial():
    if not historial:
        print("No hay consultas en el Historial")
    else:
        print("Historial de consultas del clima")
        for consulta in historial:
            print(consulta)
            print("----------------------------")

menu()

=======

>>>>>>> cb5e07ed6759a586210fbe1ce7f022c94c7b904f
