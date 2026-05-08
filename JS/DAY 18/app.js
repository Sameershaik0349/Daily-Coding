// console.log(document)//url of html

// const { data } = require("framer-motion/client")

//method function
// let person={
//     name:'sameer',
//     age:21,
//     loc:'hyd',
//     data:function(){
//         console.log(`this is my name:-${this.name}`)
//     }
// }

// arrow function

// let person={
//     name:'sameer',
//     age:21,
//     loc:'hyd',
//     data:()=>{
//         console.log(`this is my name:-${this.name}`)
//     }
// }


// console.log(person.data())

//events=============================================
// let btn=document.getElementById('btn')
// btn.addEventListener('click',function(){
//     console.log(this)
// })



//constructor method............................


// function Stud(name,age){
//     this.name=name
//     this.age=age
// }


// class Sus{
//     constructor(name,age){
//         this.name=name
//         this.age=age
//     }
// }

// let a=new Sus("sameer",21)
// console.log(a)



//=============================explicit binding===================================

//sending one msg to 100 peopele or more so the secario is here


function msg(name,greet){
    return(`hii ${name} good ${greet} your bus is ${this.bus}`)
}




let driver1={
    name:'abc',
    loc:'hyd',
    bus:"orange", 
}
let driver2={
    name:'opo',
    loc:'hyd',
    bus:"kaveri"
}
let driver3={
    name:'uio',
    loc:'hyd',
    bus:"tirumal"
}
let driver4={
    name:'rt',
    loc:'hyd',
    bus:"apsrtc"
}

// console.log(driver1.data("sameer","night"))




// msg.call(driver3,"sam","evening")

// msg.apply(driver1,["sameer","moring"])

// let a =msg.bind(driver1,"sameer","mrng")

// console.log(a("sam","eveing"))

//for multiple peopele  using return
let a =msg.bind(driver1)

console.log(a("sam","eveing"))
console.log(a("sam","eveing"))
console.log(a("sam","eveing"))
console.log(a("sam","eveing"))
console.log(a("sam","eveing"))