#Autor: Alberto Jiménez
#Version: 1.0
"""El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, 
de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. 
Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje."""

print ("""-----------------------VIAJE DE FIN DE CURSO-----------------------""")

alumnos = int(input("Introduce el número de alumnos: "))

if alumnos > 100:
    total = alumnos*65+4000
    print ("El total de alumnos son", alumnos, "el costo es de 65€, el total sería",total,"€")
elif alumnos > 50:
    total = alumnos*70+4000
    print("El total de alumnos son", alumnos, "el costo es de 70€, el total sería", total,"€")
elif alumnos <= 49 or alumnos > 30:
    total = alumnos*95+4000
    print ("El total de alumnos son", alumnos, "el costo es de 95€, el total sería", total,"€")
elif alumnos < 30:
    total = alumnos*65+4000
    print ("El total de alumnos son", alumnos, "el costo es de 4000€, el total sería", total,"€")
