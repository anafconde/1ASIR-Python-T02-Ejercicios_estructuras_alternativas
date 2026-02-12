# Autor: Felipe
# Version: 1.0
import math
#Ejercicio 17
# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y 
# muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.



resultado = int(input("Introduce el resultado del dado (1-6): "))


if resultado < 1 or resultado > 6:
    print("ERROR: número incorrecto.")
else:
    if resultado == 1:
        opuesta = "seis"
    elif resultado == 6:
        opuesta = "uno"
    elif resultado == 2:
        opuesta = "cinco"
    elif resultado == 5:
        opuesta = "dos"
    elif resultado == 3:
        opuesta = "cuatro"
    elif resultado == 4:
        opuesta = "tres"
    
    print("La cara opuesta del dado es: ",opuesta)