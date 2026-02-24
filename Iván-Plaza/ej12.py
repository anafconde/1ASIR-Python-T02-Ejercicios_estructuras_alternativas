# Autor: Iván Plaza
# Versión: 1.0
# Primeros pasos con Python

# Ejercicio 12
# Programa que lea un año e indique si es bisiesto.
# Regla: divisible por 4, no divisible por 100, salvo divisible por 400.

# Pedimos el año al usuario
año = int(input("Introduce un año: "))

# Comprobamos si es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")