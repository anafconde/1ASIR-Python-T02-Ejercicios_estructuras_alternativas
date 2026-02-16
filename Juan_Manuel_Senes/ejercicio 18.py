#autor: juan manuel senes 
#version 1.0 
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

print ("introduce un dia de la semana (del 1 al 7)")

dia=float(input("introduce un numero"))

dia1=str("lunes")
dia2=str("martes")
dia3=str("miercoles")
dia4=str("jueves")
dia5=str("viernes")
dia6=str("sabado")
dia7=str("domingo")

if (dia==1):
    print(1)
elif(dia==2):
    print(2)
elif(dia==3):
    print(3)
elif(dia==4):
    print(4)
elif(dia==5):
    print(5)
elif(dia==6):
    print(6)
elif(dia==7):
    print(7)
else:
    if(dia <=8):
        print("error introduce un numero segun los parametros")


