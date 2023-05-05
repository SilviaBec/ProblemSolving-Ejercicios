
def migratoryBirds(arr):
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

    arr=sorted(arr)
    for e in arr:
        arr.count(e)
        if arr.count(e) >= arr.count(e):
            print(e)
    
    #     indice=arr.index(arr.count(e))
    # print(arr[indice])
            
#necesito un contador cuantos hay de cada numero en el array
#cual es el mas repetido y si hay un empate 
#entre 2, elegir el mas bajo.
#answer here is 4 porque el 4 se repite 3 veces , la mayor frecuencia
migratoryBirds([1,2,3,4,5,4,3,2,1,3,4])