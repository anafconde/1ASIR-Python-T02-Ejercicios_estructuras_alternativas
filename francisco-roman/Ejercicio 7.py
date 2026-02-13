base = float(input("Base: "))
exponente = int(input("Exponente: "))

if exponente > 0:
    print(base ** exponente)
elif exponente == 0:
    print(1)
else:
    print(1 / (base ** abs(exponente)))
