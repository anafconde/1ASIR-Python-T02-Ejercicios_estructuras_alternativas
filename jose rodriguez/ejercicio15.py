# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 15
# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a 
# cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si 
# son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, 
# de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. 
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

alumnos = int(input("Introduzca un numero de alumnos: "))

if alumnos >= 100:
    costealumno = 65
    total = alumnos * costealumno
    print("Cada alumno paga", costealumno, "euros")
    print("La escuela paga a la compañia", total, "euros")
elif alumnos >= 50:
    coste_lumno = 70
    total = alumnos * costealumno
    print("Cada alumno paga", costealumno, "euros")
    print("La escuela paga a la compañia", total, "euros")
elif alumnos >= 30:
    costealumno = 95
    total = alumnos * costealumno
    print("Cada alumno paga", costealumno, "euros")
    print("La escuela paga a la compañia", total, "euros")
else:
    total = 4000
    costealumno = total / alumnos
    print("La escuela paga a la compañia", total, "euros")
    print("Cada alumno debe pagar", costealumno, "euros")
  