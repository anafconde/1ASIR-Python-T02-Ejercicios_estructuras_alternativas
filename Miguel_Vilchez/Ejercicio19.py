# Autor: Miguel Vilchez
# Versión: 1.0

mes = int(input("Introduce número de mes (1-12): "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("Tiene 31 días.")
elif mes in [4, 6, 9, 11]:
    print("Tiene 30 días.")
elif mes == 2:
    print("Tiene 28 o 29 días.")
else:
    print("Mes no válido.")