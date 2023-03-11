# Esta funcion fue utilizada para calcular la factorizacion de un numero:

# def factorial():
   
#     num = int(input("Ingrese numero entero mayor a 0: "))
#     if num <= 0:
       
#         print("Error... por favor ingrese un numero entero mayor a 0\n")
#     else:
#         factorial = 1
#         for i in range(1,num + 1):
#             factorial = factorial * i
    
#     print("El factorial de",num,"es",factorial,"\n")



num = int(input("Ingrese numero entero mayor a 0: "))

if num <= 0:
    print("Error... por favor ingrese un numero entero mayor a 0\n")

else:
    factorial_lambda = lambda num: 1 if num == 0 else num * factorial_lambda(num-1)
    resultado = factorial_lambda(num)
    print("El factorial de",num,"es",resultado,"\n")

#prueba1:
#num = 5
#resultado = 120

#prueba2:
#num = 10
#resultado = 3628800

#prueba3:
#num = -3
#resultado = Error... por favor ingrese un numero entero mayor a 0