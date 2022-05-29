import React from 'react';
import ReactDOM from "react-dom";
import HadisApplication from "./App"

ReactDOM.render(
  // Our main React application component, which we've imported from another file
  <EmployeeApplication />,
  // Gets rendered to the <div> we defined in our Django template using the shared id
  document.getElementById('js-framework-home')
);