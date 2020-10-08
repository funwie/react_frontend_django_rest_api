import React from 'react';
import { Navbar } from 'react-bootstrap';

function NavBar(props) {

    return (
        <Navbar>
            <Navbar.Brand href="#">Winterfell Dry Cleaners</Navbar.Brand>
            <Navbar.Toggle />
            <Navbar.Collapse className="justify-content-end">
            </Navbar.Collapse>
        </Navbar>
    );
}

export default NavBar;