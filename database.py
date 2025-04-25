import sqlite3

class Database:
    def __init__(self, db_name="ecommerce.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        with open('schema.sql', 'r') as file:
            sql_script = file.read()
        self.cursor.executescript(sql_script)
        self.conn.commit()

    def add_product(self, product_name, price, quantity):
        self.cursor.execute("INSERT INTO Products (product_name, price, quantity) VALUES (?, ?, ?)",
                           (product_name, price, quantity))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_order(self, user_id, price, quantity, product_name, order_date):
        self.cursor.execute("INSERT INTO Orders (user_id, price, quantity, product_name, order_date) VALUES (?, ?, ?, ?, ?)",
                           (user_id, price, quantity, product_name, order_date))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_review(self, product_id, user_id, rating):
        self.cursor.execute("INSERT INTO Reviews (product_id, user_id, rating) VALUES (?, ?, ?)",
                           (product_id, user_id, rating))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_to_wishlist(self, user_id, product_id, product_name, quantity):
        self.cursor.execute("INSERT INTO Wish_List (user_id, product_id, product_name, quantity) VALUES (?, ?, ?, ?)",
                           (user_id, product_id, product_name, quantity))
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.conn.close()

# Example usage (uncomment to test)
if __name__ == "__main__":
    db = Database()
    db.add_product("Sample Product", 99.99, 10)
    db.close()