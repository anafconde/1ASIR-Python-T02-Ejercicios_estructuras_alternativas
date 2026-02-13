# Autor: Miguel Vilchez
# Versión: 1.0

alumnos = int(input("Número de alumnos: "))

if alumnos >= 100:
    costo_alumno = 65
elif alumnos >= 50:
    costo_alumno = 70
elif alumnos >= 30:
    costo_alumno = 95
else:
    costo_alumno = 4000 / alumnos # Pago individual
    costo_total = 4000

if alumnos >= 30:
    costo_total = alumnos * costo_alumno

print(f"Pago a la compañía: {costo_total} euros")
print(f"Pago por alumno: {costo_alumno:.2f} euros")