#Ejercicio 3
#Entradas
cant_amigos = int(input("Ingrese la cantidad de amigos: "))
cant_roll = int(input("Ingrese la cantidad de rolls: "))
cant_piezas_por_roll = int(input("Ingrese la cantidad de piezas x roll: "))
#Proceso
cant_piezas_amigos = round((cant_roll * cant_piezas_por_roll) / cant_amigos,)
#Salida
print("Cada amigos recibe",cant_piezas_amigos,"rolls cada uno")
