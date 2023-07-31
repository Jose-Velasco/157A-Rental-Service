import { axiosPrivate } from "../axios";
import { useEffect } from "react";
import useAuth from "./useAuth";

const useAxiosPrivate = () => {
    const contextValue = useAuth();
    const auth = contextValue?.auth;
    // attach the access token to the Authorization header using an interceptor
    useEffect(() => {
        const requestIntercept = axiosPrivate.interceptors.request.use(
            (config) => {
                if (!config.headers.Authorization && auth?.access_token) {
                    config.headers.Authorization = `Bearer ${auth.access_token}`;
                }
                return config;
            }, (error) => Promise.reject(error)
        )
        // remove/clean-up the interceptor when the component unmounts so they don't pile up
        return () => {
            axiosPrivate.interceptors.request.eject(requestIntercept);
        }
    }, [auth]);
    return axiosPrivate;
};

export default useAxiosPrivate;