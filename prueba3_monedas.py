def leerEntero(mensaje):
    numero= input(mensaje)
    entero= False
    while not entero:
        try:
            numero= int(numero)
            entero= True
        except:
            numero= input(mensaje)
    return numero

def leerReal(mensaje):
    numero= input(mensaje)
    entero= False
    while not entero:
        try:
            numero= float(numero)
            entero= True
        except:
            numero= input(mensaje)
    return numero

def menu():
    opcion= -1
    while (opcion  <1 or opcion  >7):
        print ("1.Cambio de euros a dólares")
        print("2.Cambio de dólares a euros")
        print("3.Cambio de euros a libras")
        print("4.Cambio de libras a euros.")
        print("5.Cambio de libras a dólares")
        print("6.Cambio de dólares a libras")
        print("7.Salir")
        opcion = leerEntero("Introduce una opcion")
    return opcion

opcion= menu()
while (opcion != 7):
