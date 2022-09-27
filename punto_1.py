
# Función organzia los nombres
def qsort(lis):
    if not lis:
        return []
    return (qsort([x for x in lis[1:] if x <  lis[0]])
            + [lis[0]] +
            qsort([x for x in lis[1:] if x >= lis[0]]))
# Función principal
def names(stri):
    n = stri.split(",")
    order = qsort(n)
    return order

# Input por consola
print("Escriba los nombres de las personas separado por comas, sin espacios:")
name_lis = input()
print(names(name_lis))
