#Condicionales
#Determinar el aumento de salario
salario = float(input())

if salario <= 500000:
    aumento = salario * 0.10
elif salario > 500000 and salario <= 1000000:
    aumento = salario * 0.07
else:
    aumento = salario * 0.05
    
salario_nuevo = salario + aumento
print(salario_nuevo)