// import { data } from "framer-motion/client"\
import { data } from "framer-motion/client"
import { Subchild } from "./Subchild"
import { color } from "framer-motion"

export const Child=({name="redmi",buy=233})=>{
    return(
        <>
        <center>
        <div className="card m-4 w-50 border border-dark border-3px">
            <h1>{name}</h1>
            <h3>{buy}</h3>
        </div>
        </center>
        </>
    )
}