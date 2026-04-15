// let data =["sameer","ajay","kumar"]
// console.log(data.length)
// // console.log(data.sort())
// console.log(data.reverse())
// -----------------------------------------------
//function declaration
//function without papameter

// const { data } = require("framer-motion/client")


// function data(){
//     console.log("Functions")
// }


// data()
// ------------------------------------------------
// function expression
// ananymous function

// let data=function(){
//     console.log("this is function expression")
// }
// data()

// ---------------------------------------------------------------


// function with parameter

// function hello(c,d){
//     console.log(c+d)
//     console.log(c-d)
// }

// hello(5,6)

// ----------------------------------
//postional urgument

// function hello(a,b=8){
//     console.log(a,b)
// }

// hello(7)



// tassk

// function hello(c,d){
//     console.log(c+d)
//     console.log(c-d)
// }

// hello(5,6)



// let dat=function(a,b){
//     console.log(a*b)
//     console.log(a/b)
// }
// dat(2,)



// function da(){
//      console.log("sameer")
// }

// da()


// --------------------------------------------------------


// function with return

// function add(a,b){
//     return a+b
// }
// let a=add(4,6)
// console.log(a)


//--------------------------------------------------------
// function add(a,b){
//     console.log("sdas")
//     return a+b;
//     console.log("asbb")    //after return the line can not work
// }
// let a=add(4,6)
// console.log(a)

//------------------------------------------------------------

// function add(){
//     console.log("sdas")
//     console.log("sdas")
//     console.log("sdas")
//     console.log("sdas")
//     console.log("sdas")
//     hello      //code willl get error next line does not print
//     console.log("sdas")
//     console.log("sdas")
    
// }

// add()


//----------------------------------------------------------

// function add(){
//     console.log("sdas")
//     console.log("sdas")
//     console.log("sdas")
//     console.log("sdas")
// }
// add()
// add()    //re duing multiple time uinsg function

//==============================================================

// let person={
//     name:"abc",
//     loc:'hyd',
//     age:23,
//     data:function(){
//         console.log(`my name is ${this.name}`) 
//     }
// }

// console.log(person)
// console.log(person.data)
// console.log(person.data())


//-------------------

// function add(){
//     console.log("this is")
// }

// console.log(add())
//---------------------------------------------------


//arrow method
//arrow ananymous function

// let data = ()=>{
//     console.log("this is arrow function")
// }

// data()

//single paremter


// let data = a=>{ console.log(a)}
// data(10)

// ==============================================

//higer order
// function data (hello) {
//     console.log("hi")
//     hello()
//     console.log("good morining...")

// }

// //call back
// function data_two(){
//     console.log("studnets")

// }

// data(data_two)

// recursive

function fac(n){
    if (n==0){

        return 1
    }
    else{
        return n*fac(n-1)
    }

}

console.log(fac(5))
 

//iife

(function(){
    console.log("this is iife")
})()