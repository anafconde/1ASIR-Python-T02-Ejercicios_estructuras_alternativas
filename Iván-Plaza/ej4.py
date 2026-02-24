# Autor: Iván Plaza
# Versión: 1.0
# Primeros pasos con Python

# Ejercicio 4
# Crea un programa que pida al usuario
# dos números

#  y muestre su división si el segundo no es cero,
# o un mensaje de aviso en caso contrario.


num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))


if num2 != 0:
    resultado = num1 / num2
    print(f"La división de {num1} entre {num2} es {resultado}")
else:
    print("Error: No se puede dividir entre cero.")