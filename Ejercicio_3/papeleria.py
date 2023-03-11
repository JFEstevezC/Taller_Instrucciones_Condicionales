print("PAPELERÍA")

a = int(input("Digite el precio o costo del artículo: "))

if a < 3000:
    g = a * 0.15
elif a >= 3000 and a <= 6000:
    g = 500
else:
    g = a * 0.25

P = a + g

print("El precio total del artículo es: " + str(P))
