// setInterval(()=>{
//     console.log("hi timing fucker")
// },5000)


// setTimeout(()=>{
//     console.log("hiiiiiiiiiiiii")
// },5000)



// function data(){
//     console.log("hiii sam")
// }

// setInterval(data,5000);


function addclock(){
    let a =new Date()
    let hours =a.getHours()
    let min =a.getMinutes()
    let sec =a.getSeconds()

    const time=(`${hours}:${min}:${sec}`)
    document.getElementById('time').innerText=time
    
}

setInterval(addclock,1000)
addclock()





