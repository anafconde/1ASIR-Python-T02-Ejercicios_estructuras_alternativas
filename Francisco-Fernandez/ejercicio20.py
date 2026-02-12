# Autor: Paco Fernandez
# Version: 1.0

peso = float(input("Introduce el peso del paquete en kg: "))
zona = int(input("Introduce la zona de destino (1-5): "))

if peso > 5:
    print("El paquete no puede ser transportado (peso superior a 5 kg).")
else:
    if zona == 1:
        costo = 24
    elif zona == 2:
        costo = 20
    elif zona == 3:
        costo = 21
    elif zona == 4:
        costo = 10
    elif zona == 5:
        costo = 18
    else:
        costo = 0
        print("Zona inválida.")

    if costo != 0:
        cobro = peso * 1000 * costo 
        print("El cobro por la entrega es:", cobro, "euros")
