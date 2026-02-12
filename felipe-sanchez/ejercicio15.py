# Autor: Felipe
# Version: 1.0
import math
# Ejercicio 15
# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a 
# cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: 
# si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos,
# el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
# sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.



alumnos=int(input("Nº de alumnos: "))

if alumnos >= 100:
    print("Cada alumno tiene que pagar 65€ lo que hace un total de:",alumnos*65)
elif alumnos >= 50:
    print("Cada alumno tiene que pagar 70€ lo que hace un total de: ",alumnos*70)
elif alumnos >= 30:
    print("Cada alumno tiene que pagar 95€ lo que hace un total de:",alumnos*95)
else:
    print("Cada alumno tiene que pagar " ,4000/alumnos,"€ cada alumno")