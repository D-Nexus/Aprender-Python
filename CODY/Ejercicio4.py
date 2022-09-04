#Programas Secuenciales
#Nueva nota final
c1 = int(input())
c2 = int(input())
c3 = int(input())
c4 = int(input())
c5 = int(input())

nota_final_z = ((c2 + c3 + c4) / 3) * (((c1 + c5)/2) / 100)
nota_final_tradicional = (c1 + c2 + c3 + c4 + c5) / 5

print("Nota Final Z:",round(nota_final_z,1))
print("Nota Final tradicional:",round(nota_final_tradicional,1))