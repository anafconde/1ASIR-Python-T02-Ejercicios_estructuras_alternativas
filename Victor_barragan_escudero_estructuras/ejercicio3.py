# Autora: Víctor Manuel
# Versión: 1.0
# ejercicio 3:
#Escribe un programa que 
#lea un número e indique si es par o impar.
num1= int(input("dame otro numero "))
pi= num1%2

if pi == 0 :
    print("El",num1, "es par")
else:
    print("El",num1, "es impar")