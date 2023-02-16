# num = int(input('Digite un numero:\n'))
# factorial = 1
# if num < 0:
#        print("Error")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
# #    print("El factorial de ",num," es ",factorial)
# print("El factorial de {num} es {factorial}")

# def secuencia(texxt):
#        listaa = []
#        # for x in texxt:
#        #        listaa.append(x)
#        # listab = [x for x in listaa if x != ","]
#        # print(listaa)
#        # print(listab)

#        for texxt in secuencia:
#               print(texxt)

# secuencia("ttata")

secuencia = input("Digite una secuencia de numeros separados por coma: \n")

def listatupla(secuencia):
    mylist = secuencia.split()
    print("Resultado:\n", "Lista: ", mylist)
    mytuple = tuple(mylist)
    print("Tupla: ", mytuple)


listatupla(secuencia)

#   Prueba 1:
# 1
#   Prueba 2:
# 1,2,3,4
#   Prueba 3:
# 50,6,7000