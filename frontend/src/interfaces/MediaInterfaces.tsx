export interface MediaBase{
    title: string;
    genre: string;
    rent_price: number;
    image_url: string;
    media_description: string;
    release_date: Date;
    rating: string;
    media_id?: number;
}

export interface VideoGames extends MediaBase{
    publisher: string;
    developer: string;
}

export interface Movies extends MediaBase{
    runTime: number;
    director: string;
}
