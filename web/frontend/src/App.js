import './App.css';
import Cost from "./components/Cost"
import Dgrid from "./components/Dgrid"
function App() {
  return (
    <div className="App"> 
    <h1> Monitoring App</h1>
    
    <Dgrid></Dgrid>
 {/* <form>
 <label>indiquez les dates recherchées format JJ/MM/AAAA</label>
    <label>Date de début : <input type="text"> </input></label>
    
    <label>Date de fin : <input type="text"> </input></label>
    <button> ok </button>
    
 </form> */}
    
    </div>
  );
}

export default App;
