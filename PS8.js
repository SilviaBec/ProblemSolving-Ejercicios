function pr(n,li){
    var contador=0;
    let i;
    let x;
    for(x in li){ // 0 1 2 3 
        for(i of li){//2 1 2 1
            if(i ==li[x]){
                
                contador=contador+1
                
                
            }
        }

    }   
    
    if(Number.isInteger(contador)){
        console.log((contador-n)/2)
    }
}

pr(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])

//debe dar 3 y da 9

//10 [1,1,3,1,2,1,3,3,3,3] debe dar 4 y me da 16