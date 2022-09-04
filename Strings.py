"""Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. 
Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles."""


myStr = "hello world"

print(dir(myStr)) #Con "dir" podemos averiguar que se puede hacer con ese tipo de dato

print("My name is " + myStr) #Para sumar 2 string usamos un "+"
print("I am", 20) #Para sumar un string y un numero usamos "," 
print(f"My name is {myStr}") #La f le dice al string que lo que esta entre {} debe ser una variable
print("My name is {0}".format(myStr)) #le decimos que en el valor 0 debe ir la variable myStr

