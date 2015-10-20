lista1=range(1,4,1)
print lista1
lista2=[x for x in range(6) if x%2==1]
print lista2 
lista3=[(x,y) for x in lista1 for y in lista2]
print lista3
lista4=[(x,y) for x in lista1 for y in lista2 for z in lista1]
print lista4
lista5=[1,"perro",5.6,lista1]
print lista5
lista6=[lista1,lista2]
print lista6
print lista1[0]
print len(lista4) # len dice la cantidad de elementos de una lista
print lista4[len(lista4)-1]
print lista4[-1] # el indice -1 devuelve el ultimo elemento de una lista
x=5
y=6
print type(x+y)
lista7=[9,8,7,6]
print lista7
lista7.sort()
print lista7
lista7.sort(reverse=True)
print lista7
lista7.append(-1000)
print lista7
print lista7.pop()
print lista7
del(lista7[2])
print lista7
print lista3
print lista3[0:3]
lista8 = lista3[0:3:2] # slicing con saltos
print lista8 
# TAREA: buscar informacion sobre filter()
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
submatriz = [x[1:3] for x in matriz[1:3]]
print submatriz
print matriz[1][1]
