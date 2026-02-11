# Autor: David González Mora
# versión: 1.0
# Ejercicio 19 Relación de ejercicios
# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

numero = int(input("Introduce un número entre el 1 y el 12: "))

if numero == 1:
    print("Enero tiene 31 dias")
elif numero == 2:
    print("Febrero tiene 28 dias")
elif numero == 3:
    print("Marzo tiene 31 dias")
elif numero == 4:
    print("Abril tiene 30 dias")
elif numero == 5:
    print("Mayo tiene 31 dias")
elif numero == 6:
    print("Junio tiene 30 dias")
elif numero == 7:
    print("Julio tiene 31 dias")
elif numero == 8:
    print("Agosto tiene 31 dias")
elif numero == 9:
    print("Septiembre tiene 30 dias")
elif numero == 10:
    print("Octubre tiene 31 dias")
elif numero == 11:
    print("Noviembre tiene 30 dias")
elif numero == 12:
    print("Diciembre tiene 31 dias")
else: 
    print("Error:Introduce otro número")
    
