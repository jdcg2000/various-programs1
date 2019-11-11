
cantidaddep = [0]
valort = [0]
valortent = [0]
cantidaddepent = [0]
cantidaddepsal = [0]
valortsal = [0]


def entradas():
    if len(cantidaddep) == 0:
        cantidaddep.append(e)
    elif len(valort) == 0:
        valort.append(f)
    else:
        g = cantidaddep[-1]
        cantidaddep.append(g+e)
        g1 = valort[-1]
        valort.append(g1+f)
        valortent.append(f)
        cantidaddep.append(e)
    print(cantidaddep)
    print(valort)
    print(valortent)
    print(cantidaddepent)
def salidas():
    if len(cantidaddep) == 0:
        print("No es posible realizar salidas porque aún no hay productos registrados")
    i = valort[-1]
    j = i- f
    valort.append(j)
    k = cantidaddep[-1]
    m = k - e
    cantidaddep.append(m)
    valortsal.append(f)
    cantidaddepsal.append(e)
    print(cantidaddep)
    print(valort)
    print(cantidaddepsal)   
    print(valortsal)



while True:
    
    print("1. Realizar una entrada")
    print("2. Realizar una salida")
    aa = input("Desea ingresar una entrada o una salida ")
    a = input("Ingrese el nombre del producto ")
    b = input("Ingrese el precio unitario del producto ")
    c = input("Ingrese la cantidad de productos ")
    d = int(b)
    e = int(c)
    f = d*e
    if aa == "1":
        entradas()
    elif aa == "2":
        salidas()
    else:
        print("Opción no valida.")
    
print(cantidaddep)
print(valort)
print(valortent)
print(cantidaddepent)
print(cantidaddepsal)
print(valortsal)
