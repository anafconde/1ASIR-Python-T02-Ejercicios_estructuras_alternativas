# Autor: Iván Plaza
# Version: 1.0
# Primeros pasos con Python 

#Ejercicio 18
# Realiza un programa que pida el día de la semana (del 1 al 7) 
# y escriba el día correspondiente. Si introducimos otro número nos da un error.


dia = [1,2,3,4,5,6,7]
semana = ["lunes","Marter","Miercoles","jueves","viernes","sabado","domingo"]
valor = int(input("Introduce el numero de la semana: "))

if valor in dia and valor < 7 :
    print(f"El día correspondiente es: {semana[valor - 1]}")

else:
    print ("ERROR")