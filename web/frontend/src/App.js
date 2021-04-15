import './App.css';
import Home from "./components/Home"
import logo  from "./assets/logo.png"
import React from "react"

function App() {
  let jojo = "0"
  return (
    <div className="App"> 

    <img src={logo} className="head-logo" alt="logo"></img>
    <Home jojo={jojo} />

    
    </div>
  );
}

export default App;
