# autor: Mario Arcos
# version: 1.0
# ejercicio 4


num1 = float(input("Introduce el primer numero (dividendo): "))
num2 = float(input("Introduce el segundo numero (divisor): "))


if num2 != 0:
    resultado = num1 / num2
    print(f"El resultado de la division es: {resultado}")
else:
    print("Aviso: No se puede dividir entre cero.")