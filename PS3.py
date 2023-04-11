

def birthday(lista, dia, mes):

    rta=0
    # acum2=0
    # if suma<d:
    for x in range(0,len(lista)): # i= 0 1 2 3 4 
        if sum(lista[x:x+mes]) ==dia and len(lista[x:x+mes])==mes:
            rta=rta+1
    print(rta)
                    # suma = suma +s[y]
                    # if suma== d:
                    #     acum=acum+1
                
                            
            # for y in range(s[i,m]):
    #             suma = suma +s[y]
    #             if suma==d:
    #                 acum=acum+1
    #                 print(acum)
            
        
    # else:
    #     print(suma)
        



        
birthday([2,2,1,3,2],4,2)
#[1,2,1,3,2],3,2
# ([4],4,1)
#([1,1,1,1,1,1],3,2)