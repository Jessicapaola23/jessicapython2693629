import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range (tam)] 
    return lista
    
l1=llenarLista(15,125)
print(l1)