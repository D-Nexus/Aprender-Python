#Programas Secuenciales
#Costo total de un viaje en auto en combustible
distancia = float(input())
rendimiento = float(input())
costoxlitro = float(input())

costo_total = (costoxlitro * distancia) / rendimiento

print(round(costo_total,2))