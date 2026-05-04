// //for each

// let a =[1,2,3,4,5]
// a.forEach((items)=>{
//     console.log(items)
// })

//--------------------------------------------------------------
//map

// let data=a.map((items)=>{
//     return items*2 // it iterates and mul all elemnts in array 
// })

// console.log(data)

//-------------------------------------------------
//filter    filtering by condtion

// let data=a.filter((item)=>{
//     return item%2==0
// })

// console.log(data)
//---------------------------------------------
//reduce()

// let data=a.reduce((acc,val)=>{
//     return acc+val
// },0)
// console.log(data)


// //some

// let a =[1,2,3,4,5]
// let data =a.some((item)=>{
//     return item>2

// })

// console.log(data)


// })

// console.log(data)


//sort

let a=[1,2,3,4,5]
a.sort((a,b)=>a-b)  //1,2=>1-2=1 if when negtive value came it swap in behind scence ascending order
a.sort((a,b)=>b-a)  //1,2=>1-2=1 if when posituve value came it swap in behind scence------decsending ordder
console.log(a)