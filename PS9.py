def libro(pagi,num):
    if pagi>=num/2:
        print('Desde el final')
    else:
        print('Desde el inicio')

    if (num+2)%2==0:
        numDepares=(num+2)/2
        print((num+2),(num+2)/2)
    else:
        numDepares=(num+1)/2
        print((num+1),(num+2)/2)
    if pagi==numDepares/2:
        resultado=1
        print('1')
    elif pagi<numDepares/2:
        resultado=(numDepares/2)-pagi
        print(resultado/2)
        print('2')
    else:
        resultado=(pagi-numDepares)
        print('3')
    
    print((resultado/2)-1)
    
    




#libro(6,2) #Debe dar 1
libro(9,2) #Debe dar 1