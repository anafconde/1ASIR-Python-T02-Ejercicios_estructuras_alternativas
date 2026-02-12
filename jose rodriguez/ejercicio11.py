# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 11
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

datoa = int(input("Introduce el primer dato: "))
datob = int(input("Introduce el segundo dato: "))
datoc = int(input("Introduce el tercer dato: "))

if datoa == datob and datob == datoc:
    print("Es un triangulo equilatero")

elif datoa == datob or datoa == datoc or datob == datoc:
    print("Es un triangulo isosceles")

else:
    if datoa*datoa + datob*datob == datoc*datoc or datoa*datoa + datoc*datoc == datob*datob or datob*datob + datoc*datoc == datoa*datoa:
        print("Es un triangulo rectangulo")
    else:
        print("Es un triangulo escaleno")