# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-11


#Ejercicio 19
# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
mes = int(input("Introduce un número entre 1 y 12: "))
if mes == 1:
    print("Enero tiene 31 días.")
elif mes == 2:
    print("Febrero tiene 28 días (o 29 en años bisiestos).")
elif mes == 3:
    print("Marzo tiene 31 días.")
elif mes == 4:
    print("Abril tiene 30 días.")
elif mes == 5:
    print("Mayo tiene 31 días.")
elif mes == 6:
    print("Junio tiene 30 días.")
elif mes == 7:
    print("Julio tiene 31 días.")
elif mes == 8:
    print("Agosto tiene 31 días.")
elif mes == 9:
    print("Septiembre tiene 30 días.")
elif mes == 10:
    print("Octubre tiene 31 días.")
elif mes == 11:
    print("Noviembre tiene 30 días.")
elif mes == 12:
    print("Diciembre tiene 31 días.")