"""Una función es un bloque de código con un nombre asociado, 
que recibe cero o más argumentos como entrada, sigue una secuencia de sentencias, 
la cuales ejecuta una operación deseada y devuelve un valor y/o realiza una tarea, 
este bloque puede ser llamados cuando se necesite."""

def hello(): #Función
    print("hello world")

hello() #Llamando a la función

#Ejemplo 2
def hello_person(name): #Función con parametro "name"
    print("hello "+ name) #Usamos el "+" para concatenar string

hello_person("jorge") #Llamando a la función

#Ejemplo 3

def hello_person2(name="Persona"): #Función con parametro "name" pero con person por defecto
    print("hello "+ name) #Usamos el "+" para concatenar string

hello_person2() #Llamando a la función sin ingresar parametro imprimire "persona" por defecto
hello_person2("seba") #Se le ingreso un parametro por lo tanto no considera el "persona"

def add(n1, n2): #Ingresamos 2 parametros
    return n1 + n2 #Sumamos los paramtros dados
print(add(10, 30)) #Imprimimos la suma de la operación

print(" ") #Salto de linea

#Función lambda
add = lambda n1, n2: n1 + n2 #Creamos la función en una sola linea definiendo parametros y la operación
print(add(50, 30)) #Imprimimos la suma de la operación
