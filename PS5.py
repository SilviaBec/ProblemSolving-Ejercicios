
def migratoryBirds(arr):
    contador=1
    for e in arr:
        for x in range(1,len(arr)):
            if e==arr[x]:
                contador=contador+1
        print(e, contador)
#necesito un contados cuantos hay de cada numero en el array
#cual es el mas repetido y si hay un empate 
#entre 2, elegir el mas bajo.
#answer here is 4 porque el 4 se repite 3 veces , la mayor frecuencia
migratoryBirds([1,4,4,4,5,3])