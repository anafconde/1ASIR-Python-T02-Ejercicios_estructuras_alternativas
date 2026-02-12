# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 7
# Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base = int(input("Introduce una base: "))
expo = int(input("Introduce un exponente: "))
resultadopos = (base**expo)
resultadone = (1//base**expo)

if expo > 0:
    print("La potencia es: ", resultadopos)
elif expo == 0:
    print("El resultado es 1")
else:
    print("El resultado es: ", resultadone)