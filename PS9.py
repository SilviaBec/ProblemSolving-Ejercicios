#revisar bien el orden de los parametros porque tenia el num de segundas y lo 
#llamaba como si fuera pag, abajo al llamar la funcion igual , revisar que si
# pongo num, pag abajo ponga el valor de num, valor pag
def libro(num,pagi):
    if pagi>=num/2:
        print('Desde el final')
    else:
        print('Desde el inicio')

    if num%2 ==0:
        num=num+2
        numDepares=(num)/2
        mitadPares=numDepares/2
        


    else:
        num=num+1
        numDepares=num/2
        mitadPares=numDepares/2
        if pagi>mitadPares:
            resultado=((num-1)-pagi)/2
            if resultado%2!=0:
                print(resultado-1)
        elif pagi==mitadPares:
            resultado=1
            print(resultado)
        else:
            print('este')


    if pagi>mitadPares:
        resultado=((num-1)-pagi)/2
        
    elif pagi-mitadPares<0:
        resultado= numDepares-(numDepares-pagi)
    
    # elif numDepares-pagi<0:
    #     resultado=numDepares-pagi
    #     print(abs(resultado))

    



    

#libro(6,2) #Debe dar 1
libro(9,3) 
#Debe dar 2 CREO , de atras pa delante, pero no esta funcionando , probar en este caso hipotetico
#libro(8,2) #Debe dar 1
#8 7