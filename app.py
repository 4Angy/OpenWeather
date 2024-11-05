import var

menu()
def menu():
    op = ""
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
    else:
        print("Dato inválido, vuelva a intentar")









