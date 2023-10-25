function pr(n,li){
    let ordenada=li.sort(); //[1, 1, 1, 1, 1,2, 3, 3, 3, 3,3]
    let sinRep= new Set(ordenada);
    let enArray =Array.from(sinRep) //[ 1, 2, 3 ]
    sinRep=[sinRep]

    let contadorUno=0;
    // let contador=0;

    for(let x of enArray){ 
        let cont=0;
        for(let i of ordenada){
            if(i==x){
                cont=cont+1
            }
        }                          
        //console.log(cont)
    if(cont%2==0 || cont==1){
        if(cont!==1){
            console.log(cont/2)
        }else{console.log(cont)}
    }else{
        console.log(cont-1)
    }
    
}
            
} 

    
    

pr(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])
//debe dar 3 y da 9
//pr(11,[1,1,3,1,2,1,3,3,3,3,1]) //4
//10 [1,1,3,1,2,1,3,3,3,3] debe dar 4 y me da 16

//FALTA CONTADOR FINAL DE PARES¿?