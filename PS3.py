# a=[1,1,1,1,1,1]
# dia=3
# acumulado=0

# for x in a:
#         while acumulado<dia:
#             acumulado=acumulado+x
#             print(acumulado)



def birthday(s, d, m):
    resultado2=[]
    acumulado=0
    if s[0]==d:
        print(m)
    else:
        while acumulado<d:
            for x in s:
                for i in range(len(s)):
                    # acumulado = 
                    acumulado = acumulado +(x+s[i])
    print(acumulado)


        
birthday([1,2,3,4,5,6],3,2)
#[1,2,1,3,2],3,2
# ([4],4,1)
#([1,1,1,1,1,1],3,2)