import React from 'react';
import { Link } from "react-router-dom";
import Graph from './graph';
import Button from '@material-ui/core/Button';
import ButtonAppBar from './Navbar';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import GettingStarted from "./gettingstarted";
import './graph.css';
import sofa from './sofa.png';

require('typeface-dm-sans');


const Home = () =>  {
return (
    <html>
    <div className = "font-loader">
    <ButtonAppBar/>
    <br></br>
    <br></br>
    <br></br>
    <br></br>
    <body>
    <div className = "font-loader"
                style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center"
                }}
            >
    <h1 style={{ color: '#BB87CD', fontSize: 64, fontWeight: 'bold' }}> A Smart Way To Buy </h1>
    </div>
    <div className = "font-loader"
                style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center"
                }}
            >
    <p style={{ color: '#000000', fontSize: 18}}> KLARITY is a powerful search engine that removes the ambiguity <br></br> surrounding resale markets. By allowing buyers to find competitive pricing <br></br> and providing sellers a market standard to price their goods, we aim to <br></br> eliminate market inefficiencies and fraud that ruin user experience.<br></br></p>
    </div>
    <br></br>
    <br></br>
    <GettingStarted/>
    <br></br>
    <br></br>
    <br></br>
    <div className = "font-loader"
    style={{
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}
    >
    <img src={sofa} width="720px" height="450px" alt="Klarity Marketplace"/>
    </div>
    </body>
    </div>
    </html>
);
}
export default Home;