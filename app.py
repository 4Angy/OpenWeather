import inquirer
from rich.console import Console
from rich.table import Table
from rich.text import Text
import requests
from dotenv import load_dotenv
import os
import var  # Asegúrate de que var.py esté en el mismo directorio

# Cargar variables de entorno desde el archivo .env
load_dotenv()
API_KEY = os.getenv('API_KEY')
historial = []
console = Console()

def menu():
    while True:
        console.clear()
        console.print(" * * * Menú Principal * * *", style="bold")
        
        opciones = [
            "Elegir ciudad",
            "Cambiar de unidad",
            "Ver historial",
            "Clima de los próximos 5 días",
            "Salir"
        ]
        
        preguntas = [
            inquirer.List('opcion',
                          message="Seleccione una opción:",
                          choices=opciones,
                          ),
        ]
        
        respuesta = inquirer.prompt(preguntas)
        
        if respuesta['opcion'] == "Elegir ciudad":
            get_weather()
        elif respuesta['opcion'] == "Cambiar de unidad":
            cambiar_unidad()
        elif respuesta['opcion'] == "Ver historial":
            mostrar_historial()
        elif respuesta['opcion'] == "Clima de los próximos 5 días":
            get_weather_forecast()
        elif respuesta['opcion'] == "Salir":
            console.print("Saliendo . . .", style="bold")
            break

def cambiar_unidad():
    unidades = ["Métrico (°C)", "Imperial (°F)"]
    preguntas = [
        inquirer.List('unidad',
                      message="Seleccione la unidad de medida:",
                      choices=unidades,
                      carousel=True  # Permite la navegación con las flechas del teclado
                      ),
    ]
    
    respuesta = inquirer.prompt(preguntas)
    
    if respuesta['unidad'] == "Métrico (°C)":
        var.units = "metric"
        var.medida = "°C"
    elif respuesta['unidad'] == "Imperial (°F)":
        var.units = "imperial"
        var.medida = "°F"
    
    console.print(f"Unidad de medida cambiada a {var.medida}", style="bold green")
    input("Presione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla

def get_weather():
    var.ciudad()
    medida = var.medida
    units = var.units
    ciudad = var.city
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    response = requests.get(url)

    if response.status_code == 200:
        clima = response.json()
        temp = clima['main']['temp']
        
        # Determinar el color basado en la temperatura
        if temp < 0:
            color = "blue"
        elif temp > 30:
            color = "orange"
        else:
            color = "green"

        resultado = Text(f"""Ubicación: {clima.get("name")}
        Temperatura: {temp}{medida}
        Sensación Térmica: {clima['main']['feels_like']} {medida}
        Temperatura Mínima: {clima['main']['temp_min']} {medida}
        Temperatura Máxima: {clima['main']['temp_max']} {medida}
        Presión: {clima['main']['pressure']} hPa
        Humedad: {clima['main']['humidity']}%
        Viento: Velocidad: {clima['wind']['speed']} m/s Dirección: {clima['wind']['deg']}°
        Tiempo: {clima['weather'][0]['description']}
        Visibilidad: {clima['visibility']} metros""", style=color)

        console.print(resultado)
        historial.append(resultado)

        # Esperar a que el usuario presione una tecla antes de limpiar
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
    elif response.status_code == 404:
        console.print("La ciudad ingresada no existe, por favor ingrese una ciudad válida")
        get_weather()
    else:
        console.print(f"Error: {response.status_code}")

def get_weather_forecast():
    var.ciudad()
    medida = var.medida
    units = var.units
    ciudad = var.city
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={API_KEY}&units={units}&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        clima = response.json()
        console.print(f"Pronóstico para los próximos 5 días en {clima.get('city').get('name')}:\n")

        table = Table(title="Pronóstico del Clima")
        table.add_column("Fecha y Hora", justify="center")
        table.add_column("Temperatura", justify="center")
        table.add_column("Descripción", justify="center")

        forecast_resultado = f"Pronóstico de 5 días para {ciudad}:\n"

        for entry in clima['list']:
            fecha = entry['dt_txt']
            temp = entry['main']['temp']
            
            # Determinar el color basado en la temperatura
            if temp < 0:
                color = "blue"
            elif temp > 30:
                color = "orange"
            else:
                color = "green"

            weather_desc = entry['weather'][0]['description']
            table.add_row(fecha, Text(f"{temp}{medida}", style=color), weather_desc)
            
            forecast_resultado += f"Fecha y hora: {fecha}, Temperatura: {temp}{medida}, Tiempo: {weather_desc}\n"

        console.print(table)

        # Agregar el pronóstico al historial
        historial.append(forecast_resultado)

        # Esperar a que el usuario presione una tecla antes de limpiar
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
    elif response.status_code == 404:
        console.print("La ciudad ingresada no existe, por favor ingrese una ciudad válida")
        get_weather_forecast()
    else:
        console.print(f"Error: {response.status_code}")

def mostrar_historial():
    if not historial:
        console.print("No hay consultas en el Historial")
    else:
        console.print("Historial de consultas del clima")
        for consulta in historial:
            console.print(consulta)
            console.print("----------------------------")

    # Esperar a que el usuario presione una tecla antes de limpiar
    input("Presione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla

# Ejecutar el menú
menu()