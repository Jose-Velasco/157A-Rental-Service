import React, { useState } from "react";
import ReusableBar from "../components/ReusableBar";
import {MediaBase } from "../interfaces/MediaInterfaces";
import ReusableCard from "../components/ReusableCard";
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import { TextField, Typography, Button, Grid } from "@mui/material";

interface SearchMediaCardsProps {
    medias: MediaBase[];
}


const SearchMediaCards:React.FC<SearchMediaCardsProps> = ({ medias }) => {
    return (
        <Grid container spacing={2}>
        {medias.map ((media, index) => (
              <Grid item xs={2} sm={2} md={4}>
        <ReusableCard key={index} title = {media.title} media_id={media.media_id ? media.media_id : -1}
        description = {media.media_description}
        image = {media.image_url}/>
       </Grid>      
           ))}  
    </Grid>
    );
}

const SearchMedia:React.FC = () => {
    const axiosPrivate = useAxiosPrivate();
    const [search, setSearchbox] =  useState<string>("");
    const [ searchedMedias, setSearchedMedias] = useState<MediaBase[]>([]);
    const controller = new AbortController();

    const onSearch = async (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        try{
            const response = await axiosPrivate.get("/media/search",{
                signal: controller.signal,
                params: {
                    searchTitle: search
                }
            }).then((response) => {
                setSearchedMedias(response.data);
            });
        } catch(error){
            console.log(error);
            setSearchedMedias([]);
        }
    }

    return (
        <>
        <ReusableBar title = "Search Page"  showInventoryIcon = {false} />
        <div style={{marginTop: 65}}>
        <TextField id="search-bar" type="text" label="Enter Media Title!"  variant="outlined" value={search} onChange={(e)=> setSearchbox(e.target.value)} fullWidth />
        <Button type= "button" fullWidth variant = "contained" color = "success" sx={{mt:3,mb:2}} onClick={onSearch}>Search</Button>
        <Typography marginTop= {15}align="left"  fontSize={35} color="#808080"> Media Results </Typography>
        <SearchMediaCards medias={searchedMedias}/>
        {searchedMedias.length === 0 && <Typography marginTop= {15}align="left"  fontSize={35} color="#880808"> No Results </Typography>}
        </div>
        </>
    );
};

export default SearchMedia;