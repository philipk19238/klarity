import React from 'react';
import Graph from './graph';
import ButtonAppBar from './Navbar';
const Visualizer = () => {
    return (
        <html>
        <ButtonAppBar/>
        <br></br>
        <br></br>
        <br></br>
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
                >      <br></br>
                <br></br>
                <br></br>
                <br></br>
                    <Graph/>
                    </div>
                    </body>
                    </html>

    );
}
 
export default Visualizer;