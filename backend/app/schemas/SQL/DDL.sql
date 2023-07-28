CREATE TABLE User(
    user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    profile_pic_URL VARCHAR(1023) NOT NULL,
    age INTEGER NOT NULL,
    phone_number INTEGER NOT NULL
);

CREATE TABLE Address(
    user_id INTEGER NOT NULL,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    zip_code INTEGER NOT NULL,
    state VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    PRIMARY KEY(user_id, street, city),
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Email(
    user_id INTEGER NOT NULL,
    email VARCHAR(690) PRIMARY KEY,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


CREATE TABLE Employee(
    user_id INTEGER NOT NULL,
    ssn INTEGER PRIMARY KEY,
    salary INTEGER NOT NULL,
    start_date date NOT NULL,
    employee_type ENUM('Manager', 'Admin') NOT NULL,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Media(
    media_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    rent_price INTEGER NOT NULL,
    image_url VARCHAR(1023) NOT NULL,
    media_description VARCHAR(9999) NOT NULL,
    release_date DATE NOT NULL,
    rating VARCHAR(255)
);

CREATE TABLE Video_Game(
    media_id INTEGER PRIMARY KEY,
    publisher VARCHAR(255) NOT NULL,
    developer VARCHAR(255) NOT NULL,
    FOREIGN KEY(media_id) REFERENCES Media(media_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Film(
    media_id INTEGER,
    runtime INTEGER,
    director VARCHAR(255),
    PRIMARY KEY(media_id, runtime),
    FOREIGN KEY(media_id) REFERENCES Media(media_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Reviews(
    review_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)

CREATE TABLE ReviewContent(
    review_id INTEGER PRIMARY KEY,
    media_id INTEGER,
    publish_date DATE NOT NULL,
    content VARCHAR(500) NOT NULL,
    stars INTEGER NOT NULL,
    FOREIGN KEY(media_id) REFERENCES Media(media_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Inventory(
    media_id INTEGER PRIMARY KEY,
    rent_availability_status BOOLEAN NOT NULL,
    FOREIGN KEY(media_id) REFERENCES Media(media_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Transaction(
    transaction_id INTEGER AUTO_INCREMENT,
    user_id INTEGER,
    total_cost INTEGER NOT NULL,
    rent_duration INTEGER NOT NULL,
    PRIMARY KEY(transaction_id, user_id),
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Rented(
    transaction_id INTEGER,
    media_id INTEGER,
    PRIMARY KEY(transaction_id, media_id),
    FOREIGN KEY(transaction_id) REFERENCES Transaction(transaction_id),
    FOREIGN KEY(media_id) REFERENCES Media(media_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Cart(
    cart_id INTEGER AUTO_INCREMENT,
    user_id INTEGER,
    PRIMARY KEY(cart_id, user_id),
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE In_Cart(
    cart_id INTEGER,
    media_id INTEGER,
    PRIMARY KEY(cart_id, media_id),
    FOREIGN KEY(media_id) REFERENCES Media(media_id),
    FOREIGN KEY(cart_id) REFERENCES Cart(cart_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

