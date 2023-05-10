import random
#ejemplo 1
def llenarLista(tam, rango):
    lista=[random.randrange(rango) for i in range (tam)] #se crea una funcion (llenarlista) para 
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista (lista)/len(lista) #se utiliza para sacar el promedio de una lista y hacer la divicion 

def mayor(lista):
    mayor=max(lista)
    return mayor

def menor(lista):
    menor=min(lista)
    return menor 

def acendente(lista):
    for l1 in range(lista):
        for l2 in range(l1>l2,lista):
            return acendente
    
    

    
l2=llenarLista(10,15)
l1=llenarLista(5,15)
print("lista:",l1)
print("suma:",sumaLista(l1))
print("el promedio es:",round(promedioLista(l1),1)) #round se utiliza para sacar el promedio con solo dos numeros en decimal
print("el numero mayor:",mayor(l1))
print("el numero menor:",menor(l1))
print("el numero acendente es:",(l1>l2))


