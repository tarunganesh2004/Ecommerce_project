import tkinter as tk
from tkinter import messagebox


class Actions:
    def __init__(self, app):
        self.app = app

    def add_product(self):
        product_name = self.app.prod_name.get()
        price = float(self.app.prod_price.get())
        quantity = int(self.app.prod_quant.get())
        self.app.db.add_product(product_name, price, quantity)
        messagebox.showinfo("Success", "Product added!")
        self.app.prod_name.delete(0, tk.END)
        self.app.prod_price.delete(0, tk.END)
        self.app.prod_quant.delete(0, tk.END)

    def add_order(self):
        price = float(self.app.order_price.get())
        quantity = int(self.app.order_quant.get())
        product_name = self.app.order_prod.get()
        order_date = self.app.order_date.get()
        self.app.db.add_order(
            self.app.current_user_id, price, quantity, product_name, order_date
        )
        messagebox.showinfo("Success", "Order placed!")
        self.app.order_price.delete(0, tk.END)
        self.app.order_quant.delete(0, tk.END)
        self.app.order_prod.delete(0, tk.END)
        self.app.order_date.delete(0, tk.END)

    def add_review(self):
        product_id = int(self.app.rev_prod.get())
        rating = int(self.app.rev_rating.get())
        self.app.db.add_review(product_id, self.app.current_user_id, rating)
        messagebox.showinfo("Success", "Review added!")
        self.app.rev_prod.delete(0, tk.END)
        self.app.rev_rating.delete(0, tk.END)

    def add_to_wishlist(self):
        product_id = int(self.app.wish_prod.get())
        product_name = self.app.wish_name.get()
        quantity = int(self.app.wish_quant.get())
        self.app.db.add_to_wishlist(
            self.app.current_user_id, product_id, product_name, quantity
        )
        messagebox.showinfo("Success", "Added to wishlist!")
        self.app.wish_prod.delete(0, tk.END)
        self.app.wish_name.delete(0, tk.END)
        self.app.wish_quant.delete(0, tk.END)

    def create_account(self):
        name = self.app.create_name.get()
        phone = self.app.create_phone.get()
        address = self.app.create_address.get()
        dob = self.app.create_dob.get()
        age = int(self.app.create_age.get())
        password = self.app.create_password.get()

        self.app.db.cursor.execute(
            "INSERT INTO User (ph_no, address, name, date_of_birth, age, password) VALUES (?, ?, ?, ?, ?, ?)",
            (phone, address, name, dob, age, password),
        )
        self.app.db.conn.commit()
        user_id = self.app.db.cursor.lastrowid
        messagebox.showinfo("Success", f"Account created! Your User ID is {user_id}")
        self.app.ui_manager.show_login_screen()

    def login(self):
        user_id = int(self.app.login_user_id.get())
        password = self.app.login_password.get()
        self.app.db.cursor.execute(
            "SELECT * FROM User WHERE user_id = ? AND password = ?", (user_id, password)
        )
        user = self.app.db.cursor.fetchone()
        if user:
            self.app.current_user_id = user_id
            messagebox.showinfo("Success", "Logged in successfully!")
            self.app.ui_manager.clear_content()
        else:
            messagebox.showerror("Error", "Invalid User ID or Password")

    def update_product(self):
        product_id = int(self.app.update_prod_id.get())
        name = self.app.update_prod_name.get()
        price = float(self.app.update_prod_price.get())
        quantity = int(self.app.update_prod_quant.get())
        self.app.db.update_product(product_id, name, price, quantity)
        messagebox.showinfo("Success", "Product updated!")
        self.app.ui_manager.show_update_product()

    def delete_product(self):
        product_id = int(self.app.delete_prod_id.get())
        self.app.db.delete_product(product_id)
        messagebox.showinfo("Success", "Product deleted!")
        self.app.ui_manager.show_delete_product()
