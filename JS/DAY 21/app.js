// function outer(){
//     let a =10
//     console.log(a)
//     function inner(){
//         console.log(a)
//     }
//     inner()
// }



// outer()


function outer(){
    let count=0
    function inner(){
        count++
        console.log(count)
    }
    return inner()
}

let a =outer()
console.log(a)