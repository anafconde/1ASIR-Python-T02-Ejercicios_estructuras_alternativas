#Autor: Alberto Jiménez
#Version: 1.0
#Escribe un programa que lea un número e indique si es par o impar.

print ("""-----------------------PAR O IMPAR-----------------------""")

num1 = int(input("Escribe un número: "))

if num1%2 == 0:
    print ("El número",num1, "es par.")
else:
    print ("El número",num1, "es impar.")