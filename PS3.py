# a=[1,1,1,1,1,1]
# dia=3
# acumulado=0

# for x in a:
#         while acumulado<dia:
#             acumulado=acumulado+x
#             print(acumulado)



def birthday(s, d, m):
    suma=s[0]
    acum=0
    acum2=0
    if suma<d:
        for i in range(0,len(s)): # i= 0 1 2 3 4 
            for y in s[i:i+m]:
                    suma = suma +s[y]
                    if suma== d:
                            acum=acum+1
                            print(s[i:i+m])
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