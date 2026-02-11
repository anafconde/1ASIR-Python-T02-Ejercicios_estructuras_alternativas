# Autora: Víctor Manuel
# Versión: 1.0
# ejercicio 9:
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

n1= int(input("dame un numero "))
n2= int(input("dame otro numero "))
n3= int(input("dame otro numero "))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print("Orden:", n1 , n2 , n3)
    else:
        print("Orden:" ,n1, n3 , n2)

elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print("Orden:" , n2, n1, n3)
    else:
        print("Orden:" , n2, n3, n1)

else: # Si n3 es el mayor
    if n1 >= n2:
        print("Orden:", n3, n1, n2)
    else:
        print("Orden:" , n3, n2, n1)