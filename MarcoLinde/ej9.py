#Ejercicio 9
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
a= float(input("Pon un número: "))
b= float(input("Pon otro número: "))
c= float(input("Pon otro número más: "))
numeros= [a, b, c]
numeros.sort(reverse= True)
print("Números ordenados: ", numeros)
