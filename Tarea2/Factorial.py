# usuario pone un numero entero positivo
# validacion del numero para que sea valido
# si el numero es valido la operacion continua
# si el numero es invalido da un mensaje "por favor ingrese un numero positivo y entero"
# el numero ingresado debe ser multiplicado por la cantidad de numeros del 1 hasta el numero ingresado
# respuesta es el resultado de la ultima multiplicacion

# num = input('Ingrese un numero entero mayor a 0\n')
# i = 1
# type(num,int)


# if num < 0 :
#         print("Error... por favor ingrese un numero entero mayor a 0\n")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#        print("El factorial de ",num," es ",factorial)


# while i <= num :
#         i * num
#         i += 1
#         print("El factorial del [num] es [i]")


num = int(input('Ingrese un numero entero mayor a 0\n'))
factorial = 1
if num < 0:
       print("Error... por favor ingrese un numero entero mayor a 0\n")
       
else:
   for i in range(1,num + 1):
       factorial = factorial * i
print("El factorial de",num,"es",factorial)