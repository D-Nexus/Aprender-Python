#Variables
votos = "p3$p31$p4$p3$p1$p6$p4$p5$p310$p6$p8$p8$p4$p4$p2$p3"
#función 1
def votos_partido(votos,partido):
    cant_votos = 0
    i = 0
    letras = ""
    votos = votos+"$" #Sumamos un $ al string para contar el ultimo voto
    while i < len(votos): #Recorremos el largo del string
        if votos[i] != "$":
            letras += votos[i] #Voto antes del $
        else:
            #print(letras)
            if letras == partido: #Compara voto con el partido
                cant_votos += 1 #Suma 1 voto para ese partido
            letras = "" #Vaciamos el string con el voto 
        i +=1
    return cant_votos #Retornamos la cantidad de votos

#Programa
print("La cantidad de votos es:",votos_partido(votos,"p3"))
print("La cantidad de votos es:",votos_partido(votos,"p6"))
print("La cantidad de votos es:",votos_partido(votos,"p7"))
#Segunda parte
#c1:p1-p2-p31-p3;c2:p4-p5;c3:p6-p310-p7
grupos = input("Ingrese coaliciones: ")
votos_de_partido = input("Ingrese votos por partido: ")

grupos += ";"

while len(grupos) != 0:
    i = 0
    grupo = ""
    while grupos[i] !=";":
        grupo += grupos[i]
        if grupos[i] == ":":
            coalicion = grupo
            print("Coalición:",coalicion)
            coalicion = ""
            grupo = ""
        if grupos[i] == "p":
            grupo1 = ""
            j = i
            while "-" not in grupo1:
                grupo1 += grupos[j]
                j+=1
            grupo1 = grupo1[:j-1]
            print(grupo1)
            grupo1 = ""
            grupo = ""
        i+=1
    grupos = ""
    
    