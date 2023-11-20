def libro(pagi,num):
    if pagi>=num/2:
        print('Desde el final')
    else:
        print('Desde el inicio')

    if (num+2)%2==0:
        numDepares=(num+2)/2
    else:
        numDepares=(num+1)/2

    if pagi==numDepares/2:
        resultado=1
    elif pagi<numDepares/2:
        resultado=(numDepares/2)-pagi
        print(resultado/2)
    else:
        resultado=(pagi-(numDepares/2))
    
    print(resultado)
    
    




libro(6,2) #Debe dar 1