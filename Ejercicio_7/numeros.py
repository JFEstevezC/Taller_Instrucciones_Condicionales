print("EL TERCER NÚMERO ES IGUAL A LA SUMA DE LOS DOS ANTERIORES?")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

r = a + b

if r == c:
    print("La suma de los dos primeros es igual al tercero.")
else:
    print("La suma de los dos primeros números no es igual al tercero.")