# Author: David García Pérez
# Version: 1.0

# Ejercicio 4
# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

print("#################### División ######################")

dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

if divisor != 0:
    division=dividendo/divisor
    print("La división de", dividendo, "entre", divisor, "es", division)
elif divisor == 0:
    print("Error, el divisor no puede ser 0")
else:
    print("Error, los valores introducidos son incorrectos")

print("############################################################")