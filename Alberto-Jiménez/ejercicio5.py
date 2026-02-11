#Autor: Alberto Jiménez
#Version: 1.0
#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y 
# “asdasd” se indica “Has entrado al sistema”, sino se da un error.

print ("""-----------------------AUTENTICACIÓN-----------------------""")

user = str(input("Introduce tu usuario: "))
passwd = str(input("Intrduzca su contraseña: "))

if user == 'pepe' and passwd == 'asdasd':
    print ("Has entrado el sistema.")
else:
    print ("Error!. Datos introducidos erróneos.")