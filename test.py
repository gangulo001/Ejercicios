num = int(input('Digite un numero:\n'))
factorial = 1
if num < 0:
       print("Error")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
#    print("El factorial de ",num," es ",factorial)
print("El factorial de {num} es {factorial}")