
units= "metric"
medida="°C"
opcion=""
city=""
def Unidades():
    global opcion,units
    print("-----------------------\n Seleccione las unidades de medida:")
    print("1.Celcius\n2.Fahrenheit\nS.Volver al menú principal")
    while(opcion != "S"):
        opcion=input("Elija su opcion: ")
        if opcion=="1":
            print("Eligio grados Celcius")
            break
        elif opcion == "2":
            units="imperial"
            print("Eligio grados Fahrenheit")
            break
        elif opcion == "S":
            print("Opcion 0")
            break

        else:
            print("Dato invalido , vuelva a intentar")

def Medida():
    global medida
    if opcion == "2":
        medida="°F"
      
def ciudad ():
    global city
    while(True):
        city=input("Ingrese el nombre de la ciudad: ")
        if city == "":
         print("No puede dejar este campo vacio ...")
        elif all(caracter.isdigit() for caracter in city ):
         print("No puede ingresar números ")
        else:
         break
    

