# Autora: Víctor Manuel
# Versión: 1.0
# ejercicio 15:
# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras
# y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

print("Dime un numero del 1 al 6")
a= int(input("dame el numero "))

if a == 6 :
    print("1")
elif a == 1:
    print("6")
elif a == 5 :
    print("2")
elif a == 2:
    print("5")
elif a == 4 :
    print("3")
elif a == 3:
    print("4")
elif a > 6 or a < 1 :
    print("ERROR: número incorrecto.")
