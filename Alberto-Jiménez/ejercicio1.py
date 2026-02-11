#Autor: Alberto Jiménez
#Version: 1.0
#Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

print ("""-----------------------MAYOR O MENOR-----------------------""")

num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe un número: "))

if num1 > num2:
    print ("El",num1,"es mayor que",num2)
else:
    print ("El",num2,"es menor que",num1)