print("PRÉSTAMO BANCARIO")
x = int(input("Ingrese el valor de sus ingresos: "))
y = int(input("Ingrese el valor de las deudas que posea. Si no posee deudas escriba 0. : "))

if x > 945200 and y == 0:
    print("El préstamo que solicitó le será otorgado. ")
else:
    print("El préstamo que solicitó NO le será otorgado ya que no cumple con los requisitos necesarios. ")