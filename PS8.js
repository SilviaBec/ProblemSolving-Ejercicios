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

    }console.log(contador)    
    // for(let i=0; i<li.length;i++){
    //     const resultado = li.filter((x)=>x==li[i])
    //     console.log(resultado)
    // }

    let lista=[]
    for( let i=0;i<li.length;i++){
        if(lista.includes(li[i])==false){
            lista.push(li[i])
            
        }
        // lista.push(li[i])
        
    } //console.log(lista)


    //Eliminar duplicados
    const lista2= new Set(li);
    let resultado=[...lista2];
    //console.log(resultado)
    //Contar el numero de elementos de resultado en la lista original
    for(i of resultado){
        var contador=contador+1
        }
    } 
    //console.log(contador)


    // for(var i=0; of resultado){
    //     for(var x of li){
    //         rta2=console.count(x)
    //     }

    // } console.log(rta2)


pr(3,[2,1,2,1])