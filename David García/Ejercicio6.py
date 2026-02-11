# Author: David García Pérez
# Version: 1.0

# Ejercicio 6
# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

print("#################### Comprobar letras mayúsculas ######################")

text = input("Introduce una cadena de texto: ")

if text.isupper():
    print("La cadena", text, "está en mayúsculas")
else:
    print("La cadena", text, "no está en mayúsculas")

print("############################################################")