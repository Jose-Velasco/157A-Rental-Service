import { axiosPrivate } from "../axios";
import { useEffect } from "react";
import useAuth from "./useAuth";
import axios, { Axios } from "axios";

const isErrorResponse = (error: any, serverCode: number) => {
    return error.response && error.response.status === serverCode;
};

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
        const responseIntercept = axiosPrivate.interceptors.response.use(
            (response) => response,
            (error) => {
                if (axios.isAxiosError(error)) {
                    // if the error is a 401 and the user is logged in, log them out
                    if ((isErrorResponse(error, 401) || isErrorResponse(error, 403))) {
                        contextValue?.setAuth(null);
                    }
                }
                return Promise.reject(error);
            }

        );

        // remove/clean-up the interceptor when the component unmounts so they don't pile up
        return () => {
            axiosPrivate.interceptors.request.eject(requestIntercept);
            axiosPrivate.interceptors.response.eject(responseIntercept);
        }
    }, [auth]);
    return axiosPrivate;
};

export default useAxiosPrivate;