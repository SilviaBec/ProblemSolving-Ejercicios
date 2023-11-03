function pr(n,li){
    let ordenada=li.sort(); //[1, 1, 1, 1, 1,2, 3, 3, 3, 3,3]
    let sinRep= new Set(ordenada);
    let enArray =Array.from(sinRep) //[ 1, 2, 3 ]
    sinRep=[sinRep]
    let pares=0;
        let impares=0;

    for(let x of enArray){  //10, 20, 30, 50
        let cont=0;
        for(let i of ordenada){
            if(i==x){
                cont=cont+1
            }
        }                          
        //console.log(cont) 
        
        //HASTA ACA CUENTA CUANTOS HAY DE C/NUM 4 3 1 1 
        //[10, 10, 10, 10, 20, 20, 20, 30, 50]

    if(cont%2==0){//Si es par que lo divida en 2
        pares=cont/2
        
    } else if(cont%2!==0 && (cont-1)!==0 ){//Si es impar y != de 1
        impares= (cont-1)/2
        }
        
    }console.log(pares+impares)
}
    
//DEBO SUMAR LAS PAREJAS Y DAR UN SOLO NUM
//NO ESTA FUNCIONANDO CON LA SEGUNDA tanda
            

    

//pr(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])
//debe dar 3 y da 9
pr(11,[1,1,3,1,2,1,3,3,3,3,1]) //4
//10 [1,1,3,1,2,1,3,3,3,3] debe dar 4 y me da 16
//FALTA CONTADOR FINAL DE PARES¿?