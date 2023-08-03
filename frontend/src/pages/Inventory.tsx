import React, { useEffect } from "react";
import { TextField, Typography, Tooltip} from "@mui/material";
import Button from "@mui/material/Button";
import { useState } from "react";
import {Link} from "react-router-dom";
import ReusableCard from "../components/ReusableCard";
import ReusableBar from "../components/ReusableBar";
import {MediaBase, VideoGames, Movies} from "../interfaces/MediaInterfaces";
import Grid from '@mui/material/Grid';
import useAxiosPrivate from "../hooks/useAxiosPrivate";
import useUser  from "../hooks/useUser";
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';
import MovieCreationIcon from '@mui/icons-material/MovieCreation';
import { Gamepad, TextFields } from "@mui/icons-material";
import PlumbingIcon from '@mui/icons-material/Plumbing';
import DeleteIcon from '@mui/icons-material/Delete';


const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };

const Inventory:React.FC = () => {

    const axiosPrivate = useAxiosPrivate();
    const [media, setCard] = useState<VideoGames[]>();
    const [movie, setMovie] = useState<Movies[]>();
    const [open, setOpen] = React.useState(false);

    const[title , setTitle] = useState<string>("");
    const[genre , setGenre] = useState<string>("");
    const[image_url , setImageUrl] = useState<string>("");
    const[media_description , setMediaDescription] = useState<string>("");
    const[release_date , setReleaseDate] = useState("");
    const[rating , setRating] = useState<string>("");

    const[publisher , setPublisher] = useState<string>("");
    const[developer , setDeveloper] = useState<string>("");


    const[runTime , setRunTime] = useState<number>(0);
    const[director , setDirector] = useState<string>("");





    const handleClose = () => setOpen(false);

    const createGame = async () => {
        try{
            const body = {
                title: title,
                genre: genre,
                image_url: image_url,
                media_description: media_description,
                release_date: release_date,
                rating: rating,
                publisher: publisher,
                developer: developer,
            }
            const response = await axiosPrivate.post(`/media/video-game`, body);
            handleClose();
        }catch(error){
            console.log(error);
        }
    };
    


    const createMovie = async () => {
        try{
            const body = {
                title: title,
                genre: genre,
                image_url: image_url,
                media_description: media_description,
                release_date: release_date,
                rating: rating,
                runtime: runTime,
                director: director,
            }
            const response = await axiosPrivate.post(`/media/film`, body);
            handleClose();
        }catch(error){
            console.log(error);
        }

    };




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


    const removeMedia = async (media_id: number) => {
        let isMounted = true;
        const controller = new AbortController();
        try {
            const deleteBody = { 
                media_id: media_id,
            };
            const response = await axiosPrivate.delete(`/media/film`, { data: deleteBody });
            if (isMounted) {    

            }
        } catch (error) {
            console.log(error);
        }
    };



    const removeGame = async (media_id: number) => {
        let isMounted = true;
        const controller = new AbortController();
        try {
            const deleteBody = { 
                media_id: media_id,
            };
            const response = await axiosPrivate.delete(`/media/video-game`, { data: deleteBody });
            if (isMounted) {    

            }
        } catch (error) {
            console.log(error);
        }
    };


    return(


        <form style={{padding: "2rem"}}>
            
        
        
        <ReusableBar title = "Inventory"  showInventoryIcon = {true} showCreateIcon = {true}/>

            <Typography marginTop= {15}align="left"  fontSize={35} color="#808080"> All Games </Typography>
            <Grid container spacing={6}>
            {media?.map ((item) => (
                  <Grid item xs={4} sm={4} md={4}>
            <ReusableCard title = {item.title} media_id={item.media_id ? item.media_id : -1}
            description = {item.media_description}
            image = {item.image_url}/>
                      <Button size="large" onClick={() => removeGame(item.media_id ? item.media_id : -1)}>
            <DeleteIcon fontSize="large" color="error"/>
            </Button>
           </Grid>      
               ))}  
        </Grid>

        <Typography align="left" marginTop={6}  fontSize={35} color="#808080"> All Movies </Typography>
            <Grid container spacing={6}>
            {movie?.map ((item) => (
                  <Grid item xs={4} sm={4} md={4}>
            <ReusableCard title = {item.title} media_id={item.media_id ? item.media_id : -1}
            description = {item.media_description}
            image = {item.image_url}/>
            <Button size="large" onClick={() => removeMedia(item.media_id ? item.media_id : -1)}>
            <DeleteIcon fontSize="large" color="error" />
            </Button>
           </Grid>      
               ))}  
        </Grid>

        

        <Button
        size="large"
        onClick={() => setOpen(true)}
        style={{ marginTop: '250px'}} // Add margin to the top of the button
      >
        <PlumbingIcon fontSize="large" color="error" />
      </Button>
<Modal
      open={open}
      onClose={handleClose}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
      style = {{overflow :"scroll"}}
    >
      <Box sx={{overflow: 'scroll', width: 450, bgcolor: 'background.paper', p: 2 }}>
        <Typography variant="h6" component="h2" gutterBottom>
          Create Media
        </Typography>
        <TextField
          label="Title"
          variant="outlined"
          fullWidth
          margin="normal"
          value={title}
          onChange={(e) => setTitle(e.target.value)}/>
          <TextField label = "Genre" 
            variant = "outlined"
            fullWidth
            margin = "normal"
            value = {genre}
            onChange = {(e) => setGenre(e.target.value)}/>
            <TextField label = "Image URL"
            variant = "outlined"
            fullWidth
            margin = "normal"
            value = {image_url}
            onChange = {(e) => setImageUrl(e.target.value)}/>
            <TextField label = "Description"
            variant = "outlined"
            fullWidth
            margin = "normal"
            value = {media_description}
            onChange = {(e) => setMediaDescription(e.target.value)}/>
            <TextField label = ""
            variant = "outlined"
            fullWidth
            type = "date"
            margin = "normal"
            value = {release_date}
            onChange = {(e) => setReleaseDate(e.target.value)}/>
            <TextField label = "Rating"
            variant = "outlined"
            fullWidth
            margin = "normal"
            value = {rating}
            onChange = {(e) => setRating(e.target.value)}/>
            <TextField label = "Publisher"
            variant = "outlined"
            fullWidth
            margin = "normal"
            value = {publisher}
            onChange = {(e) => setPublisher(e.target.value)}/>
            <TextField label = "Developer"
            variant = "outlined"
            fullWidth
            margin = "normal"
            value = {developer}
            onChange = {(e) => setDeveloper(e.target.value)}/>
            <TextField label = "Run Time"
            variant = "outlined"
            fullWidth
            type = "number"
            margin = "normal"
            value = {runTime}
            onChange = {(e) => setRunTime(Number(e.target.value))}/>
            <TextField label = "Director"
            variant = "outlined"
            fullWidth
            margin = "normal"
            value = {director}
            onChange = {(e) => setDirector(e.target.value)}/>
            <div> No need to enter publisher and developer for movie. No need to enter the run time and director for movies.</div>


        <Button size="large">
          <MovieCreationIcon onClick={createMovie} fontSize="large" color="success" />
        </Button>
        <Button size="large">
          <Gamepad onClick={createGame} fontSize="large" color="success" />
        </Button>
      </Box>
    </Modal>



            </form>
    )

    


}

export default Inventory;