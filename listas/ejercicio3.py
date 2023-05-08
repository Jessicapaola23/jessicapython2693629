import random
def fibonacci(n):
    a,b=0,1
    result=[]
    while len(str(a))<n:
        result.append(a)
        a,b=b,a+b
        return result
num=int(input("ingrese la cantidad de numeros que desea:"))
fibonacci_serie= fibonacci(num)
print(fibonacci_serie)