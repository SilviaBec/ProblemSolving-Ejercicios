

const ar=[1,3,2,6,1,2]
const k=3
var lista2=[]
let conta=0
for(let i=0; i< ar.length;i++){ // 0 1 2 3 4 5
    for(let j=1;j< ar.length;j++){
        if(i<j && ((ar[i]+ar[j])%k==0)){
            lista2.push([i,j])
            
                
            
        }
    }
    

    
}
for(let e of lista2){
    conta=conta+1
}
console.log(conta)
        
        
    //no esta dando debe dar 
    //0-2/0-5/1-3/2-4/4-5/
    //node PS4.js