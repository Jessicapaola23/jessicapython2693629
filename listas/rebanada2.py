
#llenar una lista con numeros aleatorios (reales con una decimal) que representem calificaciones de un curso. se evalua de 0 a 5.
#el curso puede tener entre 20 y 30 aprendices
#HALLAR
#1.saque listas nuevas para los aprobados y los reprobados (se aprueba con 3)
#2.genere listas nuevas por cada unidad. es decir los qie sacan de 0 a 1 son un grupo,los de 1 a 2 oro y asi sucesivamente
#3.diga cual es el promedio de los que apruebn y de los que desaprueban por separado 
import random


tam=random.randint(10,20)
lista_Calificaciones=[float(random.randrange(6)) for i in range(tam)]
print("la lista de calificaciones es",lista_Calificaciones)
listaDeAprobados=[x for x in lista_Calificaciones if x]
listaDeReprobados=[x for x in lista_Calificaciones if x+1]
print("la lista de aprobados es",listaDeAprobados)
print("la lista de reprobados es",listaDeReprobados)


#lista=[float(random.randrange(1.0,5.0)) for i in range(tam)]
#print(lista)

#lista_aprovados=0

#lista_desaprobados=0




#posicion=[]

#rebanada1=lista[len(lista)/2:-1]

#print(rebanada1)