# Autor: Julio Gómez Hoces
# Versión: 1.0
# Ejercicio 14
precio_inicial = float(input("Precio inicial(kilo): "))
tipo = input("Tipo de uva ( di A o B): ").upper()
tamaño = int(input("Tamaño (di 1 o 2): "))
kilos = float(input("Cantidad de kilos entregados: "))

if tipo == "A":
    if tamaño == 1:
        precio_kilo = precio_inicial + 0.20
    elif tamaño == 2:
        precio_kilo = precio_inicial + 0.30
elif tipo == "B":
    if tamaño == 1:
        precio_kilo = precio_inicial - 0.30
    elif tamaño == 2:
        precio_kilo = precio_inicial - 0.50
else:
    print("Tipo de uva no válido")
    precio_kilo = 0

ganancia = precio_kilo * kilos

print("La ganancia es de:", round(ganancia, 2), "€")