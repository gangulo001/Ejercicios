palabra1 = input('Digite palabra 1:')
palabra2 = input('Digite palabra 2:')
i = 0
resultado = ''
if len(palabra1) != len(palabra2):
    print('error')
else:
    while i < len(palabra1):
        resultado += palabra1[i] + palabra2[i]
        i += 1
    print(resultado)