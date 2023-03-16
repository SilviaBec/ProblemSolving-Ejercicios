function breakingRecords(scores) {
    // Write your code here
    var alto=0
    var bajo=0
    var acumMax=0
    var acumMin=0
    rta=[]
    
    for(const x of scores){
        if(x<scores[scores.indexOf(x)+1]){
            bajo=x
        }        
        if(x>scores[scores.indexOf(x)+1]){
            alto=x  
        } 
        if(x>alto){
            alto=x
            acumMax=acumMax+1
        }
        if(x<bajo){
            bajo=x
            acumMin=acumMin+1
        }
        
        
//creo que el error esta en que 10 es menor que 28 , es decir lo compara
//con el num siguiente no el acum
//No debe compararse al acumulado que serian 1 2 3 etc sino al numero min o max
    }
    rta.push(acumMax,acumMin)
    console.log(rta)
    

}
breakingRecords([10,5,20,20,4,5,2,25,1])
//3,4,21,36,10,28,35,5,24,42 debe dar 4 0 ya funciono 
//10 5 20 20 4 5 2 25 1 ESTE DEBE DAR 2 4
