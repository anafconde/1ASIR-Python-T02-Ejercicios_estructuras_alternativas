# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-11

#Ejercicio 11. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.


A = float(input("Introduce el primer lado del triángulo: "))
B = float(input("Introduce el segundo lado del triángulo: "))
C = float(input("Introduce el tercer lado del triángulo: "))

if A == B and B == C:
    print("El triángulo es equilátero.")
elif A**2 == B**2 + C**2 or B**2 == A**2 + C**2 or C**2 == A**2 + B**2:
    print("El triángulo es rectángulo.")
elif A==B or A==C or B==C:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
