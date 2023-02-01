num = input('Ingrese un numero entero mayor a 0\n')
x = 0

for x in range(1, int(num)+1):
    if x % 3 == 0 and x % 5 == 0: print('FizzBuzz')
    elif x % 3 == 0: print('Fizz')
    elif x % 5 == 0: print('Buzz')
    else: print(x)
