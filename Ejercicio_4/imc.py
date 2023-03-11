print("ÍNDICE DE MASA CORPORAL")
p = int(input("Ingrese su peso en Kg: "))
a = float(input("Ingrese su altura en metros: "))

IMC = p / (a*a)
if IMC < 16:
    print(IMC)
    print("Criterio de ingreso en hospital")
elif 16 < IMC < 17:
    print(IMC)
    print("Infrapeso")
elif 17 < IMC < 18:
    print(IMC)
    print("Bajo peso")
elif 18 < IMC < 25:
    print(IMC)
    print("Peso normal (saludable)")
elif 25 < IMC < 30:
    print(IMC)
    print("Sobrepeso (obesidad grado I)")
elif 30 < IMC < 35:
    print(IMC)
    print("Sobrepeso crónico (obesidad grado II)")
elif 35 < IMC < 40:
    print(IMC)
    print("Obesidad premórbida (obesidad grado III)")
else:
    print(IMC)
    print("Obesidad mórbida (obesidad de grado IV)")
