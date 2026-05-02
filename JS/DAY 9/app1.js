

let a =document.getElementById('check')
let b =document.getElementById('link')
b.addEventListener('click',(e)=>{
    if(!a.checked){
        alert("check the box to access the link")
        e.preventDefault()
    }
})



// ===========cards=================

let main=document.getElementById('parent')
main.addEventListener('click',(e)=>{
    // console.log(e.target)
    console.log(e.currentTarget)
})


//bubbling its moving buttom to top

// let p=document.getElementById('p')
// let ch=document.getElementById('ch')
// let sub=document.getElementById('sub')
// p.addEventListener('click',()=>{
//     console.log("iam parent")
// })
// ch.addEventListener('click',()=>{
//     console.log("iam child")
// })
// sub.addEventListener('click',()=>{
//     console.log("iam sub child")
// })

//stop propgation
// let p=document.getElementById('p')
// let ch=document.getElementById('ch')
// let sub=document.getElementById('sub')
// p.addEventListener('click',(e)=>{
//     console.log("iam parent")
//     e.stopPropagation()
// })
// ch.addEventListener('click',(e)=>{
//     console.log("iam child")
//     e.stopPropagation()
// })
// sub.addEventListener('click',(e)=>{
//     console.log("iam sub child")
//     e.stopPropagation()
// })




let p=document.getElementById('p')
let ch=document.getElementById('ch')
let sub=document.getElementById('sub')
p.addEventListener('click',()=>{
    console.log("iam parent")
},{capture:true})
ch.addEventListener('click',()=>{
    console.log("iam child")
    
},{capture:true})
sub.addEventListener('click',()=>{
    console.log("iam sub child")
},{capture:true})