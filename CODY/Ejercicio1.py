#Programas Secuenciales
#Ejercicio de como calcular el credito hipotecario
h = int(input()) #Monto inicial
n = int(input()) #Cantidad de años
i = float(input()) #Intereses
#Formulas
r = i/(100*12)
m = round((h*r) / (1-(1+r)**(-12*n))) #Cuota mensual
#Proceso
cuota_año = (m*12)*n
interes_pagado = ((m*12)*n)-h
porcentaje = ((((m*12)*n)-h)*100)/h
#Salidas
print("Crédito por $",h,"a un plazo de",n,"años,","con una tasa de",i,"%")
print("Cuota mensual a pagar: $",m)
print("Monto total pagado: $",cuota_año)
print("Intereses pagados: $",interes_pagado)
print("Porcentaje que representan los intereses:",round(porcentaje,2),"%")
