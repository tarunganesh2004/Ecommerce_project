CREATE TABLE User (
    user_id INTEGER PRIMARY KEY,
    ph_no TEXT NOT NULL,
    address TEXT,
    name TEXT NOT NULL,
    date_of_birth TEXT,
    age INTEGER,
    password TEXT NOT NULL
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
);

CREATE TABLE Cart (
    user_id INTEGER,
    product_id INTEGER,
    product_name TEXT NOT NULL,
    cart_total REAL NOT NULL,
    PRIMARY KEY (user_id, product_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    product_name TEXT NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Supplier (
    supplier_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    product_name TEXT NOT NULL,
    contact_info TEXT,
    supplier_address TEXT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Category (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE Wish_List (
    user_id INTEGER,
    product_id INTEGER,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    PRIMARY KEY (user_id, product_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Reviews (
    review_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    user_id INTEGER,
    rating INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE Payments (
    payment_id INTEGER PRIMARY KEY,
    amount REAL NOT NULL,
    payment_methods TEXT NOT NULL,
    order_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);