# The elements of the first array are all factors of the integer being considered
def getTotalX(a, b):
    
    SinDuplicados=[]
    final1=[]
    
    final3=[]
    final2=[]
    
    # Write your code here
    for i in b:
        factores=[]
        for x in range(1,i+1):
            if i%x==0:
                factores.append(x)
        # print(factores)
            for y in a:
                if x in factores and x%y==0:
                    print(x)

#             for w in factores:
#                 if w not in SinDuplicados:
#                     SinDuplicados.append(w)
#                 else:
#                     final1.append(w)
# #             parte2=list(set(final1))            
    
            # if x not in final2:
            #     final2.append(x)
            # else:
            #     final3.append(x)
    # print(final3)
                        
                    
    
#     print(len(list(set(final3[1:len(final3)-1]))))

getTotalX([2,4],[16,32,96])

# if w not in final1:
#                         final1.append(w)
#                     else:
#                         print(w)







# def getTotalX(a, b):
#     factores=[]
#     sinDuplicados=[]
#     final1=[]
#     final2=[]
#     # Write your code here
#     for i in b:
#         for x in range(1,i+1):
#             if i%x==0:
#                 factores.append(x)
#     for w in factores:
#         if w not in sinDuplicados:
#             sinDuplicados.append(w)
#         else:
#             for y in a:
#                 if w%y==0:
#                     if w not in final1:
#                         final1.append(w)
#                     else:
#                         final2.append(w)
#     return len(final2)
                
