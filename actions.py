import tkinter as tk
from tkinter import messagebox


class Actions:
    def __init__(self, app):
        self.app = app

    def add_product(self):
        product_name = self.app.prod_name.get()
        price = float(self.app.prod_price.get())
        quantity = int(self.app.prod_quant.get())
        category_id = (
            int(self.app.prod_category_id.get())
            if hasattr(self.app, "prod_category_id")
            else 1
        )
        supplier_id = (
            int(self.app.prod_supplier_id.get())
            if hasattr(self.app, "prod_supplier_id")
            else 1
        )
        product_id = self.app.db.add_product(
            product_name, price, quantity, category_id, supplier_id
        )
        messagebox.showinfo("Success", f"Product added with ID: {product_id}")
        self.app.prod_name.delete(0, tk.END)
        self.app.prod_price.delete(0, tk.END)
        self.app.prod_quant.delete(0, tk.END)
        if hasattr(self.app, "prod_category_id"):
            self.app.prod_category_id.delete(0, tk.END)
        if hasattr(self.app, "prod_supplier_id"):
            self.app.prod_supplier_id.delete(0, tk.END)

    def add_supplier(self):
        product_id = int(self.app.supplier_prod_id.get())
        product_name = self.app.supplier_prod_name.get()
        contact_info = self.app.supplier_contact.get()
        supplier_address = self.app.supplier_address.get()
        self.app.db.add_supplier(
            product_id, product_name, contact_info, supplier_address
        )
        messagebox.showinfo("Success", "Supplier added!")
        self.app.supplier_prod_id.delete(0, tk.END)
        self.app.supplier_prod_name.delete(0, tk.END)
        self.app.supplier_contact.delete(0, tk.END)
        self.app.supplier_address.delete(0, tk.END)

    def add_category(self):
        category_name = self.app.category_name.get()
        description = self.app.category_desc.get()
        category_id = self.app.db.add_category(category_name, description)
        messagebox.showinfo("Success", f"Category added with ID: {category_id}")
        self.app.category_name.delete(0, tk.END)
        self.app.category_desc.delete(0, tk.END)

    def add_payment(self):
        amount = float(self.app.payment_amount.get())
        payment_method = self.app.payment_method.get()
        order_id = int(self.app.payment_order_id.get())
        self.app.db.add_payment(amount, payment_method, order_id)
        messagebox.showinfo("Success", "Payment added!")
        self.app.payment_amount.delete(0, tk.END)
        self.app.payment_method.delete(0, tk.END)
        self.app.payment_order_id.delete(0, tk.END)

    def add_order(self):
        price = float(self.app.order_price.get())
        quantity = int(self.app.order_quant.get())
        product_name = self.app.order_prod.get()
        order_date = self.app.order_date.get()
        order_id = self.app.db.add_order(
            self.app.current_user_id, price, quantity, product_name, order_date
        )
        messagebox.showinfo("Success", f"Order placed with ID: {order_id}")
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
        category_id = (
            int(self.app.update_prod_category_id.get())
            if hasattr(self.app, "update_prod_category_id")
            else 1
        )
        supplier_id = (
            int(self.app.update_prod_supplier_id.get())
            if hasattr(self.app, "update_prod_supplier_id")
            else 1
        )
        self.app.db.update_product(
            product_id, name, price, quantity, category_id, supplier_id
        )
        messagebox.showinfo("Success", "Product updated!")
        self.app.ui_manager.show_update_product()

    def delete_product(self):
        product_id = int(self.app.delete_prod_id.get())
        self.app.db.delete_product(product_id)
        messagebox.showinfo("Success", "Product deleted!")
        self.app.ui_manager.show_delete_product()