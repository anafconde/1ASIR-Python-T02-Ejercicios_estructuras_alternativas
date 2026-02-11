# Autora: Víctor Manuel
# Versión: 1.0
# ejercicio 11:
#Programa que lea 3 datos de entrada A, B y C. 
#Estos corresponden a las dimensiones de los lados de un triángulo. 
#El programa debe determinar que tipo de triangulo es, teniendo en cuenta 
#los siguiente:

# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

print("Dame tres lados y te digo de que triangulo se trata")
a= int(input("dame el lado A "))
b= int(input("dame el lado B "))
c= int(input("dame el lado C "))

if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    print("El triangulo es rectángulo")
elif a == b == c:
    print("El triangulo es equilátero")
elif a == b or a == c or b == c:
    print("El triangulo es isóceles")
else:
    print("El triangulo es escaleno")
