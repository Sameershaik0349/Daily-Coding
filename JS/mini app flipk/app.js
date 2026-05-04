// const { FunctionSquare } = require("lucide-react");

const products = [
  {
    id:1,
    name: "iPhone 13",
    price: 59999,
    description: "Apple smartphone with A15 Bionic chip and dual camera system.",
    image: "https://via.placeholder.com/150?text=iPhone+13"
  },
  {
    id:2,
    name: "Samsung Galaxy S21",
    price: 49999,
    description: "Flagship Samsung phone with AMOLED display and powerful performance.",
    image: "https://via.placeholder.com/150?text=Galaxy+S21"
  },
  {id:3,
    name: "OnePlus Nord 2",
    price: 29999,
    description: "Fast and smooth smartphone with great camera and performance.",
    image: "https://via.placeholder.com/150?text=Nord+2"
  },
  {id:4,
    name: "Realme Narzo 50",
    price: 14999,
    description: "Budget-friendly phone with good battery and gaming performance.",
    image: "https://via.placeholder.com/150?text=Narzo+50"
  },
  {id:5,
    name: "Redmi Note 11",
    price: 13999,
    description: "Affordable smartphone with AMOLED display and long battery life.",
    image: "https://via.placeholder.com/150?text=Note+11"
  },
  {id:6,
    name: "Boat Headphones",
    price: 1999,
    description: "Stylish wireless headphones with deep bass and long battery.",
    image: "https://via.placeholder.com/150?text=Headphones"
  },
  {id:7,
    name: "HP Laptop",
    price: 45999,
    description: "Reliable laptop for work and study with good performance.",
    image: "https://via.placeholder.com/150?text=HP+Laptop"
  },
  {id:8,
    name: "Dell Monitor",
    price: 12999,
    description: "Full HD monitor with clear display and slim design.",
    image: "https://via.placeholder.com/150?text=Dell+Monitor"
  },
  {id:9,
    name: "Logitech Mouse",
    price: 799,
    description: "Ergonomic mouse with smooth tracking and long battery life.",
    image: "https://via.placeholder.com/150?text=Mouse"
  },
  {id:10,
    name: "Sony Smart TV",
    price: 69999,
    description: "4K smart TV with stunning visuals and Dolby sound.",
    image: "https://via.placeholder.com/150?text=Sony+TV"
  }
];

let parent =document.getElementById('parent')
let cart=[]
function data(products){
    let b=products.map((items)=>{
        return `<div id='card'><h1>${items.name}</h1>
            <p>${items.description}</p>
            <mark>${items.price}</mark>
            <br><br>
            <button onclick="add(${items.id})">addproduct</button>
            </div>`
    })

    parent.innerHTML=b.join('')
}

data(products)

function fil(){
    let ser=document.getElementById('in').value.toLowerCase()
    let tempdata=products.filter(items=>items.name.toLowerCase().includes(ser))
    data(tempdata)
}

//add to cart


function add(product){
    let tempdata=products.find(items=>items.id==product)
    alert(`${tempdata.name}is added to cart`)
    cart.push(tempdata)
    bill()
    document.getElementById('cartto').innerHTML=cart.length
}


function bill(){
    let sum=cart.reduce((acc,val)=>acc+val.price,0)
    document.getElementById('bil').innerHTML=sum
}