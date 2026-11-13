numeros = []
for i in range(1,11):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
    while True:

        print("======== MENU DE BIENVENIDA ====== ")
        print("1.- MOSTRAR MENOR A MAYOR")
        print("2.- MOSTRAR MAYOR A MENOR")
        print("3.- SALIR") 
        print("======================================")  
        opcion = int(input("Ingresa una opción porfavor:  "))
        match opcion:
            case 1:
                lista_normal = sorted(numeros)
                print(lista_normal)
            case 2:

                lista_numeros_alreves = numeros(sorted(reverse=True))

                print(lista_numeros_alreves)    
            case 3:
                salir = int(input("Desea salir? 1.- Si 2.- No"))
                if salir == 1:
                    print("Saliendo......")
                    break
                else:
                    print("Sigamos.....")
                    continue
                