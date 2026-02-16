#autor: juan manuel senes 
#version 1.0 
#Algoritmo que pida los puntos centrales x1, y1, x2, y2 y los radios r1, r2 de dos circunferencias y las clasifique en uno de estos estados:

#exteriores
#tangentes exteriores
#secantes
#tangentes interiores
#interiores
#concéntricas

print ("dame los puntos centrales y los radios de los siguientes estados")
x1 = float (input ("dame el punto central x1: "))
y1 = float (input ("dame el punto central y1: "))
r1 = float (input ("dame el radio r1: "))
r2 = float (input ("dame el radio r2: "))
x2 = float (input ("dame el punto central x2: "))
y2 = float (input ("dame el punto central y2: "))

if (x1-x2)**2 + (y1-y2)**2 > (r1+r2)**2:
    print ("exteriores")
elif (x1-x2)**2 + (y1-y2)**2 == (r1+r2)**2:
    print ("tangentes exteriores")
elif (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2 and (x1-x2)**2 + (y1-y2)**2 > (r1-r2)**2:
    print ("secantes")
elif (x1-x2)**2 + (y1-y2)**2 == (r1-r2)**2:
    print ("tangentes interiores")
elif (x1-x2)**2 + (y1-y2)**2 < (r1-r2)**2 and (x1-x2)**2 + (y1-y2)**2 > 0:
    print ("interiores")    
elif (x1-x2)**2 + (y1-y2)**2 == 0:
    print ("concéntricas")
    


