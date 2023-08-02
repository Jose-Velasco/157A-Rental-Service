import React, { useEffect, useCallback, useState } from "react";
import {MediaBase, VideoGames, Movies} from "../interfaces/MediaInterfaces";
import ReusableCard from "../components/ReusableCard";
import { TextField, Typography, Button, Grid } from "@mui/material";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { useParams } from 'react-router-dom';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import ReusableBar from "../components/ReusableBar";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import Divider from '@mui/material/Divider';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import Rating from '@mui/material/Rating';
import CalendarTodayIcon from '@mui/icons-material/CalendarToday';
import AddShoppingCartIcon from '@mui/icons-material/AddShoppingCart';
import { ReviewWithUser } from "../interfaces/review";
import {environment} from "../axios";

const MediaDetail:React.FC = () => {
    const axiosPrivate = useAxiosPrivate();
    const { media_id } = useParams<{ media_id: string }>();
    const [media, setMedia ] = useState<VideoGames | Movies | null>(null);
    const [ reviews, setReviews ] = useState<ReviewWithUser[] | null>(null);

    useEffect(() =>{
        let isMounted = true;
        const controller = new AbortController();

        const getMedia = async () => {
            try{
                const response = await axiosPrivate.get<VideoGames | Movies>(`/media/details/${media_id}`,{
                    signal: controller.signal,
                }).then((response) => {
                    let media = response.data;
                    if(isMounted && media){
                        setMedia(media);
                    }
                });

            }catch(error){
                console.log(error);
            }
        }

        const getReviews = async () => {
            try {
                const response = await axiosPrivate.get(`/review/search_review_by_media_id/${media_id}`,{
                    signal: controller.signal,
                }).then((response) => {
                    let reviews = response.data;
                    if(isMounted && reviews){
                        setReviews(reviews);
                    }
                });

            } catch (error) {
                console.log(error);
            }
        };

        getMedia();
        getReviews();
    
        return() => {
            isMounted = false;
            controller.abort();
        }
    },[]);

    return(
        <div style={{height: "100vh", display: "flex", overflowY: "hidden"}}>
            <div>
            <ReusableBar title={"to details page"}/>
            </div>
            <div style={{display: "flex", overflow: "hidden", marginTop: 55}}>
                
                { media &&
                <Card sx = {{maxWidth: 400, height: "100%", paddingTop: 2, margin: 0, backgroundColor: "#CCDEFF"}}>
                    <CardHeader title = {media.title} subheader = {`${media.release_date}`}/>
                    <CardMedia component = "img" height = "300" image = {media.image_url}/>
                    <CardContent>
                        <Typography variant = "body2" color ="text.secondary">
                            {media.media_description}
                        </Typography>
                        <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                            {media.genre}
                        </Typography>
                        <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                            {media.rating}
                        </Typography>
                        <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                            {media.rent_price}
                        </Typography>
                        { "publisher" in media && "developer" in media &&
                            (
                                <>
                            <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                                {media.publisher}
                            </Typography>
                            <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                                {media.developer}
                            </Typography>
                                </>
                            )
                        }
                        { "runTime" in media && "director" in media &&
                            (
                                <>
                            <Typography variant = "body2" style={{fontWeight: "bold"}}>
                                {media.runTime}
                            </Typography>
                            <Typography variant = "body2" style={{fontWeight: "bold"}}>
                                {media.director}
                            </Typography>
                                </>
                            )

                        }
                    </CardContent>
                    <CardActions style={{justifyContent: "center"}}>
                        <Button size="large">
                            <AddShoppingCartIcon fontSize="large" color="warning" />
                        </Button>
                    </CardActions>
                </Card>   
                }
                <List style={{overflowY: "auto", paddingLeft: 30, paddingRight: 30, paddingTop: 20}}>

                    {
                        reviews?.map((review) => (

                            <>
                            
                    <ListItem alignItems="flex-start">
                    <ListItemAvatar>
                    <Avatar alt={`${review.first_name} ${review.last_name}`} src={`${environment.baseAPIURL}${review.profile_pic_URL}`} />
                    </ListItemAvatar>
                    <ListItemText style={{wordBreak: "break-all"}}
                    primary={
                        <React.Fragment>
                        <Rating name="read-only" value={review.stars} readOnly />
                        </React.Fragment>
                    }
                    secondary={
                        <React.Fragment>
                        <Typography
                            sx={{ display: 'inline' }}
                            component="span"
                            variant="body2"
                            color="text.primary"
                        >
                            {`${review.first_name} ${review.last_name}`} <CalendarTodayIcon fontSize="small"/> {`${review.publish_date}`}
                            <br/>
                        </Typography>
                        <Typography component={'span'}>

                        {review.content}
                        </Typography>
                        </React.Fragment>
                    }
                    />
                </ListItem>
                <Divider variant="inset" component="li" style={{marginBottom: 15, marginTop: 15}} />
                            
                            </>

                        ))
                            
                    }



                
                </List>
            </div>
        </div>
    )
};

export default MediaDetail;