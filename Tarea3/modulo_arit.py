import os

def list_sum():
    num = int(input("Ingrese la cantidad de numeros que desea sumar: "))
    numlist = []
    for ncantidad in range(num):
        Numeros = int(input("Ingrese el numero a sumar: "))
        numlist.append(Numeros)           
    resultado = sum(numlist)
    os.system('cls')
    print("El resultado de la suma de",numlist,"es",resultado,"\n")

def resta():
    num1 = int(input("Primer digito: "))
    num2 = int(input("Segundo digito: "))
    os.system('cls')
    print("El resultado de la resta de",num1,"-",num2,"es",num1 - num2,"\n")

def mult_list():
    num = int(input("Ingrese la cantidad de numeros que desea multiplicar: "))
    numlist = []
    for ncantidad in range(num):
        Numeros = int(input("Ingrese el numero a multipilicar: "))
        numlist.append(Numeros)        
        resultado = 1    
    for numdelista in numlist:
        resultado = resultado * numdelista
    os.system('cls')
    print("El resultado de la multiplicacion de",numlist,"es",resultado,"\n")

def division():
    num1 = int(input("Ingrese primer digito como divisor: "))
    num2 = int(input("Ingrese segundo digito como dividendo: "))
    resultado = num1 / num2
    os.system('cls')
    print("El resultado de la division de",num1,"/",num2,"es",resultado,"\n")

def factorial():
    num = int(input("Ingrese numero entero mayor a 0: "))
    if num <= 0:
        os.system('cls')
        print("Error... por favor ingrese un numero entero mayor a 0\n")
    else:
        factorial = 1
        for i in range(1,num + 1):
            factorial = factorial * i
            os.system('cls')
            print("El factorial de",num,"es",factorial,"\n")

def potencia():
    num1 = int(input("Ingrese el numero Base: "))
    num2 = int(input("Ingrese el numero Exponente: "))
    resultado = num1 ** num2
    os.system('cls')
    print("El resultado del numero",num1,"elevado a la potencia",num2,"es",resultado,"\n")