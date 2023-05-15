import random
#ejemplo 1
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def numMayor(lista):
    mayor=0
    for a in lista:
        if a > mayor:
            mayor=a
    return mayor

def numMenor(lista):
    menor=100000
    for x in lista:
        if menor > x:
            menor=x
    return menor

def ordenAscendente(lista):                                                                                 
    f=len(lista)
    for j in range(f-1):
        for d in range(j+1,f):
            if lista[j]>lista[d]:
                lista[j],lista[d]=lista[d],lista[j]
    return lista

def ordenDescendente(lista):                                                                                 
    f=len(lista)
    for j in range(f-1):
        for d in range(j+1,f):
            if lista[j]<lista[d]:
                lista[j],lista[d]=lista[d],lista[j]
    return lista
def encontrarMediana(lista):
    listaOrdenada=(lista)
    longitud=len(listaOrdenada)
    if longitud %2==0:
        ind1=longitud//2
        ind2=ind1-1
        mediana=(listaOrdenada[ind1])
    else:
        ind1=longitud//2
        mediana=listaOrdenada[ind2]
        return mediana

        
l1=llenarLista(5,10)
print(l1)
print("La suma de los valores es la lista es:",sumaLista(l1))
print("El promedio de la lista es:",round(promedioLista(l1), 2))
print("El numero mayor es:",numMayor(l1))
print("El numero menor es:",numMenor(l1))
print("Orden Ascendente:",ordenAscendente(l1))
print("Orden Descendente:",ordenDescendente(l1))
print("La mediana es:",ordenDescendente(l1))