import os
import datetime
now = datetime.datetime.now()

def list_sum():
    file = open("logfile.txt","a")
    num = int(input("Ingrese la cantidad de numeros que desea sumar: "))
    numlist = []
    for ncantidad in range(num):
        Numeros = int(input("Ingrese el numero a sumar: "))
        numlist.append(Numeros)           
    resultado = sum(numlist)
    file.write(str(now) + " Operacion Suma: " + "El resultado de la suma de " + str(numlist) + " es " + str(resultado) + "\n")
    file.close()
    os.system('cls')
    print("El resultado de la suma de",numlist,"es",resultado,"\n")

def resta():
    file = open("logfile.txt","a")
    num1 = int(input("Primer digito: "))
    num2 = int(input("Segundo digito: "))
    file.write(str(now) + " Operacion Resta: " + "El resultado de la resta de " + str(num1) + " - " + str(num2) + " es " + str(num1-num2) + "\n")
    file.close()
    os.system('cls')
    print("El resultado de la resta de",num1,"-",num2,"es",num1 - num2,"\n")

def mult_list():
    file = open("logfile.txt","a")
    num = int(input("Ingrese la cantidad de numeros que desea multiplicar: "))
    numlist = []
    for ncantidad in range(num):
        Numeros = int(input("Ingrese el numero a multipilicar: "))
        numlist.append(Numeros)        
        resultado = 1    
    for numdelista in numlist:
        resultado = resultado * numdelista
    file.write(str(now) + " Operacion Multiplicacion: " + "El resultado de la multiplicacion de " + str(numlist) + " es " + str(resultado) + "\n")
    file.close()
    os.system('cls')
    print("El resultado de la multiplicacion de",numlist,"es",resultado,"\n")

def division():
    file = open("logfile.txt","a")
    num1 = int(input("Ingrese primer digito como divisor: "))
    num2 = int(input("Ingrese segundo digito como dividendo: "))
    resultado = num1 / num2
    file.write(str(now) + " Operacion Division: " + "El resultado de la division de " + str(num1) + " / " + str(num2) + " es " + str(resultado) + "\n")
    file.close()
    os.system('cls')
    print("El resultado de la division de",num1,"/",num2,"es",resultado,"\n")

def factorial():
    file = open("logfile.txt","a")
    num = int(input("Ingrese numero entero mayor a 0: "))
    if num <= 0:
        os.system('cls')
        print("Error... por favor ingrese un numero entero mayor a 0\n")
    else:
        factorial = 1
        for i in range(1,num + 1):
            factorial = factorial * i
    file.write(str(now) + " Operacion Factorial: " + "El factorial de " + str(num) + " es " + str(factorial) + "\n")
    file.close()
    os.system('cls')
    print("El factorial de",num,"es",factorial,"\n")

def potencia():
    file = open("logfile.txt","a")
    num1 = int(input("Ingrese el numero Base: "))
    num2 = int(input("Ingrese el numero Exponente: "))
    resultado = num1 ** num2
    file.write(str(now) + " Operacion Potencia: " + "El resultado del numero " + str(num1) + " elevado a la potencia " + str(num2) + " es " + str(resultado) + "\n")
    file.close()
    os.system('cls')
    print("El resultado del numero",num1,"elevado a la potencia",num2,"es",resultado,"\n")