class EstructuraCiclicas:     
    def __init__(self):
        pass

    def estCic3(self):    #BUCLE CONTROLADO POR CONDICIÓN     #EJERCICIO 13
        sum=0
        prod=1
        print("Desea continuar [S/N]:  ")
        resp= input().capitalize()
        while resp == "S":
            num= int(input("Ingrese un número: "))
            sum= sum+num
            prod= prod*num
            print("El total de la suma es: {}" .format(sum))
            print("El total del producto es: {}" .format(prod))
            print("Desea continuar [S/N]:  ")
            resp=input().capitalize()

clase1= EstructuraCiclicas()
clase1.estCic3()