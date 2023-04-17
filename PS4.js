// const ar=[1,3,2,6,1,2]
// const k=3
// var lista2=[]
// for(var i of ar){
//     for(let x=0; x< ar.length;x++){
//         if(i<ar[x] && (ar[i]+ar[x])%k){
//             var lista=[]
//             lista.push(i,ar[x])
//             console.log(lista)
            
//             }

//         }
//     }
    
    


//node PS4.js




const ar=[1,3,2,6,1,2]
const k=3
var lista2=[]
for(let i=0; i< ar.length;i++){ // 0 1 2 3 4 5
    if(i<i+1 && (ar[i]+ar[i+1])%k){
        var lista2=[]
        lista2.push(i,i+1)
        console.log(lista2)
    }
    
}
        
        
    //no esta dando debe dar 
    //1-2/1-2/3-6/
    //node PS4.js