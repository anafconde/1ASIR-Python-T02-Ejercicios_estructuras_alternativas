"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

    Si se cumple Pitágoras entonces es triángulo rectángulo
    Si sólo dos lados del triángulo son iguales entonces es isósceles.
    Si los 3 lados son iguales entonces es equilátero.
    Si no se cumple ninguna de las condiciones anteriores, es escaleno.

"""
a=int(input("Lado a: "))
b=int(input("Lado b: "))
c=int(input("Lado c: "))

if (a**2+b**2)==c**2:
    print("Triangulo rectangulo")
elif a==b and a==c:
    print("Triangulo equilatero")
elif a==b or a==c or c==b:
    print("Triangulo isosceles")
else:
    print("Triangulo escaleno")

