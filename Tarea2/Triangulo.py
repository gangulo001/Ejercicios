# el usuario ingresa un numero entero mayor a 0
# el numero es validado
# si el numero es igual a 0 o menor, da error
# mensaje de error: "Error... ingrese un numero entero mayor a 0"
# si el numero es un numero entero mayor a 0 se continua
# el numero digitado es guardado como variable
# el programa empieza a imprimirse desde el numero 1 consecutivamente hasta el numero digitado por el usuario
# al numero inicial se le pone el consecutivo a la par del mismo, hasta llegar al numero digitado


    # for column in range(1,num+1):
    #     while x <= num:
    #         x = x + 1
    #         print(x)  
    #     print(column,end=" ")
        #x=x+1

      #  int(column+1)
        
        # for column in range(1,row+1):
        #     row += column
    #     print(row,end="")
    # print()
   
    # while i <= num:
    #     for i in range(1,num):
    #         print(i,i+1)
    #     i += 1


    # for line in range(1,num+1):
    #     # line = count + 1
    #     line += num
    #     print(line,num)
    #     line + 1
    # print()


    # for row in range(1,num+1):
    #     for column in(1,row+1):
    #         print(column,end="")
    #     print()

# else:
#     for i in range(1,int(num)+1):

num = int(input("Ingrese un numero entero mayor a 0\n"))

if num <= 0:
    print("Error... Ingrese un numero entero mayor a 0")
elif num > 0:
    for row in range(1,num+1):
        print(row)
        row + 1
        for column in range(1,num+1):
            print(column,end="")
            column + 1 