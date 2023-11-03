function pr(n,li){
    let ordenada=li.sort(); //[1, 1, 1, 1, 1,2, 3, 3, 3, 3,3]
    let sinRep= new Set(ordenada);
    let enArray =Array.from(sinRep) //[ 1, 2, 3 ]
    sinRep=[sinRep]
    let acum=0;
    

    for(let x of enArray){  //10, 20, 30, 50
        let cont=0;
        for(let i of ordenada){
            if(i==x){
                cont=cont+1
            }
        }                          
        //console.log(cont) 
        
    if(cont%2==0){
        acum=acum+(cont/2)
        
    } else if(cont%2!==0 && (cont-1)!==0 ){
        acum= acum+((cont-1)/2)
        }
        
    }console.log(acum)
}
    
pr(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])
//debe dar 3 
