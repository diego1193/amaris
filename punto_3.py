# Input por consola
print("Escriba la primera cadena")
x = input()
print("Escriba la degunda cadena")
y = input()

c = x
z = 0
a = False
while (a != True):
    len_x = len(x)
    len_y = len(y)

    if len_x == len_y:
        s1 = x[0]
        s2 = x[len_x-1]
        x = s2 + x[0:len_x-1]
        if x == y:
            print(f"Las cadenas {c} y {y} son amigas")
            a =True
        elif z > len_x:
            print(f"Las cadenas {c} y {y} no son amigas")
            a = True  
        z += 1
    else:
        print(f"Las cadenas {c} y {y} no son amigas")
        a = True
