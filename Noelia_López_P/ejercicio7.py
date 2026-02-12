# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-11


# Ejercicio 7. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

base=float(input("Introduce la base: "))
exponente=float(input("Introduce el exponente: "))
if exponente>0:
    resultado=base**exponente
    print("El resultado es:", resultado)
elif exponente==0:
    print("El resultado es: 1")
else:   
    resultado=1/(base**(-exponente))
    print("El resultado es:", resultado)
    