# Autora: Noelia López Poyatos
# Version: 1.0
# Descripción: Primeros pasos con Python
# Fecha: 2025-02-11


#Ejercicio 17. Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras 
# y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
#Ejemplo:
#Introduzca número del dado: 5
#En la cara opuesta está el "dos".


resultado=int(input("Introduce el resultado obtenido al lanzar el dado (entre 1 y 6): "))
if resultado==1:
    print("La cara opuesta al resultado obtenido es: seis")
elif resultado==2:
    print("La cara opuesta al resultado obtenido es: cinco")
elif resultado==3:
    print("La cara opuesta al resultado obtenido es: cuatro")
elif resultado==4:
    print("La cara opuesta al resultado obtenido es: tres")
elif resultado==5:
    print("La cara opuesta al resultado obtenido es: dos")
elif resultado==6:
    print("La cara opuesta al resultado obtenido es: uno")
else:
    print("El número introducido no es válido. Debe ser un número entero entre 1 y 6.")

