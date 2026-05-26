// import img from "../assets/chai.jpg"

import { color } from "framer-motion"
import { head } from "framer-motion/client"

export const Design=()=>{
    let image = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=687&auto=format&fit=crop"

    // let internal={
    //     head:{
    //         color:"blue",
    //         backgroundColor:"cyan",
    //         padding:"11px"
    //     }

    // }
    return(

        <>
        <center>
            <h1 className="mb-5">Multi media &styling</h1>
            {/* <audio src="" controls></audio>
            <video src="" controls></video> */}
        {/* <img src={image} alt="" height={280}/>
        <img src={img}alt="" height={280}/>
        <img src="./chai.jpg" alt="" height={280}/>
        <img src="" alt="" /> */}
        {/* <h1 style={{color:"red",backgroundColor:'lightcyan',padding:"11px"}}>inline css</h1>
        <h2 style={internal.head}>internal css</h2>
        <h3 class="external">external css</h3> */}
        <div className="card" style={{width: "18rem;"}}>
        <img src={image} class="card-img-top" alt="..." height={100 }/>
        <div className="card-body">
            <h5 className="card-title">Card title</h5>
            <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card’s content.</p>
            <a href="#" className="btn btn-primary">Go somewhere</a>
        </div>
        </div>
        </center>

        </>
    )
} 