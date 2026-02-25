#autor: juan manuel senes 
#version 1.0 
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
print ("dame dos numeros y te digo su division")
numero1=int(input())
numero2=int(input())
if (numero2/2==0):
    print("la division final es",numero1/numero2)
elif (numero2/2!=0):
    print("no se puede dividir por cero")
