import React, { Component } from 'react';
import { render } from 'react-dom';
import Typography from '@mui/material/Typography';
import Home from './Home';
import HadisAppBar from './AppBar';



export default function App(props) {
    return (<div>
        <HadisAppBar />
        <Typography variant="h5" color="initial">Hello, {props.name}!</Typography>
    </div>
        
    );
}

const appDiv = document.getElementById('app');
render(<App name="Lea" />, appDiv);


