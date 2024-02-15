import { useState, useEffect } from 'react';
import axios from 'axios';

function ApiTest() {
    const [data, setData] = useState([]);

    useEffect(() => {
    const getData = async () => {
        axios.get('http://localhost:5000/test')
        .then(response => 
            {
                console.log(response)
            }
        ).catch(error => 
            {
                console.log(error)
            }
        )
    };
    getData();
  }, []);

    // Rendern Sie die empfangenen Daten
    return (
        <>
        </>
    );
}

export default ApiTest;
