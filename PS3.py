# a=[1,1,1,1,1,1]
# dia=3
# acumulado=0

# for x in a:
#         while acumulado<dia:
#             acumulado=acumulado+x
#             print(acumulado)



def birthday(s, d, m):
    suma=s[0]
    if suma<d:
        for x in range(1,len(s)):
            while suma<d:
                suma = suma +s[x]
                print(suma)
                print(s[x])
        #No se si es por donde puse el print pero deberia parar cuando la suma supera o iguala 3
        #aqui sigue derecho, suma todo hasta 21
    else:
        print(suma)
        



        
birthday([1,2,3,4,5,6],3,2)
#[1,2,1,3,2],3,2
# ([4],4,1)
#([1,1,1,1,1,1],3,2)