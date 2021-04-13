import React, {useState} from 'react'
import Dgrid from "./Dgrid"
import Barchart from "./Barchart"

export default function Home(props) {
    const [click, setClick] = useState(true)
    
    return (
        <div className="Container">
            <p className="title"> Welcome to the monitoring App</p>
            
            <button className="btn-home" onClick={() => {
                setClick(!click) 
            }}>Click here to see the data</button>
            {click? <Dgrid vision="none" />: <Dgrid vision="block" />  }
            <Barchart></Barchart>
        </div>
    )
}
