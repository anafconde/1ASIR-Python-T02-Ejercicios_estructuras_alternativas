# Autor: Felipe
# Version: 1.0
import math
# Ejercicio 13
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia=int(input("Dime un numero de dia: "))
mes=int(input("Dime un numero de mes: "))
año=int(input("Dime un año: "))

if dia >= 0 and dia <= 31 :
    dia_correcto=dia
    if mes >= 0 and mes <= 12 :
        mes_correct=mes
        print("La fecha introducida es :",dia_correcto,"-",mes_correct,"-",año)
    else:
        print("La fecha introducida es incorrecta")

else:
        print("La fecha introducida es incorrecta")