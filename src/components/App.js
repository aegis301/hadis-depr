import React, { Component } from 'react';
import { render } from 'react-dom';
import Typography from '@mui/material/Typography';


export default function App(props) {
    return (
        <Typography variant="h1" color="initial">Hello, world!</Typography>
    );
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);


