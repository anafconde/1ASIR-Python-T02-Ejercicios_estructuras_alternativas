# Autor: Iván Plaza
# Versión: 1.0
# Primeros pasos con Python

# Ejercicio 8
# Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’
# y muestre el mensaje ‘ACEPTADA’ si la nota >= 5, edad >= 18 y sexo = 'F'.
# Si la nota y edad cumplen pero sexo = 'M', mostrar 'POSIBLE'.
# Si no se cumplen estas condiciones, mostrar 'NO ACEPTADA'.


nota = int(input("Introduce la nota: "))
edad = int(input("Introduce la edad: "))
sexo = input("Introduce el sexo (F/M): ").upper()  


if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")