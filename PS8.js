function pr(n,li){
    let ordenada=li.sort(); //[1, 1, 1, 1, 1,2, 3, 3, 3, 3,3]
    let sinRep= new Set(ordenada);
    let enArray =Array.from(sinRep) //[ 1, 2, 3 ]
    sinRep=[sinRep]

    for(let x of enArray){  //10, 20, 30, 50
        let cont=0;
        for(let i of ordenada){
            if(i==x){
                cont=cont+1
            }
        }                          
        //console.log(cont) HASTA ACA CUENTA CUANTOS HAY DE C/NUM
    if(cont%2==0){
        console.log(cont/2)
    }else if(cont%2 !==0 && cont-1!==0 ){
        console.log(cont-1)
        }
    }
}
    
//DA DOS QUE SON 2 POR LAS 2 PAREJAS DE 10 PERO 2 DEL 3-1 QUE ES UNA SOLA PAREJA DE 20S ARREGLAR ESO

            

    

pr(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])
//debe dar 3 y da 9
//pr(11,[1,1,3,1,2,1,3,3,3,3,1]) //4
//10 [1,1,3,1,2,1,3,3,3,3] debe dar 4 y me da 16
//FALTA CONTADOR FINAL DE PARES¿?