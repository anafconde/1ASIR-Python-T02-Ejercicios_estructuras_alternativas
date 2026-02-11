# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 5
# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” 
# se indica “Has entrado al sistema”, sino se da un error.

usuario = input("Introduce un usuario: ")
contrasena = input("Introduzca una contraseña: ")

if usuario == "pepe" and contrasena == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error no puedes entrar al sistema")