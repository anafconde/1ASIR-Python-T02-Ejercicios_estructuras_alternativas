#Autor: Alberto Jiménez
#Version: 1.0
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor).

print ("""-----------------------ORDENAR-----------------------""")

num1 = float(int(input("Diga un número: ")))
num2 = float(int(input("Diga un número: ")))
num3 = float(int(input("Diga un número: ")))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("Orden:", num1, num2, num3)
    else:
        print("Orden:", num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("Orden:", num2, num1, num3)
    else:
        print("Orden:", num2, num3, num1)
else:
    if num1 >= num2:
        print("Orden:", num3, num1, num2)
    else:
        print("Orden:", num3, num2, num1)