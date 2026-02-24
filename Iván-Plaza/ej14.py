# Autor: Iván Plaza
# Versión: 1.0
# Primeros pasos con Python

# Ejercicio 14
# Calcula la ganancia de un productor según tipo y tamaño de uva.

precio_inicial = float(input("Introduce el precio inicial por kilo (€): "))
tipo = input("Introduce el tipo de uva (A/B): ").upper() 
tamano = int(input("Introduce el tamaño de la uva (1/2): "))
kilos = float(input("Introduce los kilos entregados: "))


precio_final = precio_inicial


if tipo == 'A':
    if tamano == 1:
        precio_final += 0.20
    elif tamano == 2:
        precio_final += 0.30
    else:
        print("Tamaño no válido.")
elif tipo == 'B':
    if tamano == 1:
        precio_final -= 0.30
    elif tamano == 2:
        precio_final -= 0.50
    else:
        print("Tamaño no válido.")
else:
    print("Tipo de uva no válido.")


ganancia = precio_final * kilos
print(f"\nEl productor recibirá: €{ganancia:.2f}")
