export interface Review {
    review_id?: number;
    media_id: number;
    publish_date: Date;
    content: string;
    stars: number;
}

export interface ReviewWithUser extends Review {
    first_name: string;
    last_name: string;
    profile_pic_URL: string;
}