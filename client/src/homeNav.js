import React from "react";
import Button from '@material-ui/core/Button';
   import {Link } from "react-router-dom";

    function homeNav() {

        return (
            <Link to="/" style={{textDecoration: 'none'}}>
            <Button style={{ color: 'white', fontSize: 20, fontWeight: 'bold', textDecoration: 'none'}}>Home </Button>
            </Link>
        );

    }

    export default homeNav;