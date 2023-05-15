import random
#ejemplo 1
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range (tam)] 
    return lista
def llenarLista(tam, rango):
    lista=[random.randrange(rango) for i in range (tam)] 
    return lista

def sumaLista(lista):
    suma1=sum(l1)
    suma2=sum(l2)

    if suma1 > suma2:
        print(f"la suma de la lista 1:{suma1} es mayor que la suma de la lista 2")
    else:
        suma1< suma2











        

    
    
    






l1=llenarLista(5,10)
l2=llenarLista(5,10)
print("lista 1:",l1,"la suma es:",sumaLista(l1))
print("lista 2:",l2,"la suma es:",sumaLista(l2))
print("la suma mas alta esta en la lista :",(l1))

