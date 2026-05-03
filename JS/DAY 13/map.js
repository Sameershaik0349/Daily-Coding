const products = [
  {
    id:1,
    title: "iPhone 16pro",
    description: "Latest Apple smartphone with A15 chip",
    price: 80000,
    image:"https://www.apple.com/newsroom/images/2024/09/apple-debuts-iphone-16-pro-and-iphone-16-pro-max/article/Apple-iPhone-16-Pro-hero-geo-240909_inline.jpg.large.jpg"
  },
  {
    id:2,
    title: "Samsung Galaxy S22",
    description: "High performance Android flagship phone",
    price: 70000,
  },
  { id:3,
    title: "OnePlus Nord 2",
    description: "Smooth performance with great camera",
    price: 30000,
  },
  { id:4,
    title: "HP Laptop",
    description: "Powerful laptop for work and study",
    price: 60000,
  },
  { id:5,
    title: "Dell Inspiron",
    description: "Reliable laptop with long battery life",
    price: 55000,
   
  },
  {id:6,
    title: "Nike Shoes",
    description: "Comfortable and stylish running shoes",
    price: 5000,
    
  },
  {id:7,
    title: "Adidas Sneakers",
    description: "Trendy sneakers for daily wear",
    price: 4500,
    
  },
  {id:8,
    title: "Sony Headphones",
    description: "Noise cancelling wireless headphones",
    price: 3000,
    
  },
  {id:9,
    title: "Apple Watch",
    description: "Smartwatch with fitness tracking",
    price: 25000,
    
  },
  {id:10,
    title: "Bluetooth Speaker",
    description: "Portable speaker with deep bass",
    price: 2000,
  }
];



let parent =document.getElementById('parent')
let b=products.map((items)=>{
    return `<div id="card">
            <h1>${items.id}</h1>
            <img src="${items.image}">
            <p>${items.title}</p>
            <mark>${items.price}</mark>
        </div>`
})

parent.innerHTML=b.join('')