# Autor: Honorio
# Version: 1.0
#Crea un programa que pida al usuario dos números y 
# muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

numero1=int(input("Introduzca el numero1: "))
numero2=int(input("Introduzca el numero2: "))

division=int(numero1/numero2)

if numero2 == 0:
    print ("No se puede dividir con 0")
else:
    print("La division de",numero1,"y de",numero2,"es",division)