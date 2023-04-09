// import pages
import './js/theme_toggler.js';

import React from 'react';
import ReactDOM from 'react-dom';
import 'vite/modulepreload-polyfill';

import './sass/style.scss';

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap';

import CreateOrderController from './js/create_order';

window['mainModule'] = {
    CreateOrderController,
    React,
    ReactDOM,
    bootstrap,
};
