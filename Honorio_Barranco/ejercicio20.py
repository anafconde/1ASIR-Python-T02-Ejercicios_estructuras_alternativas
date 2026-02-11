# Autor: Honorio
# Version: 1.0
#Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. 
# El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

#Zona	Ubicación	Costo/gramo
#1	América del Norte	24.00 euros
#2	América Central	20.00 euros
#3	América del Sur	21.00 euros
#4	Europa	10.00 euros
#5	Asia	18.00 euros
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. 
#Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
# Programa para calcular el costo de envío de un paquete
peso_kg = float(input("Ingrese el peso: "))
zona = int(input("Ingrese la zona destino (1-Norte, 2-Central, 3-Sur, 4-Europa, 5-Asia): "))

if peso_kg > 5:
    print("El paquete no puede ser transportado por exceder 5 kg.")
else:
    if zona == 1:
        costo_por_gramo = 24.00
    elif zona == 2:
        costo_por_gramo = 20.00
    elif zona == 3:
        costo_por_gramo = 21.00
    elif zona == 4:
        costo_por_gramo = 10.00
    elif zona == 5:
        costo_por_gramo = 18.00

    peso_gramos = peso_kg * 1000
    costo_total = peso_gramos * costo_por_gramo

    # Mostrar resultado
    print("El costo por el envío del paquete es:",costo_total)
