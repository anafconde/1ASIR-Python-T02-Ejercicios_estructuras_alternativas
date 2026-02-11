#Autor: Alberto Jiménez
#Version: 1.0
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

print ("""-----------------------FECHAS CORRECTAS-----------------------""")

dia = int(input("Dime un día del mes: "))
mes = int(input("Dime un mes del año: "))
anio = int(input("Dime un año: "))

if dia > 0 and dia <= 31:
    if mes > 0 and mes <= 12:
        if anio > 0 and anio <2027:
            print ("La fecha que has ofrecido es:", dia,"/",mes,"/",anio)
else:
    print ("La fecha es incorrecta.")