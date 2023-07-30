import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import { Toolbar } from '@mui/material';
import IconButton from '@mui/material';
import Typography from '@mui/material/Typography';
import InputBase from '@mui/material';
import InventoryIcon from '@mui/material';
import ShoppingCart from '@mui/material';
import MenuItem from '@mui/material';
import Menu from '@mui/material';

interface ReusableBarProps {
    title : string;
    showInventoryIcon?: boolean;
 
}
 

export default function ReusableBar(props: ReusableBarProps) {


    return (
        <AppBar position="static" sx={{ backgroundColor: "#757DE8" }}>
            <Toolbar sx={{ justifyContent: "space-between" }}>
            
                
                </Toolbar>

            </AppBar>

    );
}