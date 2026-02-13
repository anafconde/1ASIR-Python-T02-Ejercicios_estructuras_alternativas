A = float(input("Lado A: "))
B = float(input("Lado B: "))
C = float(input("Lado C: "))

if A == B and B == C:
    print("Equilátero")
elif A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    print("Rectángulo")
elif A == B or A == C or B == C:
    print("Isósceles")
else:
    print("Escaleno")
