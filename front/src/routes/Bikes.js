import Menu from "../components/Menu";
import Table from "../components/Table";
import axios from "axios";
import {useEffect, useState} from "react";


function Bikes({setBikes}) {
    const [data, setData] = useState([]);

    async function getBikes() {
        console.log('getBikes')
        try {
            const response = await axios.get('http://localhost:8000/bikes');
            // console.log(response.data)
            setBikes(response.data);
            setData(response.data);
        } catch (error) {

            console.error(error);
        }
    }

    useEffect(async () => {
        await getBikes();
    }, [])

    return (
        <div>
            <Menu/>
            <div className={'container'}>
                <h3>Bikes:</h3>
                <Table data={data}/>
            </div>
        </div>
    );
}

export default Bikes;