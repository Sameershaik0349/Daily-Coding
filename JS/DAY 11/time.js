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




// =======set time out==========


//clear timeout============

// let time =setTimeout(() => {
//     console.log("ffff")    
// }, );

// clearTimeout(time)//it stops excuting for settimout after there tie
//ex:-if settimeout is alaram for 5 sec after 5 sec its exceute but cleartimeout stops that







//clearinterval

// let i =1;
// let time=setInterval(() => {
//   console.log(i) 
//   i++; 
// },1000);




// let i =1;
// let time=setInterval(() => {
//   console.log(i) 
//   i++; 
//   if(i==6){
//     clearInterval(time)
//   }
// },1000);