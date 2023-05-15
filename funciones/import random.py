import random
#ejemplo 1
def llenarLista(tam, rango):
    lista=[random.randrange(rango) for i in range (tam)] #se crea una funcion (llenarlista) para 
    return lista
def llenarLista(tam, rango):
    lista=[random.randrange(rango) for i in range (tam)] 
    return lista

def sumaLista(lista):
    sum=0
    for j in lista:
        sum+=j
    return sum
    
l2=llenarLista(10,15)
l1=llenarLista(10,15)
print("la lista 1 es:",l1)
print("la lista 2 es:",l2)
print("la suma es:",l1,l2)