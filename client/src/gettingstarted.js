import React from "react";
import Button from '@material-ui/core/Button';
   import {Link } from "react-router-dom";

    function gettingstarted() {

        return (
            <Link to="/visualizer" style={{textDecoration: 'none'}}>
            <Button className = "font-loader" style={{backgroundColor: '#BB87CD', color: 'white', fontSize: 20, fontWeight: 'bold', textDecoration: 'none'}}> Get Started </Button>
            </Link>
        );

    }

    export default gettingstarted;