listadep = []
listainven = []
loloprod = []
lolo = []
def buscar(codigo):
    posicion = len(listadep)
    return posicion

def buscarnombre(codigo): #permite buscar el producto por nombre
    posicion = len(listadep)
    if posicion == 0:
        nombre = " "
    else:
        for loloprod in listadep:
            if loloprod[0] == codigo:
                nombre = loloprod[1]
            else:
                nombre = " "
    return nombre

def buscarproducto(codigo):# permite obtener la informacion del producto a buscar
    producto = []
    for loloprod in listadep:
        if loloprod[0] == codigo:
            producto.append(loloprod[0])
            producto.append(loloprod[1])
            producto.append(loloprod[2])
            producto.append(loloprod[3])
            producto.append(loloprod[4])
    return producto

def buscarproducto2(codigo):# le muestra los datos obtenidos con la funcion buscarproducto al usuario
    producto = []
    for producto in listadep:
        if producto [0] == codigo:
            print("Codigo: {0}".format(producto[0]))
            print("Nombre: {0}".format(producto[1]))
            print("Unidades Disponibles: {0}".format(producto[2]))
            print("Costo promedio: ".format(producto[3]))
            print("Total: {0}".format(producto[4]))
            
    
def actualizarsaldo(codigo, tipomov, cantidad, total):# Permite actualizar la informacion del inventario de acuerdo al tipo de moviiento ingreso o salida
    producto = []
    for loloprod in listadep:
        if loloprod[0] == codigo:
            listadep.remove(loloprod)
            cantidadt = float(loloprod[2])
            totalt = float(loloprod[4])
            if tipomov == "I":
                cantidadt = cantidadt + float(cantidad)
                totalt = totalt + float(total)
                print("I", cantidadt)
                print("I", totalt)
            else:
                cantidadt = cantidadt -float(cantidad)
                totalt = totalt - float(total)
                print("S", cantidadt)
                print("S",totalt)
            if cantidadt == 0:
                costo = 0
            else:
                costo = totalt/cantidadt
            producto.append(loloprod[0])
            producto.append(loloprod[1])
            producto.append(cantidadt)
            producto.append(costo)
            producto.append(totalt)
            listadep.append(loloprod)
    
def ingreso():# permite realizar el ingreso de un producto al inventario
    inventario = []
    print(" ")
    print("////////  INGRESO DE PRODUCTO ////////")
    codigo = input("Ingrese el codigo del producto: ")
    nombre = buscarnombre(codigo)
    if nombre == " ":
        nombre = input("Ingrese el nombre del producto: ")
    else:
        nombre = buscarnombre(codigo)
        print("Nombre del producto: {}".format(nombre))
    cantidad = input("Ingrese la cantidad de productos: ")
    precio = input("Ingrese el precio del producto: ")
    total = float(cantidad * precio)
    orden = input("Ingrese el No. de orden de compra: ")
    if buscar(codigo) == 0:
        loloprod.append(codigo)
        loloprod.append(nombre)
        loloprod.append(cantidad)
        loloprod.append(precio)
        loloprod.append(total)
        listadep.append(loloprod)
    else:
        actualizarsaldo(codigo, "I", cantidad, total)
    inventario.append("I")
    inventario.append(codigo)
    inventario.append(nombre)
    inventario.append(cantidad)
    inventario.append(precio)
    inventario.append(total)
    inventario.append(orden)
    listainven.append(inventario)
    print(" ")
    
def salida():# permite realizar la salida de un producto al inventario
    inventario = []
    print(" ")
    print("//////// SALIDA DE PRODUCTO ////////")
    codigo = input("Ingrese el codigo del producto: ")
    vector = buscarproducto(codigo)
    if len(vector) >0:
        print("Nombre del producto: {0}".format(vector[1]))
        print("Costo del producto: {0}".format(vector[3] )
        cantidad = float(input("Ingrese la cantidad a egresar "))
        total = float(vector[3] * cantidad)
        orden =input("Ingrese el No de factura: ")
        inventario.append("S")
        inventario.append(codigo)
        inventario.append(vector[1])
        inventario.append(cantidad)
        inventario.append(float(vector[3]))
        inventario.append(total)
        inventario.append(orden)
        actualizarsaldo(codigo,"E",cantidad,total)
        listaninven.append(inventario)
        print(" ")
    else:
        print("¡El producto no existe!")
        

def inventario():
    inventario = []
    producto = []
    print(" ")
    print("//////// INVENTARIO DE PRODUCTO ////////")
    print(" ")
    print(listainven)
    
    
while True:# emula el meu principal de la aplicacion
    print("SISTEMA DE INVENTARIO")
    print(" ")
    print("//////// Menú Principal ////////")
    print("0. SALIR")
    print("1. INGRESO DE PRODUCTO")
    print("2. SALIDA DE PRODUCTO")
    print("3. INVENTARIO")
    print("4. BUSQUEDA DE PRODUCTO")
    opcion=input("Digitar una Opción: ")
    if opcion=="0":
        break
    elif opcion=="1":
        ingreso()
    elif opcion=="2":
        salida()
    elif opcion=="3":
        inventario()
    elif opcion=="4":
        print(" ")
        print("//////// BUSQUEDA DE PRODUCTO ////////")
        Codigo=input("Ingrese el Código del Producto: ")
        BuscarProducto2(Codigo)
    else:
        print("Opción no válida")