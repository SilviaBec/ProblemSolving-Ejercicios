
def migratoryBirds(arr):
    
    for e in arr:
        for x in range(1,len(arr)):
            if e == arr[x]:
                frecuencia=0
                frecuencia = frecuencia+1
                print(frecuencia)
            else:
                frecuencia=1
                print(frecuencia)

        #     cuenta=0
        #     cuenta=cuenta+1
        # print(cuenta)
        # for x in range(0,len(arr)):
        #     if e in arr:


        
    
    
    
#     frecuencias=[]
#     finalistas=[]
#     if len(arr)>=5 and len(arr)<=200000:
#         for e in arr:
#             frecuencias.append(arr.count(e))
        
#         for x, y in zip(arr,frecuencias):
#             if y ==max(frecuencias):
#                 finalistas.append(x)
#     print(min(finalistas))

    
    #---------------------SEGUNDO INTENTO MUCHAS MENOS LINEAS MISMOS CASOS FALLIDOS---------
    # frecuencias=[]
    # if len(arr)>5 and len(arr)<200000:
    #     arr=sorted(arr)
    #     for e in arr:
    #         frecuencias.append(arr.count(e))
    # print(arr[frecuencias.index(max(frecuencias))])




            
#necesito un contador cuantos hay de cada numero en el array
#cual es el mas repetido y si hay un empate 
#entre 2, elegir el mas bajo.
#answer here is 4 porque el 4 se repite 3 veces , la mayor frecuencia
migratoryBirds([1,2,2,4])