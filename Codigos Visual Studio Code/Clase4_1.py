#Ejercicio 1
#Entrada
valor_prod = float(input("Ingrese el valor del producto en USD: "))
valor_usd = float(input("Ingrese el valor del dolar de hoy en CLP: "))
#Proceso
valor_prod_clp = round(valor_prod * valor_usd,)
#Salida
print("El valor del producto en CLP es",valor_prod_clp)