def leerEntero(x):
    numero= input(x)
    entero= False
    while not entero:
        try:
            numero= int(numero)
            entero= True
        except:
            numero: input(x)
    return numero
        
    
a= leerEntero("Introduce un entero")
print(a) 
b= leerEntero("Introduce un entero")
print(b) 
