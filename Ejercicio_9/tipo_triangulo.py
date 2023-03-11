import math
print("TIPO DE TRIÁNGULO")
a = int(input("Ingrese el lado a del triángulo: "))
b = int(input("Ingrese el lado b del triángulo: "))
c = int(input("Ingrese el lado c del triángulo: "))

r = a^2 + b^2

if r == c^2:
    print("El triángulo es rectángulo")
elif r < c^2:
    print("El triángulo es agudo")
else:
    print("El triángulo es obtuso")