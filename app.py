import time
import var,requests
from dotenv import load_dotenv
import os 


# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

historial = []

def menu():
    op=""
   
    while(op != "s"):
        print("     * * * Menú Principal * * *")
        print("-----------------------------------")
        print("a.Elegir ciudad\nb.Cambiar de unidad\nc. Ver historial\nS.Salir de la aplicacion")
        op=input("Elija su opcion: ")
        op=op.lower()
        if op == "a":
            get_weather()
        elif op == "b":
            var.Unidades()
            var.Medida()
        elif op == "c":
            mostrar_historial()
        elif op == "s":
            despedida = "Saliendo . . ."
            for caracter in despedida:
                print(caracter, end=" ")
                time.sleep(0.5)
        else:
            print("Dato inválido, vuelva a intentar")


def get_weather():
    var.ciudad()
    medida=var.medida
    units=var.units
    ciudad=var.city
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        clima = response.json()
        print(f"""        Ubicación:  {clima.get("name")}
        Temperatura: {clima['main']['temp']}{medida}
        Sensación Térmica: {clima['main']['feels_like']} {medida}
        Temperatura Mínima: {clima['main']['temp_min']} {medida}
        Temperatura Máxima": {clima['main']['temp_max']} {medida}
        Presión: {clima['main']['pressure']} hPa
        Humedad: {clima['main']['humidity']}%
        Viento: Velocidad: {clima['wind']['speed']} m/s
                Dirección: {clima['wind']['deg']}°
        Tiempo: {clima['weather'][0]['description']}
        Visibilidad: {clima['visibility']} metros"""
        print(resultado)
        historial.append(resultado)
    elif response.status_code == 404:
        print("La ciudad ingresada no existe , por favor ingrese una ciudad valida")
        get_weather()
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