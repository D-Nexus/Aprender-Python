#invitación a las funciones de python

#funciones que desarrolla el/la programador/a
def votos_partido(votos,partido): 
    i=0
    p = ""
    votos = votos+"$"
    cont_votos = 0
    while i<len(votos):
        if votos[i]!="$":
            p = p + votos[i]#
        else:
            if p == partido:
                cont_votos = cont_votos+1#1
            p = ""
        i=i+1#0->1->2->3->4->5->6->7
    return cont_votos
#programa principal
votos = "p3$p31$p4$p3$p1$p6$p4$p5$p310$p6$p8$p8$p4$p4$p2$p3"
copa = "c1:p1-p2-p31-p3;c2:p4-p5;c3:p6-p310-p7"
#le agrego un ; al final para formar un patrón
#es decir, que todos los coaliciones:partidos terminen con un ;
copa = copa + ";" 
coa_par = ""
while len(copa) != 0:
    #en este ciclo separo una coalición y sus partidos
    #eso queda en la variable coa_par
    i = 0
    while copa[i]!=";":
        coa_par = coa_par+copa[i]
        i = i+1
    #acá se recorre coa_par
    j = 0
    coa = ""#nombre de la coalición
    votos_coa = 0
    while coa_par[j] != ":":#c1:p1-p2-p31-p3
        coa = coa + coa_par[j]
        j = j+1
    print("Coalición:",coa)
    coa_par = coa_par[j+1:]+"-"#p1-p2-p31-p3-
    print("coa_par:",coa_par)
    while len(coa_par)!=0:#ir imprimiendo cada partido
        k = 0
        par = ""
        while coa_par[k] != "-":
            par = par + coa_par[k]
            k = k+1
        votos_par = votos_partido(votos,par)
        print("Partido",par,"votos",votos_par)
        votos_coa = votos_coa + votos_par
        coa_par = coa_par[k+1:]
    print("total votos coalición:",votos_coa)
    copa = copa[i+1:]
    print("copa",copa)
        






