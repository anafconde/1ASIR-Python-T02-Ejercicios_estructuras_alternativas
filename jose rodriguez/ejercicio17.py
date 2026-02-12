# Autor: Jose Rodriguez
# Versión: 1.0
# Ejercicio 17 
# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el 
# número en letras (dato cadena) de la cara opuesta al resultado obtenido. 
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

numero = int(input("Introduce numero del dado: "))

if numero < 1 or numero > 6:
    print("ERROR: numero incorrecto.")
elif numero == 1:
    print("En la cara opuesta esta el 6")
elif numero == 2:
    print("En la cara opuesta esta el 5")
elif numero == 3:
    print("En la cara opuesta esta el 4")
elif numero == 4:
    print("En la cara opuesta esta el 3")
elif numero == 5:
    print("En la cara opuesta esta el 2")
else:
    print("En la cara opuesta esta el 1")
