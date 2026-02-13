# Autor: Miguel Vilchez
# Versión: 1.0

dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

valida = False

if mes >= 1 and mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if 1 <= dia <= 31:
            valida = True
    elif mes in [4, 6, 9, 11]:
        if 1 <= dia <= 30:
            valida = True
    elif mes == 2:
        # Verificación básica de bisiesto para febrero
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            if 1 <= dia <= 29:
                valida = True
        else:
            if 1 <= dia <= 28:
                valida = True

if valida:
    print("La fecha es correcta.")
else:
    print("La fecha es incorrecta.")