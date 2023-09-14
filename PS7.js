function bueno(cuenta,lokno,pago){
    let acum=0;
    for(var i=0;i<cuenta.length ;i++){
        acum=acum+cuenta[i];
        console.log(acum)
    } 
        if(pago-((acum-cuenta[lokno])/2)==0){
            console.log("Aprobado")
        }else{
            console.log(pago-((acum-cuenta[lokno])/2))
        }
    
}
bueno([5,10,3,9],1,12)

