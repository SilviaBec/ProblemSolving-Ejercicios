def birthday(s, d, m):
    resultado2=[]
    for x in s:
        for i in range(1,len(s)+1):
            if x+s[s.index(x)+i] ==d:
                resultado =x,s[s.index(x)+i]
                if resultado not in resultado2:
                    resultado2.append(resultado)
                if len(resultado2)==m:
                    print(len(resultado2))

# def birthday(s, d, m):
#     resultado2=[]
#     for x in s:
#         if x==d and len(resultado2)==m:
#                 print(m)
#         else: 
#             while x<d:
#                 for i in range(1,len(s)+1):
#                     if x+s[s.index(x)+i] ==d:
#                         pass

                        
#             resultado =x,s[s.index(x)+1]
#             if resultado not in resultado2:
#                 resultado2.append(resultado)
#     if len(resultado2)==m:
#         print(len(resultado2))

            

        
        
birthday([1,1,1,1,1,1],3,2)
#[1,2,1,3,2],3,2
# ([4],4,1)
#([1,1,1,1,1,1],3,2)