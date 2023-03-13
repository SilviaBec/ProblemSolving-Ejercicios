function breakingRecords(scores) {
    // Write your code here
    contadorMin=0
    contadorMax=0

    for(const x of scores){
        if(x==scores.min || x<scores.min){
            contadorMin=contadorMin+1
        }
        if(x==scores.max || x<scores.max){
            contadorMax=contadorMax+1
// x<scores[scores.indexOf(x)+1]
        }

    }

    console.log(contadorMax,contadorMin)

}
breakingRecords([10,5,20,20,4,5,2,25,1])

