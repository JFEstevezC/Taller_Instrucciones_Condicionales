import math
print("ECUACIÓN CUADRÁTICA")
print("La ecuación cuadrática es de la forma ax^2 + bx + c = 0")

a = int(input("Ingrese el coeficiente de ax^2: "))
b = int(input("Ingrese el coeficiente de bx: "))
c = int(input("Ingrese el coeficiente de c: "))

r = complex
r1 = complex
r2 = complex

e = (b^2)-(4*a*c)

r = math.sqrt(e)

r1 = (-b + r)/2*a
r1 = (-b - r)/2*a

print (r1)
print (r2)





# Calcular e imprimir las raíces de la ecuación de segundo grado de coeficientes reales. El programa debe tener en cuenta los diferentes casos que puedan surgir: la existencia de dos raíces reales distintas, de dos raíces reales iguales y de dos raíces complejas.