import { title } from "framer-motion/client"
import { Child } from "./Child"

export const Prop = () => {
    let data={
        title:"hoodie",
        price:222
    }
    return (
        <>
            <center>
                <div className="card p-5 m-5 w-50 border border-dark border-3 text-primary">
                    <h1 className="parent">this is parent</h1>
            <Child name={data.title} buy={data.price}/>
            <Child/>
                </div>
            </center>
        </>
    )
} 