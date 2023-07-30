import React from 'react';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import {CardActionArea, CardActions} from '@mui/material';


interface ReusableCardProps {
  title: string;
  description: string;
  image: string;
}


export default function ReusableCard(props: ReusableCardProps) {
    return(
    <Card sx = {{maxWidth: 345, backgroundColor: "#757DE8"}}>
        <CardActionArea> 
            <CardMedia component = "img" height = "140" image = {props.image}/>
            <CardContent>
                <Typography gutterBottom variant = "h5" component = "div">
                    {props.title}
                    </Typography>
                    <Typography variant = "body2" color ="text.secondary">
                        {props.description}
                    </Typography>
                 </CardContent>



        </CardActionArea>
        </Card>
    );
}
