# Autor: Iván Plaza
# Version: 1.0
# Primeros pasos con Python 

#Ejercicio 20
#  Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur,
#  Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido.
#  Lo anterior se muestra en la tabla:


zonas = ["América del Norte", "América Central", "América del Sur", "Europa", "Asia"]
costos_por_gramo = [24.0, 20.0, 21.0, 10.0, 18.0]


peso_kg = float(input("Ingrese el peso del paquete en kg: "))
print("Zonas disponibles:")
for i, zona in enumerate(zonas, start=1):
    print(f"{i} - {zona}")

zona_num = int(input("Ingrese el número de la zona de destino: "))


if peso_kg > 5:
    print("Entrega rechazada: el paquete excede el límite de 5 kg.")
elif zona_num < 1 or zona_num > 5:
    print("ERROR")
else:
    peso_g = peso_kg * 1000
    costo = peso_g * costos_por_gramo[zona_num - 1]
    print(f"El costo del envío es: {costo:.2f} euros")