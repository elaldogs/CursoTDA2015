import numpy as np

matriz1=np.zeros([3,3])     # matriz 3x3 de ceros
print matriz1
matriz2=np.zeros([4,2])     # matriz 4x2 de ceros
print matriz2
matriz3=np.ones([3,3])      # matriz 3x3 de unos
print matriz3
matriz4=np.empty([4,4])     # matriz 4x4 sin inicializar
print matriz4
lista=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print type(lista) 
matriz5=np.asarray(lista)
print type(matriz5)
print matriz5
vector=np.reshape(matriz5, [1,16])
print vector
print len(matriz5)
lista1=matriz5.tolist()
print lista1
print type(lista1)
matriz6 = np.dot(matriz5,matriz5)
print matriz6
print np.dot(vector,vector.T)   # transponemos el segundo vector para que las dimensiones cuadren
print np.inner(2,matriz6)       # multiplica por escalar
print np.inner(vector,vector)   # esto es el producto interno de vectores
print np.inner(matriz5,matriz5) # ??? Tarea: determinar que hizo
print matriz5.T                 # arreglo.T es la transpuesta de arreglo
# TAREA: Adentrarse mas en numpy (inversos de matrices, rango, etc.)

