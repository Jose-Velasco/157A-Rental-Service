import React, { useEffect } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import {Link} from "react-router-dom";
import ReusableCard from "../components/ReusableCard";
import ReusableBar from "../components/ReusableBar";
import {MediaBase, VideoGames, Movies} from "../interfaces/MediaInterfaces";
import Grid from '@mui/material/Grid';
import useAxiosPrivate from "../hooks/useAxiosPrivate";

const Home:React.FC = () => {
    const axiosPrivate = useAxiosPrivate();
    const [media, setCard] = useState<VideoGames[]>();
    const [movie, setMovie] = useState<Movies[]>();

     useEffect(() =>{
     let isMounted = true;
        const controller = new AbortController();
    
        const getCard = async () => {
            try{
                const response = await axiosPrivate.get("/media/video-game",{
                    signal: controller.signal,
                });
                console.log(response.data)
                if(isMounted){
                    setCard(response.data);
                    const mediaTitles = media?.map((item) => item.title); // Creates an array of titles from the media array
                }
            }catch(error){
                console.log(error);
            }
        }

        const getMovie = async () => {
            try{
                const response = await axiosPrivate.get("/media/film",{
                    signal: controller.signal,
                });
                console.log(response.data)
                if(isMounted){
                    setMovie(response.data);
                    const mediaTitles = movie?.map((item) => item.title); // Creates an array of titles from the media array
                }
            }catch(error){
                console.log(error);
            }
        }

        getCard();
        getMovie();
    
        return() => {
            isMounted = false;
            controller.abort();
        }
    }
    ,[]);

    return(
        <form style={{padding: "2rem"}}>
            <ReusableBar title = "Jeffrey"  showInventoryIcon = {false}/>
            <Typography marginTop= {15}align="left"  fontSize={35} color="#808080"> Recommended Games </Typography>
            <Grid container spacing={6}>
            {media?.slice(0,3).map ((item) => (
                  <Grid item xs={4} sm={4} md={4}>
            <ReusableCard title = {item.title} media_id={item.media_id ? item.media_id : -1}
            description = {item.media_description}
            image = {item.image_url}/>
           </Grid>      
               ))}  
        </Grid>

        <Typography align="left" marginTop={6}  fontSize={35} color="#808080"> Recommended Movies </Typography>
            <Grid container spacing={6}>
            {movie?.slice(0,3).map ((item) => (
                  <Grid item xs={4} sm={4} md={4}>
            <ReusableCard title = {item.title} media_id={item.media_id ? item.media_id : -1}
            description = {item.media_description}
            image = {item.image_url}/>
           </Grid>      
               ))}  
        </Grid>

        </form>
    );
};


export default Home;