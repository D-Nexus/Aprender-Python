#Entrada
monto_credito = int(input())
cantidad_años = int(input())
tasa_interes = float(input())
#Proceso
r = tasa_interes / (100 * 12)
m = round((monto_credito * r) / (1 - ((1 + r)**(-12 * cantidad_años))),)
monto_total = round((m * 12) * cantidad_años,)
total_intereses = round((monto_total - monto_credito),)
porcentaje_intereses = round((total_intereses * 100) / monto_credito,2)
#Salida
print("Crédito por $",monto_credito,"a un plazo de",cantidad_años,", con una tasa de",tasa_interes,"%")
print("Cuota mensual a pagar: $",m)
print("Monto total pagado: $",monto_total)
print("Intereses pagados: $",total_intereses)
print("Porcentaje que representan los intereses: ",porcentaje_intereses,"%")