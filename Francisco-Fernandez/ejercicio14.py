# Autor: Paco Fernandez
# Version: 1.0
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
# se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, 
# considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al 
# precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, 
# y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

precio_inicial = float(input("Introduce el precio inicial por kilo: "))
kilos = float(input("Introduce la cantidad de kilos: "))
tipo = input("Introduce el tipo de uva (A/B): ")
tamano = int(input("Introduce el tamaño (1/2): "))

if tipo == "A":
    if tamano == 1:
        precio_final = precio_inicial + 0.20
    else:  
        precio_final = precio_inicial + 0.30
elif tipo == "B":
    if tamano == 1:
        precio_final = precio_inicial - 0.30
    else:  
        precio_final = precio_inicial - 0.50

ganancia = precio_final * kilos

print("El precio final por kilo es:", precio_final)
print("La ganancia total es:", ganancia)
