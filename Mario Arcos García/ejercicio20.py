# autor: Mario Arcos
# version: 1.0
# ejercicio 20

peso_kg = float(input("Introduce el peso del paquete en kg: "))

if peso_kg > 5:
    print("La entrega rechazada: El paquete supera el limite de 5kg.")
else:
    peso_gramos = peso_kg * 1000
    
    print("\n--- Zonas de envio ---")
    print("1. América del Norte (24.00€/g)")
    print("2. América Central (20.00€/g)")
    print("3. América del Sur (21.00€/g)")
    print("4. Europa (10.00€/g)")
    print("5. Asia (18.00€/g)")
    
    zona = int(input("Seleccione el número de la zona de destino: "))

    if zona == 1:
        costo = peso_gramos * 24
    elif zona == 2:
        costo = peso_gramos * 20
    elif zona == 3:
        costo = peso_gramos * 21
    elif zona == 4:
        costo = peso_gramos * 10
    elif zona == 5:
        costo = peso_gramos * 18
    else:
        costo = 0
        print("Error: Zona no válida.")
    if costo > 0:
        print(f"\nEl costo total del envio es: {costo:,.2f} €.")