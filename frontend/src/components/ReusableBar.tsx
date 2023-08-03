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
import HomeIcon from '@mui/icons-material/Home';
import DomainIcon from '@mui/icons-material/Domain';
import CreateIcon from '@mui/icons-material/Create';
import { Home } from '@mui/icons-material';




interface ReusableBarProps {
  title: string;
  showInventoryIcon?: boolean;
  showCreateIcon?: boolean;
}

export default function ReusableBar(props: ReusableBarProps) {
  return (
    <AppBar position="absolute"sx={{ backgroundColor: "#757DE8", width: "100%"}}>
      <Toolbar sx={{ justifyContent: "center" }}>
        <Typography variant="h6" component="div" sx={{ flexGrow: 0 }}>&nbsp;{props.title}
        </Typography>
        {/* Render icons conditionally if showInventoryIcon is true */}
        <Link to="/home">
        <IconButton size="large" aria-label="Home">
          <HomeIcon />
          </IconButton>
          </Link>
        {props.showInventoryIcon &&
        <Link to = "/inventory">
        <IconButton size="large" aria-label="Inventory" color = "error">
        <InventoryIcon />
        </IconButton>
        </Link>}
        <Link to="/cart-checkout">
        <IconButton size="large" aria-label="Shopping Cart" color="success">
            <ShoppingCartIcon />
        </IconButton>
        </Link>
        <Link to="/search">
        <IconButton size="large" aria-label="Search" >
            <SearchIcon />
        </IconButton>
        </Link>
        <IconButton size = "large" aria-label="Manage Accounts">
          <ManageAccounts />    
        </IconButton>
        {props.showCreateIcon &&
        <IconButton size = "large" aria-label="Create" color="error">
          <CreateIcon />
          </IconButton>}
        
      </Toolbar>
    </AppBar>
  );
}
