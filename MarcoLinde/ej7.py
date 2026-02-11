#Ejercicio 7
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
#la base y el exponente. Pueden ocurrir tres cosas:
#El exponente sea positivo, sólo tienes que imprimir la potencia.
#El exponente sea 0, el resultado es 1.
#El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
base= float(input("Pon un número: "))
exp= float(input("Pon otro número: "))
if exp>0:
    resultado= base**exp
elif exp==0:
    resultado= 1
else:
    resultado= 1/(base**abs(exp))
print("El resultado es: ", resultado)
