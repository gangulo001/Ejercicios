# Esta funcion se utilizo para potencir un numero:

# def potencia():
    
#     num1 = int(input("Ingrese el numero Base: "))
#     num2 = int(input("Ingrese el numero Exponente: "))
#     resultado = num1 ** num2

#     print("El resultado del numero",num1,"elevado a la potencia",num2,"es",resultado,"\n")




potencia_lambda = lambda num1, num2: num1 ** num2

num1 = int(input("Ingrese el numero Base: "))
num2 = int(input("Ingrese el numero Exponente: "))

resultado = potencia_lambda(num1, num2)
print("El resultado del numero", num1, "elevado a la potencia", num2, "es", resultado, "\n")

#prueba1:
#num1 = 5
#num2 = 2
#resultado = 25

#pureba2:
#num1 = -3
#num2 = 3
#resultado = -27

#prueba3
#num1 = 2
#num2 = 5
#resultado = 32