from numpy import *
import matplotlib.pyplot as plt

y = str(input("Ingrese la función f(x)= "))
def f(x):
    return round(eval(y),2)

puntosx=[]
puntosy=[]
comx=[]
comy=[]
listxtrap=[]
listytrap=[]
areadiv=[]
areatotal=[]


x1 =int(input("Ingrese el valor de x del primer punto ")) #Pregunta al usuario el primer punto en "x" para delimitar el dominio de la función
x2 =int(input("Ingrese el valor de x sel segundo punto ")) #Pregunta al usuario el segundo punton de "x" para delimitar el dominio de la función
div =int(input("En cuántos trapecios quiere dividir el área a medir ")) #El usuario puede introducir la cantidad de trapecios para dividir el área debajo de la función


for a in range(x2): #Ciclo for para que el programa guarde en la lista "puntosx" los valores que se van a incluir en el dominio de la gráfica a medir.
    fx=x1+a
    puntosx.append(fx)
print(puntosx)

for b in range(x2): #Ciclo for para que el programa guarde en la lista "puntosy" los valores que se van a incluir en el campo de la gráfica a medir.
    fxy=f(x1+b)
    puntosy.append(fxy)
print(puntosy)

for c in range(x1-5, x2+5): #Ciclo for para que el programa guarde en la lista "comx" los valores en "x" que van a seguir la funcion que no se medira
    fd=0+c
    comx.append(fd)
    
for d in range(x1-5, x2+5): #Ciclo for para que el programa guarde en la lista "comy" los valores de "y" que van a seguir la función que no se medira
    fp=f(0+d)
    comy.append(fp)
    
for e in range(div+1): #Ciclo for para que el programa guarde en la lista "listtrapx" los valores que determinan laa distancia en "x" entre los trapecios
    trapx=(((x2-x1)/div)*e)+x1
    listxtrap.append(trapx)
print(listxtrap)

for f in range(div+1):
    lolo=int(((((x2-x1)/div)*f)))
    trapy=puntosy[lolo]
    listytrap.append(trapy) 
print(listytrap)

for g in range(div):
    area=((listytrap[g]+listytrap[g+1])/2)*(listytrap[g+1]-listxtrap[g])
    areadiv.append(area)
print(areadiv)

sum=0
for h in range(0,len(areadiv)):
    sum=sum+areadiv[h]
print("Su área total es",sum)

plt.fill_between(puntosx,puntosy)
plt.scatter(puntosx,puntosy,) 
plt.plot(puntosx,puntosy,"r")
plt.plot(comx,comy)
plt.show()
   