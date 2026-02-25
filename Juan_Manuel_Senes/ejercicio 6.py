#autor: juan manuel senes 
#version 1.0 
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
print("dame una letra para decirte que es mayuscula")
letra = input( )
if (letra.isupper):
    print("la letra",letra,"es mayuscula")
else: print ("la letra",letra,"es minuscula")
