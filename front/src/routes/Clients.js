import Menu from "../components/Menu";
import Table from "../components/Table";
import axios from "axios";
import {useEffect, useState} from "react";


function Clients({setClients}) {
    const [data, setData] = useState([]);

    async function getClients() {
        console.log('getClients')
        try {
            const response = await axios.get('http://localhost:8000/clients');
            // console.log(response.data)
            setClients(response.data)
            setData(response.data)
        } catch (error) {
            console.error(error);
        }
    }

    useEffect(async () => {
        await getClients();
    }, [])

    return (
        <div>
            <Menu/>
            <div className={'container'}>
                <h3>Clients:</h3>
                <Table data={data}/>
            </div>
        </div>
    );
}

export default Clients;