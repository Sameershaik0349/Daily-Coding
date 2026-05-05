// function validation(){
//     let user=document.getElementById('username').value
//     let pass=document.getElementById('pass').value
//     if(user.trim()===""|| pass.trim()===""){
//         return false
//     }
//     else{
//         alert("sucessfully submitted")
//         return true
//     }
// }
function validation(){
    let isvalid=true;
    let usernamepattern=/^[A-Z]{1}[a-z]{8,}$/
    let passwordpattern=/^[A-Z]{1}[a-z]{8,}$/

    let errou=document.getElementById('erroru')
    let errop=document.getElementById('errorp')

    let username=document.getElementById('username').value
    let password=document.getElementById('pass').value

    if(!usernamepattern.test(username)){
        isvalid=false;
        errou.innerHTML="please enter valid username"
        errou.style.color='red'
    }
    else{
        errou.innerHTML=""
    }

    if(!passwordpattern.test(password)){
        isvalid=false;
        errop.innerHTML="please enter valid password"
        errop.style.color='red'
    }
    else{
        errop.innerHTML=""
    }

    if(isvalid){
        alert("succesfull")
    }

    return isvalid
    
}


