import React from 'react';
import Graph from './graph';
import Button from '@material-ui/core/Button';
import ButtonAppBar from './Navbar';
import Home from './Home';
import Visualizer from './Visualizer';
import {
    BrowserRouter,
    Switch,
    Route,
    Link
  } from "react-router-dom";
import './graph.css';

require('typeface-dm-sans');

function App() {
return (
    <Switch>
     <Route exact path="/" component={Home} />
     <Route path="/visualizer" component={Visualizer} />
   </Switch>
);}
export default App;