import './App.css';
import {useState} from "react";
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from "./routes/Home";
import Clients from "./routes/Clients";
import Bikes from "./routes/Bikes";


function App() {
    const [clients, setClients] = useState([]);
    const [bikes, setBikes] = useState([]);

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home/>}/>
                <Route path="clients" element={<Clients setClients={setClients}/>}/>
                <Route path="bikes" element={<Bikes setBikes={setBikes}/>}/>
            </Routes>
        </BrowserRouter>

    )
        ;
}

export default App;
