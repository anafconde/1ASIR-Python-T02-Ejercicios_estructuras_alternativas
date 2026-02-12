#Autor: Alberto Jiménez
#Version: 1.0
"""Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y 
muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido."""

print ("""-----------------------DADO-----------------------""")

num1 = int(input("Dime un número de un dado (1-6): "))

if num1 == 1:
    print ("El opuesto a",num1,"es 6")
elif num1 == 2:
    print ("El número opuesto a", num1, "es 5.")
elif num1 == 3:
    print ("El número opuesto a", num1, "es 4.")
elif num1 == 4:
    print ("El número opuesto a",num1,"es 3.")
elif num1 == 5:
    print ("El número opuesto a", num1,"es 2.")
elif num1 == 6:
    print ("El número opuesto a", num1, "es 1.")
else:
    print ("Error!. Debes introducir un número del 1-6.")