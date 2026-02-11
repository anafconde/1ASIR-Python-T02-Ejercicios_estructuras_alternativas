# Autor: David González Mora
# versión: 1.0
# Ejercicio 9 Relación de ejercicios
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

n = int(input("Introduce un número"))
n1 = int(input("Introduce un número"))
n2 = int(input("Introduce un número"))

if n >= n1 and n >= n2 and n1 >= n2:
    if n1 >= n2:
        print(n, n1, n2)
    else:
        print(n, n2, n1)

elif n1 >= n and n1 >= n2: 
    if n >= n2:
        print(n1, n, n2)
    else:
        print(n1, n2, n)

else:
    if n >= n1:
        print(n2, n, n1)
    else:
        print(n2, n1, n)
