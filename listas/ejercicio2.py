import random

tam=int(random.randint(10,15))
lista=[random.randrange(0,9) for i in range (tam)]
print(lista)

j=int(input("ingrese el numero que desea buscar:"))

if j in lista:
    print("el numero esta")
else:
    print("el numero no esta")

repetido=False
cont=0
posicion=0
for i in range(len(lista)):
    if lista[i] ==j:
       repetido=True
       cont +=1
       
if repetido:
    print(f"el {j} esta repetido {cont} veces")
else:
    print(f"el {j} no esta en la lista")

