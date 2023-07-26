CREATE TABLE User(
    user_id INTEGER PRIMARY KEY AUTO INCREMENT,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birthday date NOT NULL,
    profile_pic_URL VARCHAR(1023) NOT NULL,
    age INTEGER NOT NULL
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
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

CREATE TABLE Email(
    user_id INTEGER NOT NULL,
    email VARCHAR(1023) PRIMARY KEY,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

CREATE TABLE Phone_Number(
    user_id INTEGER NOT NULL,
    phone_number INTEGER PRIMARY KEY,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

CREATE TABLE Employee(
    user_id INTEGER NOT NULL,
    ssn INTEGER PRIMARY KEY,
    employee_type ENUM('Manager', 'Admin') NOT NULL,
    FOREIGN KEY(user_id) REFERENCES User(user_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

-- CREATE TABLE Manager(
--     ssn INTEGER PRIMARY KEY,
--     FOREIGN KEY(ssn) REFERENCES Employee(ssn),
--     ON DELETE CASCADE,
--     ON UPDATE CASCADE
-- );

-- CREATE TABLE Admin(
--     ssn INTEGER PRIMARY KEY,
--     FOREIGN KEY(ssn) REFERENCES Employee(ssn),
--     ON DELETE CASCADE,
--     ON UPDATE CASCADE
-- );

CREATE TABLE Media(
    media_id INTEGER PRIMARY KEY AUTO INCREMENT,
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
    FOREIGN KEY(media_id) REFERENCES Media(media_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

CREATE TABLE Film(
    media_id INTEGER,
    runtime INTEGER,
    director VARCHAR(255),
    PRIMARY KEY(media_id, runtime),
    FOREIGN KEY(media_id) REFERENCES Media(media_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

CREATE TABLE Review(
    review_id INTEGER AUTO INCREMENT,
    user_id INTEGER,
    media_id INTEGER,
    publish_date DATE NOT NULL,
    content VARCHAR(9999) NOT NULL,
    starts INTEGER NOT NULL,
    PRIMARY KEY(review_id, user_id, media_id),
    FOREIGN KEY(user_id) REFERENCES User(user_id),
    FOREIGN KEY(media_id) REFERENCES Media(media_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

CREATE TABLE Inventory(
    rental_id INTEGER AUTO INCREMENT,
    media_id INTEGER,
    rent_availability_status BOOLEAN NOT NULL,
    PRIMARY KEY(rental_id, media_id),
    FOREIGN KEY(media_id) REFERENCES Media(media_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

CREATE TABLE Transaction(
    transaction_id INTEGER AUTO INCREMENT,
    user_id INTEGER,
    rental_id INTEGER NOT NULL,
    total_cost INTEGER NOT NULL,
    rent_duration INTEGER NOT NULL,
    PRIMARY KEY(transaction_id, user_id),
    FOREIGN KEY(user_id) REFERENCES User(user_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

--Who owns the cart
CREATE TABLE Cart(
    cart_id INTEGER AUTO INCREMENT,
    user_id INTEGER,
    PRIMARY KEY(cart_id, user_id),
    FOREIGN KEY(user_id) REFERENCES User(user_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

--Whats in the cart
CREATE TABLE In_Cart(
    cart_id INTEGER,
    rental_id INTEGER,
    PRIMARY KEY(cart_id, rental_id),
    FOREIGN KEY(rental_id) REFERENCES Inventory(rental_id),
    FOREIGN KEY(cart_id) REFERENCES Cart(cart_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);

CREATE TABLE Customer(
    user_id INTEGER,
    PRIMARY KEY(user_id),
    FOREIGN KEY(user_id) REFERENCES User(user_id),
    ON DELETE CASCADE,
    ON UPDATE CASCADE
);