# Autora: Víctor Manuel
# Versión: 1.0
# ejercicio 5:
# Escribe un programa que pida un nombre de usuario y 
# una contraseña y si se ha introducido “pepe” y “asdasd” 
# se indica “Has entrado al sistema”, sino se da un error.num1= int(input("dame otro numero "))
usuario= input("Introduce tu usuario: ")
contrasena= input("Introduce tu contraseña: ")

if usuario == "pepe" and contrasena == "asdasd":
    print("Has entrado al sistema")
else :
    print("usuario o contraseña incorrecto")