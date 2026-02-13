# Autor: Miguel Vilchez
# Versión: 1.0

cara = int(input("Introduzca número del dado: "))

if cara == 1:
    print("En la cara opuesta está el 'seis'.")
elif cara == 6:
    print("En la cara opuesta está el 'uno'.")
elif cara == 2:
    print("En la cara opuesta está el 'cinco'.")
elif cara == 5:
    print("En la cara opuesta está el 'dos'.")
elif cara == 3:
    print("En la cara opuesta está el 'cuatro'.")
elif cara == 4:
    print("En la cara opuesta está el 'tres'.")
else:
    print("ERROR: número incorrecto.")