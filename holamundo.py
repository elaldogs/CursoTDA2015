print "hola mundo" #este es un comentawrio

"""Este es un comentario de varias lineas,
que continua en esta linea"""

x=5
y=x
print x
print y 
print x+y
print str(x) # esta es una buena practica
print "El valor de x es: " + str(x)
if x>5:
    print "x es mayor que 5"
    print "quiero mas instrucciones"
else:
    print "x es menor o igual que 5"
    print "quiero mas instrucciones en el else"
print "El cuadrado de " + str(x) + " es " + str(x**2)
print "Tarea: Checar las otras operaciones aritmeticas (excepto sqrt)"
print "En python hay listas, conjuntos y tuplas"
lista = [1,2,3]
print "Tu lista tiene " + str(lista)
conjunto = {3,2,2}
print conjunto
print "Tu conjunto tiene " + repr(conjunto)
tupla = (3,2,1)
print "Tu tupla tiene " + str(tupla)
y=7
print "Los valores de x & y son: " + str(x) + " y " + str(y)
(x,y)=(y,x)
print "Los valores de x & y son: " + str(x) + " y " + str(y)
tuplaconunelemento=(5,)
print tuplaconunelemento
(x,y,w,z)=(x,y)+(5,5) # + concatena tuplas, listas
# esto no funciona:  conjunto= conjunto + {2,3,4}
print range(10)
for i in range(10):
    print "Esta es la ejecucion numero " + str(i) + " del ciclo"
for i in [3,5,7]:
    print "i vale " + str(i)
listademodulos = [x%2 for x in range(10)]
print listademodulos
print "Tarea: Jugar con list comprehension"
print range(0,10,1)
print range(1,10,1)
print range(1,10,5)
