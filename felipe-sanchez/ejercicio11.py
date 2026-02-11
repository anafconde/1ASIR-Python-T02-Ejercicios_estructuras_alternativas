# Autor: Felipe
# Version: 1.0
import math
# Ejercicio 11
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.


lado1=int(input("Dame un tamaño: "))
lado2=int(input("Dame otro tamaño: "))
lado3=int(input("Dame el ultimo tamaño: "))


if lado1 == lado2 == lado3:
    print("Es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es isosceles")
elif ((lado1**2)+(lado2**2))==(lado3**2):
    print("Es rectangulo")
else:
    print("Es escaleno")