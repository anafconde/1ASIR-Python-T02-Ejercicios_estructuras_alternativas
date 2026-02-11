Leer alumnos

Si alumnos >= 100 Entonces
    precio_alumno = 65
    total = alumnos * precio_alumno
Sino
    Si alumnos >= 50 Entonces
        precio_alumno = 70
        total = alumnos * precio_alumno
    Sino
        Si alumnos >= 30 Entonces
            precio_alumno = 95
            total = alumnos * precio_alumno
        Sino
            total = 4000
            precio_alumno = total / alumnos
        FinSi
    FinSi
FinSi

Escribir "Cada alumno paga: ", precio_alumno
Escribir "Total a pagar a la compañía: ", total
