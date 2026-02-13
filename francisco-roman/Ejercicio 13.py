dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if 1 <= mes <= 12 and 1 <= dia <= 31:
    print("Fecha correcta")
else:
    print("Fecha incorrecta")
