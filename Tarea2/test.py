
# print(2**3 + (5 + 6)**(1 + 1))

# a = [1, 2, 3, 4, 5]
# print(len(a))

# listtest = [99, 999, 9999, 0]

# print(max(listtest))

# a = [1, 3, 5] 

# a = tuple(a) 
# a[1] = 2 

# print(a)

# class tester:

#     def __init__(self, id):

#         self.id = str(id)

#         id="404"

 

# temp = tester(200)

# print(temp.id)

# x = 'abcd'

# for i in range(len(x)):

#     print(i)






# def list_sum():
    
#     num = int(input("Ingrese la cantidad de numeros que desea sumar: "))
#     numlist = []

#     for ncantidad in range(num):
#         Numeros = int(input("Ingrese el numero a sumar: "))
#         numlist.append(Numeros)  

#     resultado = sum(numlist)

#     print("El resultado de la suma de",numlist,"es",resultado,"\n")



# def resta():
    
#     num1 = int(input("Primer digito: "))
#     num2 = int(input("Segundo digito: "))

#     print("El resultado de la resta de",num1,"-",num2,"es",num1 - num2,"\n")

resta_lambda = lambda num1, num2: num1 - num2

num1 = int(input("Primer digito: "))
num2 = int(input("Segundo digito: "))

resultado = resta_lambda(num1, num2)

print("El resultado de la resta de", num1, "y", num2, "es", resultado)


# def mult_list():
    
#     num = int(input("Ingrese la cantidad de numeros que desea multiplicar: "))
#     numlist = []

#     for ncantidad in range(num):
#         Numeros = int(input("Ingrese el numero a multipilicar: "))
#         numlist.append(Numeros)        
#         resultado = 1   

#     for numdelista in numlist:
#         resultado = resultado * numdelista
   
#     print("El resultado de la multiplicacion de",numlist,"es",resultado,"\n")





#*****************************************************************************************************************************

# def division():
    
#     num1 = int(input("Ingrese primer digito como divisor: "))
#     num2 = int(input("Ingrese segundo digito como dividendo: "))
#     resultado = num1 / num2
    
#     print("El resultado de la division de",num1,"/",num2,"es",resultado,"\n")




# division_lambda = lambda num1, num2: num1 / num2

# num1 = int(input("Ingrese primer digito como divisor: "))
# num2 = int(input("Ingrese segundo digito como dividendo: "))

# resultado = division_lambda(num1, num2)

# print("El resultado de la division de",num1,"/",num2,"es",resultado,"\n")








#*********************************************************************************************************************************

# def factorial():
   
#     num = int(input("Ingrese numero entero mayor a 0: "))
#     if num <= 0:
       
#         print("Error... por favor ingrese un numero entero mayor a 0\n")
#     else:
#         factorial = 1
#         for i in range(1,num + 1):
#             factorial = factorial * i
    
#     print("El factorial de",num,"es",factorial,"\n")



# num = int(input("Ingrese numero entero mayor a 0: "))

# if num <= 0:
#     print("Error... por favor ingrese un numero entero mayor a 0\n")

# else:
#     factorial_lambda = lambda num: 1 if num == 0 else num * factorial_lambda(num-1)
#     resultado = factorial_lambda(num)
#     print("El factorial de",num,"es",resultado,"\n")


#**********************************************************************************************************************

# def potencia():
    
#     num1 = int(input("Ingrese el numero Base: "))
#     num2 = int(input("Ingrese el numero Exponente: "))
#     resultado = num1 ** num2

#     print("El resultado del numero",num1,"elevado a la potencia",num2,"es",resultado,"\n")




# potencia_lambda = lambda num1, num2: num1 ** num2

# num1 = int(input("Ingrese el numero Base: "))
# num2 = int(input("Ingrese el numero Exponente: "))

# resultado = potencia_lambda(num1, num2)
# print("El resultado del numero", num1, "elevado a la potencia", num2, "es", resultado, "\n")
