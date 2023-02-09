import os
import modulo_arit
os.system('cls')
import datetime
now = datetime.datetime.now()
file = open("logfile.txt","a")
file.write(str(now) + " Programa abierto" + "\n")
file.close()

Salir = False

while not Salir:

    operacion = int(input("Digite el numero de operacion que desea realizar:\n\n 1 = Suma (cantidad ilimitada)\n 2 = Resta(2 numeros)\n 3 = Multiplicacion (cantidad ilimitada)\n 4 = Division (2 numeros)\n 5 = Factorial de un numero\n 6 = Potencia (2 numeros)\n 7 = Salir\n"))

    if operacion == 1:
        modulo_arit.list_sum()

        # num = int(input("Ingrese la cantidad de numeros que desea sumar: "))
        # numlist = []
        # for ncantidad in range(num):
        #     Numeros = int(input("Ingrese el numero a sumar: "))
            
        #     # if num != int():
        #     #     print("Numeros sin valor: resultado = null")
        #     # elif not numlist:
        #     #     print("Numeros sin valor: resultado = null")
        #     # else:
            
        #     numlist.append(Numeros)           
            
        #     # elif not numlist:
        #     # print("Numeros sin valor: resultado = null")        
        
        # resultado = sum(numlist)
        
        # # num1 = int(input("Primer digito"))
        # # num2 = int(input("Segundo digito"))
        
        # # import os
        # os.system('cls')
        # print("El resultado de la suma de",numlist,"es",resultado,"\n")
    
    elif operacion == 2:
        modulo_arit.resta()
        # num1 = int(input("Primer digito"))
        # num2 = int(input("Segundo digito"))
        # # import os
        # os.system('cls')
        # print("El resultado de la resta de",num1,"-",num2,"es",num1 - num2,"\n")
    
    
    elif operacion == 3:
        modulo_arit.mult_list()
        # num = int(input("Ingrese la cantidad de numeros que desea multiplicar: "))
        # numlist = []
        # for ncantidad in range(num):
        #     Numeros = int(input("Ingrese el numero a multipilicar: "))
        #     numlist.append(Numeros)        
        #     resultado = 1    
        # for numdelista in numlist:
        #     resultado = resultado * numdelista
        # num1 = int(input("Primer digito"))
        # num2 = int(input("Segundo digito"))
        # import os
        # os.system('cls')
        # print("El resultado de la multiplicacion de",numlist,"es",resultado,"\n")

    elif operacion == 4:
        modulo_arit.division()
        # num1 = int(input("Ingrese primer digito como divisor: "))
        # num2 = int(input("Ingrese segundo digito como dividendo: "))
        # resultado = num1 / num2
        # # import os
        # os.system('cls')
        # print("El resultado de la division de",num1,"/",num2,"es",resultado,"\n")

    elif operacion == 5:
        modulo_arit.factorial()
        # num = int(input("Ingrese numero entero mayor a 0: "))
        # if num <= 0:
        #     import os
        #     os.system('cls')
        #     print("Error... por favor ingrese un numero entero mayor a 0\n")
        # else:
        #     factorial = 1
        #     for i in range(1,num + 1):
        #         factorial = factorial * i
        #         import os
        #         os.system('cls')
        #         print("El factorial de",num,"es",factorial,"\n")
                
    elif operacion == 6:
        modulo_arit.potencia()
        # num1 = int(input("Ingrese el numero Base: "))
        # num2 = int(input("Ingrese el numero Exponente: "))
        # resultado = num1 ** num2
        # os.system('cls')
        # print("El resultado del numero",num1,"elevado a la potencia",num2,"es",resultado,"\n")

    elif operacion == 7:
        file = open("logfile.txt","a")
        file.write(str(now) + " Programa cerrado" + "\n")
        file.close()
        os.system('cls')
        print("Gracias por usar la calculadora\n")
        Salir = True
