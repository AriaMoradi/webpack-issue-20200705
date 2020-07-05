import ReactDOM from 'react-dom';
import React from 'react';

let props = JSON.parse(document.getElementById('react_props').innerHTML);

ReactDOM.render(
    React.createElement(window.component,props),
    document.getElementById('root')
);