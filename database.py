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
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Supplier (
            supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            product_name TEXT,
            contact_info TEXT,
            supplier_address TEXT,
            FOREIGN KEY (product_id) REFERENCES Product(product_id)
        )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT,
            description TEXT
        )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            payment_method TEXT,
            order_id INTEGER,
            FOREIGN KEY (order_id) REFERENCES Orders(order_id)
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
        return self.cursor.lastrowid

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

    def add_supplier(self, product_id, product_name, contact_info, supplier_address):
        self.cursor.execute(
            "INSERT INTO Supplier (product_id, product_name, contact_info, supplier_address) VALUES (?, ?, ?, ?)",
            (product_id, product_name, contact_info, supplier_address),
        )
        self.conn.commit()

    def get_suppliers(self):
        self.cursor.execute("SELECT * FROM Supplier")
        return self.cursor.fetchall()

    def update_supplier(
        self, supplier_id, product_id, product_name, contact_info, supplier_address
    ):
        self.cursor.execute(
            "UPDATE Supplier SET product_id = ?, product_name = ?, contact_info = ?, supplier_address = ? WHERE supplier_id = ?",
            (product_id, product_name, contact_info, supplier_address, supplier_id),
        )
        self.conn.commit()

    def delete_supplier(self, supplier_id):
        self.cursor.execute(
            "DELETE FROM Supplier WHERE supplier_id = ?", (supplier_id,)
        )
        self.conn.commit()

    def add_category(self, category_name, description):
        self.cursor.execute(
            "INSERT INTO Category (category_name, description) VALUES (?, ?)",
            (category_name, description),
        )
        self.conn.commit()

    def get_categories(self):
        self.cursor.execute("SELECT * FROM Category")
        return self.cursor.fetchall()

    def update_category(self, category_id, category_name, description):
        self.cursor.execute(
            "UPDATE Category SET category_name = ?, description = ? WHERE category_id = ?",
            (category_name, description, category_id),
        )
        self.conn.commit()

    def delete_category(self, category_id):
        self.cursor.execute(
            "DELETE FROM Category WHERE category_id = ?", (category_id,)
        )
        self.conn.commit()

    def add_payment(self, amount, payment_method, order_id):
        self.cursor.execute(
            "INSERT INTO Payments (amount, payment_method, order_id) VALUES (?, ?, ?)",
            (amount, payment_method, order_id),
        )
        self.conn.commit()

    def get_payments(self, user_id):
        self.cursor.execute(
            "SELECT p.* FROM Payments p JOIN Orders o ON p.order_id = o.order_id WHERE o.user_id = ?",
            (user_id,),
        )
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
