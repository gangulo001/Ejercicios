# Esta funcion fue utilizada en el ejercicio de la calculadora para dividir 2 numeros:

# def division():
    
#     num1 = int(input("Ingrese primer digito como divisor: "))
#     num2 = int(input("Ingrese segundo digito como dividendo: "))
#     resultado = num1 / num2
    
#     print("El resultado de la division de",num1,"/",num2,"es",resultado,"\n")




division_lambda = lambda num1, num2: num1 / num2

num1 = int(input("Ingrese primer digito como divisor: "))
num2 = int(input("Ingrese segundo digito como dividendo: "))

resultado = division_lambda(num1, num2)

print("El resultado de la division de",num1,"/",num2,"es",resultado,"\n")

#prueba1:
#num1 = 10
#num2 = 7
#resultado = 1.4285714285714286

#prueba2:
#num1 = 10
#num2 = 5
#resultado = 2

#prueba3:
#num1 = 7
#num2 = 10
#resultado = 0.7