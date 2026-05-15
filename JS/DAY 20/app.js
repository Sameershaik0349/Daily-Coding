// async function data(){
//     return 's'     // async function return a prpmise
// }

import productsData from "./Data"



// let a =data()
// console.log(a);




// async function data(){
//     return 1     // async function return a prpmise
// }

// let a =data()
// console.log(a);




// async function data(){
//     return 1     // async function return a prpmise
// }

// let a =data()
// .then(x=>console.log(x))



// let a =new Promise((resolve,reject)=>{
//     resolve("this is my promise")
// })
// async function data() {
//     return a
// }
// let b =data()
// .then(x=>console.log(x))






// let a =new Promise((resolve,reject)=>{
//      resolve("this is my promise")
//  })
// async function data() {
//       let v=await a  
//       console.log(v)
// }
// data()




///destructing

// let array={
//     name:'sameer',
//     age:21,
//     marks:"pass",
//     loc:"hyd"
// }

// let {name,age,marks,loc}=array
// console.log(name)



// let data=['sun','mon','tues','wed']
// let [a,b,c,d]=data
// console.log(c)


import productsData from "./Data.js"

let parent= document.getElementById('parent')



async function dummy() {
    let a =await productsData
    let {products}=await a.json()
    
    let b=products.map((items)=>{
        return `<div id="cards">
            <img src="${items.thumbnail}" alt="" height=160>
            <h1>${items.title}</h1>
            <p>${items.description}</p>
            <mark>${items.price}</mark>
            </div>`
    })
    parent.innerHTML=b.join('')

}
