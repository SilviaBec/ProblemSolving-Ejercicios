function breakingRecords(scores) {
    // Write your code here
    var acumMax=0
    var acumMin=0
    
    for(const x of scores){
        if(x<scores[scores.indexOf(x)+1]){
            acumMin=acumMin+1
        }
        if(x>scores[scores.indexOf(x)+1]){
            acumMax=acumMax+1
        }

    }
    rta.push(acumMax,acumMin)
    return rta
    

}
breakingRecords([10,5,20,20,4,5,2,25,1])

