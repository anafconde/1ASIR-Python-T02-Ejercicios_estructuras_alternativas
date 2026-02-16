#autor: juan manuel senes 
#version 1.0 
#Escribir un programa que lea un año e indique si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

print ("dame un año y te dire si es bisiesto o no")

año= int(input("introduce un año"))

if (año %4==0 and año % 100 !=0 )or (año%400==0):
    print ("es bisiesto")
else:
    print("no es bisiesto")
