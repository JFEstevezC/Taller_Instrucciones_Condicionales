print("EJERCIO DE COORDENADAS CARTESIANAS")
x = int(input("Escriba el punto en x de la coordenada cartesiana de la que quiere conocer el cuadrante en el que se encuentra ubicado: "))
y = int(input("Escriba el punto en y de la coordenada cartesiana de la que quiere conocer el cuadrante en el que se encuentra ubicado: "))

if x == 0 and y == 0:
    print("Los puntos que usted escribió en x y en y se encuentran en el origen.")
elif x == 0 and y != 0:
    print("Los puntos que usted ingresó se encuentran en el eje y")
elif x != 0 and y == 0:
    print("Los puntos que usted ingresó se encuentran en el eje x")
elif x > 0 and y > 0:
    print("Los puntos que usted ingresó se encuentran en el cuadrante I")
elif x < 0 and y > 0:
    print("Los puntos que usted ingresó se encuentran en el cuadrante II")
elif x < 0 and y < 0:
    print("Los puntos que usted ingresó se encuentran en el cuadrante III")
else:
    print("Los puntos que usted ingresó se encuentran en el cuadrante IV")
