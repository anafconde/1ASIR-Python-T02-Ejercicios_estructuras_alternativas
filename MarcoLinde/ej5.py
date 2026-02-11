#Ejercicio 5
#Escribe un programa que pida un nombre de usuario 
#y una contraseña y si se ha introducido “pepe” y “asdasd” se indica 
#“Has entrado al sistema”, sino se da un error.
name= input("Nombre: ")
passw= input("Contraseña: ")
if name=="pepe" and passw=="asdasd":
    print("Has entrado al sistema")
else:
    print("Error: nombre de usuario o contraseña incorrectos")
