import React, { useEffect } from "react";
import { TextField, Typography} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import {Link} from "react-router-dom";
import ReusableCard from "../components/ReusableCard";
import axios from "../axios";
import ReusableBar from "../components/ReusableBar";
import {MediaBase, VideoGames, Movies} from "../interfaces/MediaInterfaces";

const Home:React.FC = () => {
    const [media, setCard] = useState<VideoGames[]>();


     useEffect(() =>{

        let isMounted = true;
        const controller = new AbortController();
    
        const getCard = async () => {
            try{
                const response = await axios.get("/media/video-game",{
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
        getCard();
    
        return() => {
            isMounted = false;
            controller.abort();
        }
    }
    
    ,[]);
    return(
        <form>
            {media?.map ((item) => (
            <ReusableCard title = {item.title}
            description = {item.media_description}
            image = {item.image_url}
            />
                 ))}   
        </form>
    );
};


export default Home;