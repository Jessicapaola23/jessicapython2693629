import random
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]
par=[tam for par in lista if tam**2==0]
impar=[tam for impar in lista if tam^2==0]
print(lista)

print(par)
print(impar)
#Llenar una lista por comprension basado en otra lista previamente llena con numeros aleatorios. Si el dato es par llene la lista con la raiz del numero pero si es impar llenelo con el numero elevado al cuadrado