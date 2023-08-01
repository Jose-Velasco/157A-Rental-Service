import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import SearchIcon from '@mui/icons-material/Search';
import InventoryIcon from '@mui/icons-material/Inventory';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import MenuItem from '@mui/material/MenuItem';
import Menu from '@mui/material/Menu';
import ManageAccounts from '@mui/icons-material/ManageAccounts';
import { IconButton } from '@mui/material';
import { Link } from 'react-router-dom';



interface ReusableBarProps {
  title: string;
  showInventoryIcon?: boolean;
}

export default function ReusableBar(props: ReusableBarProps) {
  return (
    <AppBar position="absolute"sx={{ backgroundColor: "#757DE8", width: "100%"}}>
      <Toolbar sx={{ justifyContent: "center" }}>
        <Typography variant="h6" component="div" sx={{ flexGrow: 0 }}>
          Welcome,&nbsp;{props.title}&nbsp;
        </Typography>
        {/* Render icons conditionally if showInventoryIcon is true */}
        {props.showInventoryIcon &&
        <IconButton size="large" aria-label="Inventory" color="inherit">
        <InventoryIcon />
        </IconButton>}
        <IconButton size="large" aria-label="Shopping Cart" color="inherit">
            <ShoppingCartIcon />
        </IconButton>
        <Link to="/search">
        <IconButton size="large" aria-label="Search" >
            <SearchIcon />
        </IconButton>
        </Link>
        <IconButton size = "large" aria-label="Manage Accounts" color="inherit">
          <ManageAccounts />    
        </IconButton>
        
      </Toolbar>
    </AppBar>
  );
}
