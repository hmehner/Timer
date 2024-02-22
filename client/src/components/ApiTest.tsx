import React, { useState, useEffect } from 'react'

interface Data {
    message: string;
}

const ApiTest: React.FC = () => {

    const [data, setData] = useState<Data | null>(null)

    useEffect(() => {
        console.log('page loaded')
        fetch('http://localhost:5000/test')
            .then((response) => response.json())
            .then((data) => {
                console.log(data.message)
                setData(data)
            })
    }, []);

    return (
        <>
            <h1>API Data:</h1>
            <p>{data ? data.message : 'Lade Daten...'}</p>
        </>
    )
}

export default ApiTest;

