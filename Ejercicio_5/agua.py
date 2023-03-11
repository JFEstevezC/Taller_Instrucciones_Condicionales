print("PRECIO DEL GASTO DE AGUA EN UNA VIVIENDA")
x = int(input("Ingrese el número de m^3 gastados en la vivienda: "))
g = 10000
if x < 50:
    r = g
elif 50 < x < 200:
    r = g + ((x-50)*2000)
else:
    r = g + ((x-50)*3000)
print("El precio total de acuerdo a sus m^3 gastados es: " +str(r))