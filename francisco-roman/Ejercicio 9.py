Leer a
Leer b
Leer c

Si a >= b Y a >= c Entonces
    mayor = a
    Si b >= c Entonces
        medio = b
        menor = c
    Sino
        medio = c
        menor = b
    FinSi
Sino
    Si b >= a Y b >= c Entonces
        mayor = b
        Si a >= c Entonces
            medio = a
            menor = c
        Sino
            medio = c
            menor = a
        FinSi
    Sino
        mayor = c
        Si a >= b Entonces
            medio = a
            menor = b
        Sino
            medio = b
            menor = a
        FinSi
    FinSi
FinSi

Escribir mayor, medio, menor
