import React, { Component } from 'react';
import { render } from 'react-dom';

export default function Test(props) {
    return (
        <Typography variant="h1" color="initial">Hello, patients!</Typography>
    );
}

const testDiv = document.getElementById('test-div');
render(<Test />, testDiv);