//this line imports react functionality 
import React from 'react';
import { useEffect, useState } from "react";
import { LineChart, Line, Tooltip} from 'recharts';
import './graph.css';
require('typeface-pt-sans');



function CustomTooltip(props) {
    var price = ""
    var date = ""
    console.log(props)

    if (props.data[props.label]) {
        price = props.data[props.label]["1. open"]
        date = props.data[props.label]["date"]
    }



    return (
        <div>
            <div >{date} </div>
            <div style={{ color: "#000000", fontWeight: 'bold'}}> $ {price}</div>
            
        </div>
    )

}


export default function App() {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState([]);
    const data = [];
    // Note: the empty deps array [] means
    // this useEffect will run once
    // similar to componentDidMount()
    useEffect(() => {
        fetch("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=O19KF6HV0JGF7DRI")
            .then(res => res.json())
            .then(
                (result) => {
                   
                    for (var instance in result["Weekly Time Series"] ) {
                        var mydata = (result["Weekly Time Series"][instance])
                        mydata.date= instance
                        data.push(mydata)
                    }
                    //var isArray = Array.isArray(data);
                    setItems(data.reverse())
                },

                // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
                // exceptions from actual bugs in components.
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )

            
    }, [])




    return (
        <div>
            <LineChart width={500} height={250} margin={{ top: 150, right: 30, left: 20, bottom: 5 }} data={items}>

                        <Line dot={false}  type="monotone" dataKey="1. open" stroke="#82ca9d" strokeWidth={4} fill="#62ac92" yAxisId="100" />
                       <Tooltip content={<CustomTooltip data={items} />} />
                        
                    </LineChart>             
        </div>
    )
}