# Author: David García Pérez
# Version: 1.0

# Ejercicio 20
# Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia.
# El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

# Zona	Ubicación	Costo/gramo
# 1	América del Norte	24.00 euros
# 2	América Central	20.00 euros
# 3	América del Sur	21.00 euros
# 4	Europa	10.00 euros
# 5	Asia	18.00 euros

# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

print("#################### Cálculo costo de transporte ######################")

zona = int(input("Introduce la zona de envío (1-5): "))
peso = float(input("Introduce el peso del paquete (kg): "))

if peso > 5:
    print("No se puede enviar el paquete, ya que supera los 5 kg de peso máximo")
else:
    gramos = peso * 1000
    if zona == 1:
        costo_gramo = 24.00
        destino = "América del Norte"
    elif zona == 2:
        costo_gramo = 20.00
        destino = "América Central"
    elif zona == 3:
        costo_gramo = 21.00
        destino = "América del Sur"
    elif zona == 4:
        costo_gramo = 10.00
        destino = "Europa"
    elif zona == 5:
        costo_gramo = 18.00
        destino = "Asia"
    else:
        print("Zona incorrecta")

    total = gramos * costo_gramo

    print("Destino:", destino)
    print("Peso del paquete:", gramos, "gramos")
    print("Costo por gramo:", costo_gramo, "€")
    print("Total a pagar:", total, "€")

print("############################################################")