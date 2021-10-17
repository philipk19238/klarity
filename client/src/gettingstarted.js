import React from "react";
import Button from '@material-ui/core/Button';
import './graph.css';
import {Link } from "react-router-dom";

    function gettingstarted() {

        return (
            <Link to="/visualizer" style={{textDecoration: 'none'}}>
            <Button className = "btn-hover color-1" style={{color: 'white', fontSize: 20, fontWeight: 'bold', textDecoration: 'none'}}> Get Started </Button>
            </Link>
        );

    }

    export default gettingstarted;