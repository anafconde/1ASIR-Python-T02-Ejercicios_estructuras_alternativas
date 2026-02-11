# Autor: David González Mora
# versión: 1.0
# Ejercicio 5 Relación de ejercicios
# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

nombre = input("Introduce un usuario: ")
con = input("Introduce una contraseña: ")

if nombre == "pepe" and con == "asdasd":
    print("Bienvenido al sistema")
else:
    print("No has introducido la contraseña correcta")
