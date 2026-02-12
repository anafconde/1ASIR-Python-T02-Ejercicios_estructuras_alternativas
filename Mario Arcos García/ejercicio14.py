# autor: Mario Arcos
# version: 1.0
# ejercicio 14


precio_inicial = float(input("Precio inicial por kilo: "))
kilos = float(input("Cantidad de kilos: "))
tipo_de_uva = input("Tipo de uva (A o B): ")
tamano = int(input("Tamaño de uva (1 o 2: "))


if tipo_de_uva == 'A':
    if tamano == 1:
        precio_inicial += 0.20
    else:
        precio_inicial += 0.30
elif tipo_de_uva == 'B':
    if tamano == 1:
        precio_inicial -= 0.30
    else:
        precio_inicial -= 0.50

ganancia = precio_inicial * kilos
print(f"La ganancia total es: {ganancia}")