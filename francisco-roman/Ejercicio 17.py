numero = int(input("Introduce número del dado: "))

if numero < 1 or numero > 6:
    print("ERROR: número incorrecto")
else:
    opuesta = 7 - numero
    nombres = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]
    print("En la cara opuesta está el", nombres[opuesta - 1])
