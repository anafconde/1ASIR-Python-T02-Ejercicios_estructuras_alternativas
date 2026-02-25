# Autor: Miguel Vilchez
# Versión: 1.0

n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(n1, n2, n3)
    else:
        print(n1, n3, n2)
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(n2, n1, n3)
    else:
        print(n2, n3, n1)
else:
    if n1 >= n2:
        print(n3, n1, n2)
    else:
        print(n3, n2, n1)