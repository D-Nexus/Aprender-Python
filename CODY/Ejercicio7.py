#Condicionales
#Formar Triangulos
a = float(input())
b = float(input())
c = float(input())

if a == b and b == c:
    print("Triangulo equilatero")
elif a > b and b > c and (a+b) > c and (a+c) > b and (b+c) > a:
    print("Triangulo escaleno")
elif (a+b) > c and (a+c) > b and (b+c) > a and ((a == c) or (b == c) or (a == b)):
    print("Triangulo isosceles")
elif a < b and b > c and (a+b) > c and (a+c) > b and (b+c) > a:
    print("Triangulo escaleno rectangulo")
else:
    print("No es triangulo")
    