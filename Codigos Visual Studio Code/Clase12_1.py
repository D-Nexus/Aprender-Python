#función para saber tu dia de nacimiento
def dia_de_la_semana(dd,mm,aaaa):
    a = (14-mm)//12
    y = aaaa - a
    m = mm + (12*a)-2
    d = (dd + y + (y//4) - (y//100) + (y//400) + ((31*m)//12))%7
    if d == 0:
      return "Domingo"
    elif d == 1:
      return "Lunes"
    elif d == 2:
      return "Martes"
    elif d == 3:
      return "Miercoles"
    elif d == 4:
      return "Jueves"
    elif d == 5:
      return "Viernes"
    else:
      return "Sabado"
    return d
def fecha(datos):
  dia_invitado = int(datos[:2])
  mes_invitado = int(datos[2:4])
  agno_invitado = int(datos[4:8])
  nom_invitado = invitado[9:]
  return dia_invitado,mes_invitado,agno_invitado,nom_invitado
#Programa
print(dia_de_la_semana(20,1,2003)) 
invitados = '16052000,Sofia;29022000,Silvia;01082000,Andrea'

i = 0
invitado = ""
while invitados[i] !=";":
  invitado = invitado + invitados[i]
  i += 1
print(invitado) #16052000,Sofia
#invitado[0:1] --> imprime desde el cero hasta 1-1 = 0 desde 0 hasta 0
dia_invitado = int(invitado[:2])
mes_invitado = int(invitado[2:4])
agno_invitado = int(invitado[4:8])
nom_invitado = invitado[9:]
print(dia_invitado)
print(mes_invitado)
print(agno_invitado)
print("El dia de la semana que nacio es:",dia_de_la_semana(dia_invitado,mes_invitado,agno_invitado))
invitados = invitados[i+1:] #Permite procesar a la siguiente persona del String
print(nom_invitado)

print(invitados) #29022000,Silvia;01082000,Andrea
dia,mes,agno,nombre = fecha(invitados) #Llamamos la función para obtener los datos del string
print(dia)
print(mes)
print(agno)
print(nombre)
print("El dia de la semana que nacio es:",dia_de_la_semana(dia,mes,agno)) #Llamo la función para saber el dia de nacimiento
