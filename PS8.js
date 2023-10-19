function pr(n,li){
    var contador=0;
    var acum=1;
    let resultado;
    let ordenada=li.sort();
    let sinRep= new Set(ordenada);
    console.log(sinRep);
    ordenada.forEach(function(p,indice,sinRep) {
        if(p==ordenada[indice+1]){
            contador= contador+1            
        } 
        console.log('elemento: ',p,'indice: ',indice, 'rta: ',contador);
    });

    for(let x in ordenada){// 0 1 2 3 
        for(let i of sinRep){//2 1 2 1
            if(i==ordenada[x]){
                contador= contador+1
            
            }
        }
    } 
    

    for(let x in li){ // 0 1 2 3 
        for(let i of li){//2 1 2 1
            if(i ==li[x]){
                
                contador=contador+1
                resultado= contador/n
                
            }
        }

    } 
    
    if(Number.isInteger(contador)){
        //let resultado= Math.sqrt((contador-2)/2)
        let resultado= Math.sqrt((contador-2))
        resultado=resultado.toString().split('.')
        // console.log(resultado[0])
    }
    // else{
    //     console.log(rta, contador)
    // }
}

// pr(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])
pr(11,[1,1,3,1,2,1,3,3,3,3,1])
//debe dar 3 y da 9

//10 [1,1,3,1,2,1,3,3,3,3] debe dar 4 y me da 16