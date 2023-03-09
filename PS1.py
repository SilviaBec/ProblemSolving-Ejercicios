# The elements of the first array are all factors of the integer being considered
def getTotalX(a, b):
    factores=[]
    SinDuplicados=[]
    final1=[]

    final2=[]

    # Write your code here
    for i in b:
        for x in range(1,i+1):
            if i%x==0:
                factores.append(x)


    for z in range(0,len(factores)):
        if factores.count(factores[z])==len(b):
            if factores[z] not in SinDuplicados:
                SinDuplicados.append(factores[z])
            # SinDuplicados.append(factores[z])
            # list(set(SinDuplicados))
    for y in a:
        for w in SinDuplicados:
            if w%y==0:
                final1.append(w)
                for t in range(0,len(final1)):
                    if final1.count(final1[t])==len(a):
                        if final1[t] not in final2:
                            final2.append(final1[t])
    print(final2)
                

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

