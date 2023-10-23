function pr(n,li){
    let ordenada=li.sort(); //[1, 1, 1, 1, 1,2, 3, 3, 3, 3,3]
    let sinRep= new Set(ordenada);
    let enArray =Array.from(sinRep) //[ 1, 2, 3 ]
    sinRep=[sinRep]
    let i;
    let contadorUno=0;
    let contadorDos=0;
    let contadorTres=0;
    // let contador=0;

    for(let i of ordenada){ 
        if(i==1){
            contadorUno=contadorUno+1}
        
            }console.log(contadorUno)


            for(let x of ordenada){ 
                if(x==2){
                    contadorDos=contadorDos+1}
                
                    }console.log(contadorDos)


                    for(let w of ordenada){ 
                        if(w==3){
                            contadorTres=contadorTres+1}
                        
                            }console.log(contadorTres)
            


        } 

    
    

// pr(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])
//debe dar 3 y da 9
pr(11,[1,1,3,1,2,1,3,3,3,3,1]) //4
//10 [1,1,3,1,2,1,3,3,3,3] debe dar 4 y me da 16