// console.log("task1")
// setTimeout(()=>{
//     console.log("task2")
// },3000)
// console.log("task3")

// const { data } = require("framer-motion/client")



// let p=new Promise((resolve,reject)=>{
//     console.log("task1")
//     setTimeout(()=>{
//         console.log("task2")
//         resolve()
//     },3000)
// })
// .then(()=>{
//     console.log("task3")
// })
// console.log(p)
// ----------------------------------------------------
// let p=new Promise((resolve,reject)=>{
//     console.log("task1")
//     setTimeout(()=>{
//         console.log("task2")
//         reject()
//     })
// })
// .then(()=>{
//     console.log("task3")
// })


// console.log(p)




//--------------------FETCH---------------------/\\


//IIIIIIIIIIIIIIIIIIIIIIIIMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMPPPPPPPPPPPPPPPPPPPPPPPPPPPPP______________________________????????????????????>>>>>>>>>>>???????/////////////////

let parent=document.getElementById('parent')
fetch("https://dummyjson.com/products?limit=10")

// console.log(p)
.then((Response)=>{
    return Response.json()
})
.then((data)=>{
    let b=data.products.map((items)=>{
        return ` <div id="card">
            <img src="${items.thumbnail}">
            <h2>${items.title}</h2>
            <p>${items.description}</p>
            <mark>${items.price}</mark>
            
        </div>`
    })
    parent.innerHTML=b.join('')
})





//example for how the dummpy data works
// let p=fetch("https://dummyjson.com/products?limit=10")

// .then((Response)=>{
//     return Response.json()
// })
// .then((data)=>{
//     console.log(data)
// })
// console.log(p)


