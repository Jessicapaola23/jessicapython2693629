num=int(input("ingrese un numero positivo:"))
n=int (input("ingrese el valor de n:"))

multiplos=0 
for i in range(1,num+1):
    if i%n==0:
        print(i)
        multiplos +=1
print(f"Hay {multiplos} multiplos de {n} en la serie")        