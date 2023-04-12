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
for(var i of ar){ // 1 3 2 6 1 2
    for(let x=0; x< ar.length;x++){ // 0 1 2 3 4 5
        if(x<x+1 && (ar[x]+ar[x+1])%k){
            
            console.log(x,x+1)
            
            }

        }
    }

    //no esta dando debe dar 
    //1-2/1-2/3-6/