#Autor: Alberto Jiménez
#Version: 1.0
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
# El programa debe determinar qué tipo de triángulo es, teniendo en cuenta lo siguiente:
#- Si se cumple Pitágoras entonces es triángulo rectángulo.
#- Si sólo dos lados del triángulo son iguales entonces es isósceles.
#- Si los 3 lados son iguales entonces es equilátero.
#- Si no se cumple ninguna de las condiciones anteriores, es escaleno.

import math

print("""-------------------------VAMOS A AVERIGUAR EL TIPO DE TRIÁNGULO----------------------------""")

num1 = int(input("Dime un lado de un triángulo: "))
num2 = int(input("Dime otro lado del triángulo: "))
num3 = int(input("Dime el último lado del triángulo: "))


if num1 == num2 == num3:
    print("El triángulo en cuestión es un triángulo equilátero")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print("El triángulo en cuestión es un triángulo isósceles")
else:
    print("El triángulo en cuestión es un triángulo escaleno")


