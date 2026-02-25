#autor: juan manuel senes 
#version 1.0 
#Algoritmo que pida un número y diga si es positivo, negativo o 0.

print ("dame un numero y te digo si es positivo o negativo")

numero=int(input())

if (numero%2==0):
    print("el numero es par")
elif (numero%2!=0):
    print("el numero es impar")