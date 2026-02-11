# Autor: Felipe
# Version: 1.0
import math
# Ejercicio 5
# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha 
# introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

usuario=input("Dame el nombre de usuario: ")
contraseña=input("Introduzca la contraseña: ")


if usuario =="pepe" and contraseña == "asdasd" :
    print("Has entrado al sistema")
else:
    print("Credenciales incorrectos")