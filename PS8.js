function pr(n,li){
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
        
    }console.log(lista)


    //Eliminar duplicados
    const lista2= new Set(li);
    let resultado=[...lista2];
    console.log(resultado)
    // Contar el numero de elementos de resultado en la lista original
    

}

pr(3,[2,1,2,1])