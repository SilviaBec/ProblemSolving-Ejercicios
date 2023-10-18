function pr(n,li){
    var contador=0;
    for(let x in li){ // 0 1 2 3 
        for(let i of li){//2 1 2 1
            if(i ==li[x]){
                
                contador=contador+1
                contador=contador/2
                
            }
        }

    }   
    
    if(Number.isInteger(contador)){
        let resultado= Math.sqrt((contador-2)/2)
        resultado=resultado.toString().split('.')
        console.log(resultado[0])
    }
}

pr(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])

//debe dar 3 y da 9

//10 [1,1,3,1,2,1,3,3,3,3] debe dar 4 y me da 16