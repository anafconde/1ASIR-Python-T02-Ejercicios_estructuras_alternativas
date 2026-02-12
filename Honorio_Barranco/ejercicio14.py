# Autor: Honorio
# Version: 1.0
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva,
#  la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, 
# se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, 
# considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1;
#  y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, 
# y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

precio_inico=float(input("Introduzca el precio inicial: "))
tipo=input("Introduzca el tipo (A o B): ")
tamanio=int(input("Introduzca el tamaño (1 o 2): "))
kilo=int(input("Introduzca el kilo de uvas: "))

if tipo == "A":
    if tamanio == 1:
        final_precio=precio_inico + 0.20
    elif tamanio == 2:
        final_precio=precio_inico + 0.30
    else:
        print("Tamaño invalido")
        final_precio=precio_inico
elif tipo == "B":
    if tamanio == 1:
        final_precio=precio_inico - 0.30
    elif tamanio == 2:
        final_precio=precio_inico + 0.50
    else:
        print("Tamaño invalido")
        final_precio=precio_inico
else:
    print("El tipo qe has introducido no es valido")
    final_precio=precio_inico


ganancia=precio_inico * kilo

print("El producto recibira una ganacia de ",ganancia)