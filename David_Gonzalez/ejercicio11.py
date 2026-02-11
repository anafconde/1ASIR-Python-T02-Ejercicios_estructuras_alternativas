# Autor: David González Mora
# versión: 1.0
# Ejercicio 11 Relación de ejercicios
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

a = float(input("Introduce un número: "))
b = float(input("Introduce un número: "))
c = float(input("Introduce un número: "))

if a**2 + b**2 == c**2:
    print("Es un triángulo rectángulo")

elif a == b == c:
    print("Es un triángulo equilátero")

elif a == b or a == c or b == c:
    print("Es un triángulo isósceles")

else:
    print("Es un triángulo escaleno")
