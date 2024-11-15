import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

units= "metric"
medida="°C"
opcion=""
city=""
cont=0
historial = []
def clear_scrn():
    os.system('cls')
def Unidades():
    global opcion,units,medida
    print("-----------------------\n Seleccione las unidades de medida:")
    print("1.Celcius\n2.Fahrenheit\n0.Volver al menú principal")
    while(opcion != "S"):
        opcion=input("Elija su opcion: ")
        if opcion=="1":
            units= "metric"
            medida="°C"
            break
        elif opcion == "2":
            units="imperial"
            medida="°F"
            break
        elif opcion == "0":
            print("Volviendo...")
            break

        else:
            print("Dato invalido , vuelva a intentar")
    clear_scrn()
    
def ciudad ():
    global city,cont
    while(True):
        
        city=input("Ingrese el nombre de la ciudad: ")
        if city == "":
         print("No puede dejar este campo vacio ...")
        elif all(caracter.isdigit() for caracter in city ):
         print("No puede ingresar números ")
        else:
            cont+=1
            break
def get_weather():
    global city,units,medida,opcion,cont
    global historial
    if (cont>0):
        print(f"Ciudad elegida : "+ city)
        opcion=input("Desea cambiar de ciudad ? S/N :...")
        if (opcion.lower == "s"):
            ciudad()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}&lang=es"
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
    else:
        print(f"Error: {response.status_code}")

def get_weather_forecast():
 
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
