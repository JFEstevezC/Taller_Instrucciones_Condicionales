print("MÚLTIPLOS")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

a1 = a % b
b1 = b % a

if a1 == 0:
    print("EL primer número es múltiplo del segundo número")
elif b1 == 0:
    print("El sedundo número es múltiplo del primer número")
else:
    print("Los números no son múltiplos del otro.")