import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("ecommerce.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS User (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ph_no TEXT,
            address TEXT,
            name TEXT,
            date_of_birth TEXT,
            age INTEGER,
            password TEXT
        )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Product (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            quantity INTEGER
        )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            price REAL,
            quantity INTEGER,
            product_name TEXT,
            order_date TEXT,
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Review (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            user_id INTEGER,
            rating INTEGER,
            FOREIGN KEY (product_id) REFERENCES Product(product_id),
            FOREIGN KEY (user_id) REFERENCES User(user_id)
        )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Wishlist (
            wishlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product_id INTEGER,
            product_name TEXT,
            quantity INTEGER,
            FOREIGN KEY (user_id) REFERENCES User(user_id),
            FOREIGN KEY (product_id) REFERENCES Product(product_id)
        )""")
        self.conn.commit()

    def add_product(self, name, price, quantity):
        self.cursor.execute(
            "INSERT INTO Product (name, price, quantity) VALUES (?, ?, ?)",
            (name, price, quantity),
        )
        self.conn.commit()

    def add_order(self, user_id, price, quantity, product_name, order_date):
        self.cursor.execute(
            "INSERT INTO Orders (user_id, price, quantity, product_name, order_date) VALUES (?, ?, ?, ?, ?)",
            (user_id, price, quantity, product_name, order_date),
        )
        self.conn.commit()

    def add_review(self, product_id, user_id, rating):
        self.cursor.execute(
            "INSERT INTO Review (product_id, user_id, rating) VALUES (?, ?, ?)",
            (product_id, user_id, rating),
        )
        self.conn.commit()

    def add_to_wishlist(self, user_id, product_id, product_name, quantity):
        self.cursor.execute(
            "INSERT INTO Wishlist (user_id, product_id, product_name, quantity) VALUES (?, ?, ?, ?)",
            (user_id, product_id, product_name, quantity),
        )
        self.conn.commit()

    def get_products(self):
        self.cursor.execute("SELECT * FROM Product")
        return self.cursor.fetchall()

    def update_product(self, product_id, name, price, quantity):
        self.cursor.execute(
            "UPDATE Product SET name = ?, price = ?, quantity = ? WHERE product_id = ?",
            (name, price, quantity, product_id),
        )
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM Product WHERE product_id = ?", (product_id,))
        self.conn.commit()

    def get_orders(self, user_id):
        self.cursor.execute("SELECT * FROM Orders WHERE user_id = ?", (user_id,))
        return self.cursor.fetchall()

    def get_reviews(self, user_id):
        self.cursor.execute("SELECT * FROM Review WHERE user_id = ?", (user_id,))
        return self.cursor.fetchall()

    def get_wishlist(self, user_id):
        self.cursor.execute("SELECT * FROM Wishlist WHERE user_id = ?", (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
