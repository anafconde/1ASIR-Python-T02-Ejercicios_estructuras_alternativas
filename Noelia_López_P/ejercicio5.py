# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-11

# Ejercicio 5. Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
usuario=input("Introduce el nombre de usuario: ")
contraseña=input("Introduce la contraseña: ")
if usuario=="pepe" and contraseña=="asdasd":
    print("Has entrado al sistema.")
else:
    print("Error. Usuario o contraseña incorrectos.")

