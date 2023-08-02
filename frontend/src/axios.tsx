import axios from 'axios';
export const environment = {
    baseAPIURL: "http://localhost:8000",
};


export default axios.create({
    baseURL: environment.baseAPIURL,

});

export const axiosPrivate =  axios.create({
    baseURL: environment.baseAPIURL,
    headers: {"Content-Type": "application/json"},
    withCredentials: true,
});