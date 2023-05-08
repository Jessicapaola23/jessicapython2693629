num1=int(input("ingrese un número:"))
num2=int(input("ingrese otro número:"))
while num1==num2:
    print("los numeros ingresados son iguales. Por favor ingrese números diferentes.")
    num1=int(input("ingrese un número:"))
    num2=int(input("ingrese otro número:"))

if num1>num2:
    print(f"El número {num1} es mayor que el {num2}")

else:
    print(f"El número {num2} es mayor que el {num1}")


    


