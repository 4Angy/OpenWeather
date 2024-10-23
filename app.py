
import time
import var,requests
from dotenv import load_dotenv
import os 


# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
def menu():
    op=""
   
    while(op != "s"):
         print("     * * * Menú Principal * * *")
         print("-----------------------------------")
         print("a.Elejir ciudad\nb.Cambiar de unidad\nS.Salir de la aplicacion")
         op=input("Elija su opcion: ")
         op=op.lower()
         if op == "a":
            get_weather()
         elif op == "b":
            var.Unidades()
            var.Medida()
         elif op == "s":
            despedida="Saliendo . . ."
            for caracter in despedida:
                print(caracter,end=" ")
                time.sleep(0.5)
         else:
            print("Dato invalido , vuelva a intentar")

def get_weather():
    var.ciudad()
    medida=var.medida
    units=var.units
    ciudad=var.city
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        clima = response.json()
        print(f"""        Ubicación: , {clima.get("name")}
        Temperatura: {clima['main']['temp'],medida}
        Sensación Térmica: {clima['main']['feels_like'], medida}
        Temperatura Mínima: {clima['main']['temp_min'], medida}
        Temperatura Máxima": {clima['main']['temp_max'], medida}
        Presión: {clima['main']['pressure']} hPa
        Humedad: {clima['main']['humidity']}%
        Viento: Velocidad: {clima['wind']['speed']} m/s
                Dirección: {clima['wind']['deg']}°
        Tiempo: {clima['weather'][0]['description']}
        Visibilidad: {clima['visibility']} metros""")
    elif response.status_code == 404:
        print("La ciudad ingresada no existe , por favor ingrese una ciudad valida")
        get_weather()
    else:
        print(f"Error: {response.status_code}")


menu()