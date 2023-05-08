import random
#
n=int(input("ingrese la cantidad de numeros de la lista:"))
lista=[]
anterior=0

for i in range(n):
    siguiente_decena=(anterior//10+1)*10
    num=random.randint(anterior,siguiente_decena-1)
    lista.append(num)
    anterior=num

    print(f"la lista generada es ¨{lista}")
    

