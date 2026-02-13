a = float(input("Número 1: "))
b = float(input("Número 2: "))
c = float(input("Número 3: "))

lista = [a, b, c]
lista.sort(reverse=True)

print("Ordenados de mayor a menor:", lista[0], lista[1], lista[2])
