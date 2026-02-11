# Autor: Paco Fernandez
# Version: 1.0
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))

if num2 <= 0:
    print("No se puede dividir entre cero")
else:
    resultado = num1//num2
    print("El resultado de la division es ", resultado)
