
from collections import Counter


def migratoryBirds(arr):
    # conteo=Counter(arr) #Counter({2: 2, 1: 1, 4: 1}) numero: frecuencia en lista
    # maxima=max(conteo.values())
    # print(maxima)
            #Hasta aca voy super bien me imprime 2 2 las dos frecuencias mas repetidas
    

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




    #INTENTO CON COMPRENSION DE LISTAS FALLÓ, PERO AVANZÓ, QUITAR SORTET MAYBE:
    # if len(arr)>5 and len(arr)<200000:
    # arr=sorted(arr)
    # frecuencias=[arr.count(e) for e in arr]
    # print(arr[frecuencias.index(max(frecuencias))])



    frec=Counter(arr) #Counter({2: 2, 1: 1, 4: 1}) numero: frecuencia en lista
    maxi= max(frec.values()) #2 el valor maximo de frecuencia
    #frec.items() me da: ([(1, 1), (2, 2), (4, 1)])
    resultado=[x for x,y in frec.items() if y == maxi] #por cada x,y en el diccionario fre.items() 
    #añadir x o sea el numero del array si y o sea la frecuencia es = a el num maximo de frecuencia
    print (min(resultado))

            
#necesito un contador cuantos hay de cada numero en el array
#cual es el mas repetido y si hay un empate 
#entre 2, elegir el mas bajo.
#answer here is 4 porque el 4 se repite 3 veces , la mayor frecuencia
migratoryBirds([1,2,2,4])
#El problema que debo tener aca [1,2,2,4] es que las frecuencias son  1 2 2 1
# si elijo el mas bajo sale 1 pero 1 porque 1 esta dos veces pero no es un
#num de frecuencia repetida sino 2 diferentes de frecuencia 1
#arreglar eso!!!!!!!!!!!!