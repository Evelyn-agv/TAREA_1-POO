class EstructuraCiclicas:     
    def __init__(self):
        pass
    
    """Estructuras FOR"""
    def estCic1(self):                        #EJERCICIO 11
        i=1
        suma=0
        for i in range(100):
            suma= suma+i*i
            i+=1
        print("La suma de los 100 números es: {}" .format(suma))
    
    
    """Estructuras WHILE"""
    def estCic2(self):    #BUCLE CONTROLADO POR CONTADOR      #EJERCICIO 12
        i=1
        while i<=100:
            print("Presentación de los números: {}" .format(i))
            i+=1
        return i
    

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
    

    def estCic4(self):    #BUCLE CONTROLADO POR CONDICIÓN         #EJERCICIO 14
        sum=0
        prod=1
        num= int(input("Ingrese un número: "))
        while num!=-1:
            sum= sum+num
            prod= prod*num
            print("El total de la suma es: {}" .format(sum))
            print("El total del producto es: {}" .format(prod))
            num= int(input("Ingrese un número: "))
    

    def estCic5(self):    #BUCLE CONTROLADO POR BANDERAS O INTERRUPTORES          #EJERCICIO 15
        primo= True
        divisor=2
        num= int(input("Ingrese un número: "))
        while divisor<num and primo==True:
            res= num%divisor
            if res==0:
                primo= False
            divisor+=1
        if primo== True:
            print("El número {} es primo" .format(num))
        else:
            print("El número {} no es primo" .format(num))
    
    
    """Estructuras REPEAT"""
    def estCic6(self):                          #EJERCICIO 16
        I=1
        serie=0
        num= int(input("Ingrese un número: "))
        band=True
        while band:
            if band ==True:
                serie= serie+(1/I)
                band= False
            else:
                serie= serie-(1/I)
                band= True
            I+=1
            if I>num:
                break
            print("El resultado de la serie es: {}" .format(serie))
    
    
    """Bucles anidados"""
    def estCic7(self):                         #EJERCICIO 17
        num= int(input("Ingrese un número: "))
        fact=1
        for i in range(1, num+1):
            fact*=i
        print("El factorial del número {} es: {}" .format(num, fact))

clase1= EstructuraCiclicas()
clase1.estCic1()
clase1.estCic2()
clase1.estCic3()
clase1.estCic4()
clase1.estCic5()
clase1.estCic6()
clase1.estCic7()