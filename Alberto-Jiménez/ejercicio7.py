#Autor: Alberto Jiménez
#Version: 1.0
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
#- El exponente sea positivo, sólo tienes que imprimir la potencia.
#- El exponente sea 0, el resultado es 1.
#- El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

print ("""-----------------------BASE Y EXPONENTE-----------------------""")

base = int(input("Dime un número de base: "))
expo = int(input("Dime un número de exponente: "))


potencia = base**expo

if expo == 0:
    print ("El resultado de exponer", expo, "a", base, "es 0")
elif expo >= 1:
    print ("El resultado de exponer", expo, "a", base, "es", potencia)
else:
    negativo = 1/potencia
    print ("El resultado de exponer", expo, "a", base, "es", negativo)

