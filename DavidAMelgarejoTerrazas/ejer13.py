"""
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
"""
dia=int(input("Dia: "))
mes=int(input("Mes: "))
year=int(input("Año: "))
bisiesto=False
if mes>12 or mes<1:
    print("Mes no válido")
else:
    if year%4==0 and (year%100!=0 or year%400==0):
        bisiesto=True

    if mes==2:
        if bisiesto and dia<=29:
            print("Fecha válida")
        elif not bisiesto and dia<=28:
            print("Es Fecha válida")
    elif mes in [4,6,9,11] and dia<=30:
        print("Fecha válida")
    elif mes in [1,3,5,7,8,10,12] and dia<=31:
        print("Fecha válida")
    else:
        print("Fecha no válida")