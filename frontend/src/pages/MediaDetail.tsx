import React, { useEffect, useCallback, useState } from "react";
import {MediaBase, VideoGames, Movies} from "../interfaces/MediaInterfaces";
import ReusableCard from "../components/ReusableCard";
import { TextField, Typography, Button, Grid, Tooltip } from "@mui/material";
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
import RateReviewIcon from '@mui/icons-material/RateReview';
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';
import useUser from "../hooks/useUser";
import SaveIcon from '@mui/icons-material/Save';
import { InCart } from "../interfaces/cart";
import { useNavigate } from "react-router-dom";
import axios from "axios";


const style = {
    position: 'absolute' as 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };

const MediaDetail:React.FC = () => {
    const axiosPrivate = useAxiosPrivate();
    const navigate = useNavigate();
    const { media_id } = useParams<{ media_id: string }>();
    const [media, setMedia ] = useState<VideoGames | Movies | null>(null);
    const [ reviews, setReviews ] = useState<ReviewWithUser[] | null>(null);
    const [open, setOpen] = React.useState(false);
    const [ publishDate, setPublishDate ] = useState<string>("");
    const [ content, setContent ] = useState<string>("");
    const [ stars, setStars ] = useState<number>(0);
    const userContextValue = useUser();
    const user = userContextValue?.user;
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    const getReviews = async () => {
        let isMounted = true;
        const controller = new AbortController();
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

        getMedia();
        getReviews();
    
        return() => {
            isMounted = false;
            controller.abort();
        }
    },[]);

    const addToCart = async () => {
        try {
            const body: InCart = {
                media_id: media?.media_id ? media?.media_id : -1,
                cart_id: user?.cart_id ? user?.cart_id : -1,
            }
            const response = await axiosPrivate.post(`/cart/in`, body);
            navigate("/home");
        } catch (error) {
            if (axios.isAxiosError(error) && error.response?.status == 409) {
                alert(`${error.response.data.detail}. Please wait for another user to return the media.`);
                console.log("media is already in cart");
            }
            console.log(error);
            }
    };

    const createReview = async () => {
        try{
            const body = {
                user_id: user?.user_id ? user?.user_id : -1,
                media_id: media?.media_id ? media?.media_id : -1,
                content: content,
                stars: stars,
                publish_date: publishDate,
            }
            const response = await axiosPrivate.post(`/review/create_review`, body);
            getReviews();
            handleClose();
        }catch(error){
            console.log(error);
        }
    };

    return(
        <div style={{height: "100vh", display: "flex", overflowY: "hidden"}}>
            <div>
            <ReusableBar title={"to details page"}/>
            </div>
            <div style={{display: "flex", overflow: "hidden", marginTop: 55}}>
                
                { media &&
                <Card sx = {{maxWidth: 400, height: "100%", paddingTop: 2, margin: 0, backgroundColor: "#CCDEFF"}}>
                    <CardHeader title = {media.title} subheader = {`Release date: ${media.release_date}`}/>
                    <CardMedia component = "img" height = "300" image = {media.image_url}/>
                    <CardContent>
                        <Typography variant = "body2" color ="text.secondary">
                            {media.media_description}
                        </Typography>
                        <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                            {`Genre: ${media.genre}`}
                        </Typography>
                        <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                            {`Rating: ${media.rating}`}
                        </Typography>
                        { "publisher" in media && "developer" in media &&
                            (
                                <>
                            <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                                {`Publisher: ${media.publisher}`}
                            </Typography>
                            <Typography variant = "body2" color ="text.secondary" style={{fontWeight: "bold"}}>
                                {`Developer: ${media.developer}`}
                            </Typography>
                                </>
                            )
                        }
                        { "runtime" in media && "director" in media &&
                            (
                                <>
                            <Typography variant = "body2" style={{fontWeight: "bold"}}>
                                {`Runtime: ${media.runtime}`}
                            </Typography>
                            <Typography variant = "body2" style={{fontWeight: "bold"}}>
                                {`Director: ${media.director}`}
                            </Typography>
                                </>
                            )

                        }
                    </CardContent>
                    { user && user.cart_id &&
                    <CardActions style={{justifyContent: "center"}}>
                        <Button size="large" onClick={addToCart}>
                            <AddShoppingCartIcon fontSize="large" color="warning" />
                        </Button>
                        <Button size="large" onClick={handleOpen}>
                            <RateReviewIcon fontSize="large" color="success" />
                        </Button>
                    </CardActions>
                    }
                </Card>   
                }
                <List style={{overflowY: "auto", paddingLeft: 30, paddingRight: 30, paddingTop: 20, width: "100vw"}}>

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
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
        <Box sx={style}>
          <Typography id="modal-modal-title" gutterBottom variant="h6" component="h2">
          Create Review
          </Typography>
          <TextField label="publish date" type="date" fullWidth value={publishDate} onChange={(e)=> setPublishDate(e.target.value)}></TextField>
          <TextField label="content" type="text" fullWidth value={content} onChange={(e)=> setContent(e.target.value)}></TextField>
          <Tooltip title="0-5 integer only" placement="bottom" open={stars <= 5 && stars >= 0}>
          <TextField placeholder="Enter digit 0 - 5" InputLabelProps={{shrink: true}} label="stars 0-5"  inputProps={{ inputMode: 'numeric', pattern: '[0-5]' }} fullWidth value={stars} onChange={(e)=> setStars(+e.target.value)}></TextField>
          </Tooltip>
          <Button size="large">
                <SaveIcon onClick={createReview} fontSize="large" color="success" />
            </Button>
        </Box>
      </Modal>
        </div>
    )
};

export default MediaDetail;