# el usuario debe ingresar 2 palabras del mismo largo (misma cantidad de letras)
# ambas palabras deben ser validadas
# si no cumplen con lo solicitado da error: "Error... por favor ingrese 2 palabras con la misma contidad de letras"
# si cumple con lo solicitado se continua
# las letras de cada palabra deben ser contadas y luego intercaladas
# respuesta de nueva palabra creada


print("Ingrese 2 palabras con la misma cantidad de letras")
data1 = str(input("Primera palabra: "))
data2 = str(input("Segunda palabra: "))

if len(data1) != len(data2):
    print("Error... por favor ingrese 2 palabras con la misma contidad de letras")
else:
    print(data1[0:-1:2])
    newdata1 = (data1[::-1])
    print(newdata1)
    
    # print([x for x in range(newdata1[0:-1:2])])
    # i = (newdata1[0:-1:2])
    # print(i)
    # newdata11 = (i[::-1])
    # print(newdata11[0:-1:2])
    # for character in data1:
        # for i in range(1,int(len(data1)) + 1):
        #     print(data1,end = data2)
        #     i + 1
#print(len(data1),len(data2))

