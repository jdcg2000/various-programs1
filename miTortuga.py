

def cuadrado(t, size):#funcion que realiza el cuadrado con turtle
    for a in range(4):
        t.forward(size)
        t.left(90)
    

def circulo(t, radio):#funcion que realiza el circulo con turtle
    t.circle(radio)
    
def rectangulo(t, size1, size2):#funcion que realiza el rectagulo con turtle
    t.forward(size1)
    t.left(90)
    t.forward(size2)
    t.left(90)
    t.forward(size1)
    t.left(90)
    t.forward(size2)
    
def poligono(t, size, n):#funcion que realiza  un poligono al que el usuario le puede escoger la cantidad de lados con turtle
    for b in range(n):    
        t.forward(size)
        t.left(360/n)
        
def triangulo_equilatero(t, size):#funcion que realiza un triangulo equilatero con turtle
    for c in range(3):
        t.forward(size)
        t.left(120)
        
        
        
        

    
        
