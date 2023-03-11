# Esta funcion fue utilizada en la calculadora para calcular la resta de 2 numeros:

# def resta():
    
#     num1 = int(input("Primer digito: "))
#     num2 = int(input("Segundo digito: "))

#     print("El resultado de la resta de",num1,"-",num2,"es",num1 - num2,"\n")

# Nueva solucion usando lambda:

resta_lambda = lambda num1, num2: num1 - num2

num1 = int(input("Primer digito: "))
num2 = int(input("Segundo digito: "))

resultado = resta_lambda(num1, num2)

print("El resultado de la resta de", num1, "y", num2, "es", resultado)

#prueba1:
#num1 = 5
#num2 = 2
#resultado = 3

#prueba2:
#num1 = 20
#num2 = 10
#resultado = 10

#prueba2:
#num1 = 20
#num2 = 10
#resultado = -10

