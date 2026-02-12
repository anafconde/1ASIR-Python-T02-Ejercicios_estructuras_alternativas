# autor: Mario Arcos
# version: 1.0
# ejercicio 6

entrada = input("Introduce un caracter o palabra: ")


if len(entrada) == 1 and entrada.isupper():
    print(f"Correcto: '{entrada}' es una letra mayuscula.")
else:
    print(f"Error: '{entrada}' no es una letra mayuscula (puede ser minuscula, un numero, un simbolo o tener más de un caracter).")
