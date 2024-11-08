import requests, curses
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv('API_KEY')

units = "metric"
medida = "°C"
city = ""
historial = []

def Unidades(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    opciones = ["Celsius", "Fahrenheit", "Volver al menú principal"]
    current_row = 0
    global units, medida

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Seleccione las unidades de medida:", curses.A_BOLD)

        for idx, opcion in enumerate(opciones):
            x = 2
            y = idx + 2
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, opcion)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, opcion)

        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(opciones) - 1:
            current_row += 1
        elif key == ord("\n"):
            if current_row == 0:  
                units, medida = "metric", "°C"
                mensaje = "Eligió grados Celsius"
            elif current_row == 1:  
                units, medida = "imperial", "°F"
                mensaje = "Eligió grados Fahrenheit"
            elif current_row == 2:  
                break
            
        # Mensaje de confirmación
            stdscr.clear()
            stdscr.addstr(0, 0, mensaje, curses.A_BOLD)
            stdscr.addstr(2, 0, "Presione una tecla para continuar...")
            stdscr.refresh()
            stdscr.getch()  
            break

def get_weather(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Ingrese el nombre de la ciudad: ")
    curses.echo()
    global city
    city = stdscr.getstr(1, 0).decode("utf-8")
    curses.noecho()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}&lang=es"
    response = requests.get(url)

    if response.status_code == 200:
        clima = response.json()
        resultado = f"""Ubicación: {clima.get("name")}
        Temperatura: {clima['main']['temp']}{medida}
        Sensación Térmica: {clima['main']['feels_like']}{medida}
        Presión: {clima['main']['pressure']} hPa
        Humedad: {clima['main']['humidity']}%
        Tiempo: {clima['weather'][0]['description']}"""
        
        stdscr.addstr(3, 0, resultado)
        historial.append(resultado)
    else:
        stdscr.addstr(3, 0, "La ciudad ingresada no existe o hubo un error con la API.")
    
    stdscr.refresh()
    stdscr.getch()

def mostrar_historial(stdscr):
    stdscr.clear()
    if not historial:
        stdscr.addstr(0, 0, "No hay consultas en el Historial")
    else:
        stdscr.addstr(0, 0, "Historial de consultas del clima")
        for idx, consulta in enumerate(historial):
            stdscr.addstr(idx + 1, 0, consulta)

    stdscr.refresh()
    stdscr.getch()

def get_weather_forecast(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Ingrese el nombre de la ciudad: ")
    curses.echo()
    global city
    city = stdscr.getstr(1, 0).decode("utf-8")
    curses.noecho()

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={units}&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        clima = response.json()
        stdscr.addstr(3, 0, f"Pronóstico para los próximos 5 días en {clima.get('city').get('name')}:\n")

        # Recorremos el pronóstico en intervalos de 3 horas
        for entry in clima['list']:
            fecha = entry['dt_txt']
            temp = entry['main']['temp']
            resultado = f"Fecha y hora: {fecha}, Temperatura: {temp}{medida}\n"
            stdscr.addstr(4, 0, resultado)
            stdscr.refresh()

        historial.append(f"Pronóstico de 5 días para {city}")
    else:
        stdscr.addstr(3, 0, "La ciudad ingresada no existe o hubo un error con la API.")
    
    stdscr.refresh()
    stdscr.getch()
