def mifuncion(parametro=None):
    """Esta es la primera funcion que hago"""
    print parametro

def cuadrado(x):
    """Esta funcion recibe un valor x y devuelve su
    cuadrado"""
    valor_de_retorno=x**2
    return valor_de_retorno

def raizycuadrado(x):
    """Esta funcion recibe x y devuelve su raiz cuadrada
    y su cuadrado, en ese orden"""
    return (x**(1.0/2.0),x**2)

def imprimenombre(nombre="Juan",apellido="Perez"):
    print nombre + " " + apellido

def potencia(x,n=1.0):
    return x**n

"""
def potencia2(x=1,n):
    return x**n

da un error de interpretacion
"""
if __name__=="__main__":
    mifuncion("lo que sea")
    print cuadrado(5)
    (r3,c3)=raizycuadrado(3)
    print "la raiz de 3 es " + str(r3)
    print "el cuadrado de 3 es " + str(c3)
    imprimenombre("Cristhian","Hidber")
    imprimenombre()
    imprimenombre(apellido="Hidber")
    imprimenombre(apellido="Hidber", nombre="Cristhian")
    imprimenombre(apellido="Hidber", nombre="Cristhian")
    print potencia(5)
    print potencia(5,2.0)
    lista1=range(1,11)
    lista2=[cuadrado(x) for x in lista1]
    print lista2
    print (lambda x: x**2)(3)   #lambda define funciones sin nombre
    lista3=[(lambda x: x**2)(x) for x in lista1]    #la funcion sin nombre juega el papel de
                                                    #la funcion cuadrado
    print lista3
    # TAREA: investigar el funcionamiento de filter, map, zip