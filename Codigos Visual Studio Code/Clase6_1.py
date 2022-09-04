nombre_piloto = input("Ingrese su nombre: ")
grado = input("Ingrese su grado de piloto: ")
horas_vuelo = int(input("Ingrese la cantidad de horas de vuelo: "))
dias_vuelos = int(input("Ingrese la cantidad de dias de vuelo: "))
sueldo_base = 1000
valor_hora = 100
paga = 0
paga_total = 0
if (grado == "novato" or grado == "experimentado" or grado == "senior") and horas_vuelo >= 0 and dias_vuelos >= 0:
    paga = (horas_vuelo * valor_hora) + sueldo_base
    #Procesos y salidas
    if grado == "novato":
        if dias_vuelos >= 0 and dias_vuelos <= 2:
            paga_total = (paga * 0.04) + paga
            print("Su sueldo es:",paga_total)
        elif dias_vuelos == 3:
            paga_total = (paga * 0.06) + paga
            print("Su sueldo es:",paga_total)
        elif dias_vuelos == 4:
            paga_total = (paga * 0.1) + paga
            print("Su sueldo es:",paga_total)
        else:
            paga_total = (paga * 0.12) + paga
            print("Su sueldo es:",paga_total)
    elif grado == "experimentado":
        if dias_vuelos >= 0 and dias_vuelos <= 2:
            paga_total = (paga * 0.06) + paga
            print("Su sueldo es:",paga_total)
        elif dias_vuelos == 3:
            paga_total = (paga * 0.08) + paga
            print("Su sueldo es:",paga_total)
        elif dias_vuelos == 4:
            paga_total = (paga * 0.12) + paga
            print("Su sueldo es:",paga_total)
        else:
            paga_total = (paga * 0.15) + paga
            print("Su sueldo es:",paga_total)
    else:
        if dias_vuelos >= 0 and dias_vuelos <= 2:
            paga_total = (paga * 0.1) + paga
            print("Su sueldo es:",paga_total)
        elif dias_vuelos == 3:
            paga_total = (paga * 0.1) + paga
            print("Su sueldo es:",paga_total)
        elif dias_vuelos == 4:
            paga_total = (paga * 0.15) + paga
            print("Su sueldo es:",paga_total)
        else:
            paga_total = (paga * 0.15) + paga
            print("Su sueldo es:",paga_total)
else:
        print("Lo siento, no podemos procesar su solicitud en estos momentos") 
