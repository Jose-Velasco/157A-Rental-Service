export interface Token {
    access_token: string;
    token_type: string;
}

export interface TokenData {
    username: string;
}

export interface JSONWebToken {
    // subject whom the token refers to
    sub: string;
    // expiration time (seconds since Unix epoch?)
    exp: number;
}