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
            print(int(numDepares),int(mitadPares))
        else:
            num=num+1
            numDepares=num/2
            mitadPares=numDepares/2
            print(numDepares,mitadPares)

    if pagi-mitadPares==0:
        resultado=1
        print(resultado) #esto aca no imprime 
    elif pagi-mitadPares<0:
        resultado= numDepares-(numDepares-pagi)
        print(resultado)


    

#libro(6,2) #Debe dar 1
libro(8,2) #Debe dar 1