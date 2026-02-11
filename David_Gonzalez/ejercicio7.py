# Autor: David González Mora
# versión: 1.0
# Ejercicio 7 Relación de ejercicios
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = int(input("Introduce la base: "))
expo = int(input("Introduce el exponente: "))
potencia = base ** expo

if potencia > 0:
    print(potencia)
elif potencia == 0:
    print(1)
else:
    print(potencia*-1)
