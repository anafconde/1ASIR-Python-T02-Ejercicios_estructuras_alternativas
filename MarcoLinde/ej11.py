#Ejercicio 11
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las 
#dimensiones de los lados de un triángulo. El programa debe determinar 
#que tipo de triangulo es, teniendo en cuenta los siguiente:
#Si se cumple Pitágoras entonces es triángulo rectángulo
#Si sólo dos lados del triángulo son iguales entonces es isósceles.
#Si los 3 lados son iguales entonces es equilátero.
#Si no se cumple ninguna de las condiciones anteriores, es escaleno.
A= float(input("Pon un número: "))
B= float(input("Pon otro número: "))
C= float(input("Pon otro número más: "))
if A+B>C and A+C>B and B+C>A:
    if A**2+B**2==C**2 or A**2+C**2==B**2 or B**2+C**2==A**2:
        print("Has hecho un triángulo rectángulo")
    elif A==B==C:
        print("Has hecho un triángulo equilátero")
    elif A==B or A==C or B==C:
        print("Has hecho un triángulo isósceles")
else:
    print("Has hecho un triángulo escaleno")
