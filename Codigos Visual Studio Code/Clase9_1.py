#Codigo para imprimir horas y minutos
#Son 3 horas con 10 minutos cada una
#Entradas
horas = 1
minutos = 0
#Proceso
while horas <= 23:
    while minutos <= 59: 
        if horas <10 and minutos <10:
            print("0",horas,":","0",minutos)
        elif horas <10:
            print("0",horas,":",minutos)
        elif minutos <10:
            print(horas,":","0",minutos)
        else:
            print(horas,":",minutos)
        minutos += 1
    horas += 1
    minutos = 0
print("hemos terminado")