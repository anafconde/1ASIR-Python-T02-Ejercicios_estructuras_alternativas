# autor: Mario Arcos
# version: 1.0
# ejercicio 8

nota = float(input("Introduce la nota (0-10): "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (f/m): ") 


if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")