  import { useState } from "react"  

export const Home =()=>{
    let [count,setCount]=useState(0)

    // function increamne(){
    //     setCount(count+1)
    // }
    // function dec(){
    //     setCount(count-1)
    // }
    return (
        <>
        <center>
            <h1>This is home page</h1>
            {/* <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptates, ad voluptate. Molestias explicabo, dolorum itaque, facere saepe praesentium quam nesciunt blanditiis nostrum maiores, commodi ducimus? Inventore sit reprehenderit laborum ipsa!</p> */}
            <h2>Count:-{count}</h2>
            {/* <button className="btn btn-primary m-2 " onClick={increamne}>increamnet</button>
            <button className="btn btn-danger m-2 "onClick={dec}>decreamnet</button> */}
            <button className="btn btn-primary m-2 " onClick={()=>setCount(count+1)}>increamnet</button>
            <button className="btn btn-danger m-2 "onClick={()=>setCount(count-1)}>decreamnet</button>
            </center>
        </>
    )
}