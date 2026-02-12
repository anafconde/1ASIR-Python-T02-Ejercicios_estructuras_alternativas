# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 13
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

if mes < 1 or mes > 12:
    print("La fecha no es correcta")

elif mes == 2:
    if dia >= 1 and dia <= 28:
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia >= 1 and dia <= 30:
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")

else:
    if dia >= 1 and dia <= 31:
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")