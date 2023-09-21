function pr(n,li){
    for(let i=0; i<li.length;i++){
        const resultado = li.filter((x)=>x==li[i])
        console.log(resultado)
    }
}

pr(3,[2,1,2,1])