# Autor: Iván Plaza
# Versión: 1.0
# Primeros pasos con Python

# Ejercicio 6
# Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.


letra = input("Introduce una letra: ")


if len(letra) == 1 and letra.isalpha():  
    if letra.isupper():
        print(f"'{letra}' es una letra mayúscula.")
    else:
        print(f"'{letra}' no es una letra mayúscula.")
else:
    print("Error: Debes introducir solo una letra.")