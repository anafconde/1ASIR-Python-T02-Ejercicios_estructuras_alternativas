# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-11

# Ejercicio 15. El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar 
# a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. 
# La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, 
# el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
# sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses 
# y lo que debe pagar cada alumno por el viaje.
alumnos = int(input("Introduce el número de alumnos: "))

if alumnos >= 100:
    costo_alumno = 65
    total_pago = alumnos * costo_alumno
elif alumnos >= 50:
    costo_alumno = 70
    total_pago = alumnos * costo_alumno
elif alumnos >= 30:
    costo_alumno = 95
    total_pago = alumnos * costo_alumno
else:
    total_pago = 4000
    costo_alumno = total_pago / alumnos

print(f"El pago a la compañía de autobuses es de {total_pago} euros.")
print(f"El costo por alumno es de {costo_alumno} euros.")