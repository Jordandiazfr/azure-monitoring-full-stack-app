import './App.css';
import Dgrid from "./components/Dgrid"
import Home from "./components/Home"
import logo  from "./assets/logo.png"
import React, {useState} from "react"

function App() {
  let jojo = "0"
  const [click, setClick] = useState(false)
  return (
    <div className="App"> 

    <img src={logo} className="head-logo"></img>
    <Home jojo={jojo} />

    
    </div>
  );
}

export default App;
