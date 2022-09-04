#Solicitar a un usuario el valor del dividendo en UF y calcule su valor en pesos chilenos.
#Entradas
uf = float(input("Ingrese el valor de la UF en pesos chilenos: "))
dividendo = float(input("Ingrese el valor del dividendo en UF: "))
#Operación
dividendo_pesos = dividendo*uf
#Salida
print("Su dividendo en pesos chilenos es:",round(dividendo_pesos,2))