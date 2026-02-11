# Autor: David González Mora
# versión: 1.0
# Ejercicio 3 Relación de ejercicios
# Escribe un programa que lea un número e indique si es par o impar.

numero = int(input("Indica un número: "))
par = numero % 2

if par == 0:
    print("Este número", numero, "es par")
else: 
    print("Este número", numero, "es impar")
    
