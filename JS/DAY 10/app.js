// console.log(document)----url page
// console.log(window)

// document.body.style.backgroundColor ="Red"

// let p =document.getElementsByTagName('ul')  //html collection
// // console.log(p)
// p[1].style.backgroundColor ='blue'

// let p=document.getElementsByClassName("numbers1")
// // console.log(p)
// p[0].style.backgroundColor="yellow"



// let i =document.getElementById('l1')// give direct element
// console.log(i)
// i.style.backgroundColor='orange'

// let p= document.querySelector('ul')
// p.style.backgroundColor='orange'
// console.log(p)

// let p=document.querySelectorAll('ul')//node list
// // console.log(p)
// p[0].style.backgroundColor='green'



// let p=document.getElementById('num')
// // console.log(p.parentNode )// asking who p 's parent
// // console.log(p.childNodes)
// console.log(p.nextSibling )



//maupilation=============================


// let num =document.getElementById('num')
// // console.log(num)

// // first create a tag

// let li6= document.createElement('li')
// li6.setAttribute('id','l6')
// li6.textContent = "six"
// num.appendChild(li6)
// console.log(li6)


// let li7= document.createElement('li')
// li7.setAttribute('id','l7')
// li7.textContent = "seven"
// // num.insertBefore(li7,l3)   //in specific place
// // num.replaceChild(li7,l3)//for replce first new next old in parameter
// num.removeChild(l3)//for remove
// console.log(li7)

// let a =document.getElementById('number')
// console.log(a.getAttribute('class'))



let hi =document.getElementById('hi')
console.log(hi.innerText)
console.log(hi.textContent)
// console.log(hi.textContent())