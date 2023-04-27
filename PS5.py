
def migratoryBirds(arr):
    lista=[]
    lista2=[]
    contador=1
    for e in arr:
    
        if e not in lista:
            lista.append(e)
            
        else:
            lista2.append(e)
            print(lista2.count(e))
            
#necesito un contados cuantos hay de cada numero en el array
#cual es el mas repetido y si hay un empate 
#entre 2, elegir el mas bajo.
#answer here is 4 porque el 4 se repite 3 veces , la mayor frecuencia
migratoryBirds([1,4,4,4,5,3])