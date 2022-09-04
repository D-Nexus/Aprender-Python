
"Ejercicio 1"

s = 0

for n in range(1,10):
    if n % 7 == 0:
        break
    s += n

print(s)

"Ejercicio 2"

a = 0

for n in range(1,10):
    if n % 2 == 0:
        continue
    a += n

print(a)

"Ejercicio 3"

b = 0

for n in range(1,10):
    if n % 11 == 0:
        break
    b += n
else:
    b += 10

print(b)

"Ejercicio 4"

c = 0

for n in range(1,10):

    if n % 2 == 0:
        pass
    c += n

print(c)

"Ejercicio 5"

d = 0

for n in range(1,10):
    if n % 2 != 0:
        continue
    d += n
else:
    d += 5

print(d)