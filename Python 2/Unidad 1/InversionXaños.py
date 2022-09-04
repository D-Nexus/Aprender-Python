

inversion = float(input("Cuando desea invertir: "))
interes = float(input("Interes anual: "))
años = int(input("Cantidad de años: "))

for i in range(años):
    inversion *= 1 + interes/100
    print("Capital tras "+ str(i+1)+ " años: "+ str(round(inversion,5)))
  


        