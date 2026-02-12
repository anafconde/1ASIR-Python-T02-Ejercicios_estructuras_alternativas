# Autor: Paco Fernandez
# Version: 1.0
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena = input("Introduce una cadena: ")

if cadena.isalpha() and cadena.isupper():
    print("La cadena está formada solo por letras mayúsculas.")
else:
    print("La cadena no está formada solo por letras mayúsculas.")

