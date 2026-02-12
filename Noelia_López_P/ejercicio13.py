# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-11

# Ejercicio 13. Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_mes = 30
elif mes == 2:
    dias_mes = 28

if dia > dias_mes:
    print("La fecha no es correcta.")
else:
    print("La fecha es correcta.")

    