# Autor: Miguel Vilchez
# Versión: 1.0

base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
    print("Resultado:", resultado)
elif exponente == 0:
    print("Resultado: 1")
else:
    resultado = 1 / (base ** abs(exponente))
    print("Resultado:", resultado)