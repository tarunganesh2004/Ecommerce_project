import tkinter as tk
from tkinter import messagebox


class UIManager:
    def __init__(self, app):
        self.app = app
        self.content_widgets = []

    def clear_content(self):
        for widget in self.content_widgets:
            if isinstance(widget, int):  # Canvas text or window IDs
                self.app.canvas.delete(widget)
            else:  # Tkinter widgets
                widget.destroy()
        self.content_widgets = []

    def create_horizontal_menu(self):
        # Products Menu
        products_menu = tk.Menubutton(
            self.app.menu_frame,
            text="Products",
            font=("Arial", 12),
            fg="white",
            bg="#333",
            relief="flat",
        )
        products_menu.pack(side="left", padx=10)
        products_submenu = tk.Menu(products_menu, tearoff=0)
        products_menu.config(menu=products_submenu)
        products_submenu.add_command(label="Add Product", command=self.show_add_product)
        products_submenu.add_command(
            label="View Products", command=self.show_view_products
        )
        products_submenu.add_command(
            label="Update Product", command=self.show_update_product
        )
        products_submenu.add_command(
            label="Delete Product", command=self.show_delete_product
        )

        # Orders Menu
        orders_menu = tk.Menubutton(
            self.app.menu_frame,
            text="Orders",
            font=("Arial", 12),
            fg="white",
            bg="#333",
            relief="flat",
        )
        orders_menu.pack(side="left", padx=10)
        orders_submenu = tk.Menu(orders_menu, tearoff=0)
        orders_menu.config(menu=orders_submenu)
        orders_submenu.add_command(label="Place Order", command=self.show_place_order)
        orders_submenu.add_command(label="View Orders", command=self.show_view_orders)

        # Reviews Menu
        reviews_menu = tk.Menubutton(
            self.app.menu_frame,
            text="Reviews",
            font=("Arial", 12),
            fg="white",
            bg="#333",
            relief="flat",
        )
        reviews_menu.pack(side="left", padx=10)
        reviews_submenu = tk.Menu(reviews_menu, tearoff=0)
        reviews_menu.config(menu=reviews_submenu)
        reviews_submenu.add_command(label="Add Review", command=self.show_add_review)
        reviews_submenu.add_command(
            label="View Reviews", command=self.show_view_reviews
        )

        # Wishlist Menu
        wishlist_menu = tk.Menubutton(
            self.app.menu_frame,
            text="Wishlist",
            font=("Arial", 12),
            fg="white",
            bg="#333",
            relief="flat",
        )
        wishlist_menu.pack(side="left", padx=10)
        wishlist_submenu = tk.Menu(wishlist_menu, tearoff=0)
        wishlist_menu.config(menu=wishlist_submenu)
        wishlist_submenu.add_command(
            label="Add to Wishlist", command=self.show_add_to_wishlist
        )
        wishlist_submenu.add_command(
            label="View Wishlist", command=self.show_view_wishlist
        )

    def show_login_screen(self):
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        # Login widgets directly on canvas
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="Login",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="User ID:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.login_user_id = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.login_user_id)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.app.login_user_id, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Password:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.login_password = tk.Entry(self.app.root, show="*")
        self.content_widgets.append(self.app.login_password)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.app.login_password, width=200
            )
        )

        login_btn = tk.Button(
            self.app.root, text="Login", command=self.app.actions.login
        )
        self.content_widgets.append(login_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 250, window=login_btn)
        )

        create_btn = tk.Button(
            self.app.root, text="Create Account", command=self.show_create_account
        )
        self.content_widgets.append(create_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 300, window=create_btn)
        )

    def show_create_account(self):
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="Create Account",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.create_name = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.create_name)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.app.create_name, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Phone Number:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.create_phone = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.create_phone)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.app.create_phone, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                250,
                text="Address:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.create_address = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.create_address)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 250, window=self.app.create_address, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                300,
                text="Date of Birth (YYYY-MM-DD):",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.create_dob = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.create_dob)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 300, window=self.app.create_dob, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                350,
                text="Age:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.create_age = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.create_age)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 350, window=self.app.create_age, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                400,
                text="Password:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.create_password = tk.Entry(self.app.root, show="*")
        self.content_widgets.append(self.app.create_password)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 400, window=self.app.create_password, width=200
            )
        )

        create_btn = tk.Button(
            self.app.root, text="Create", command=self.app.actions.create_account
        )
        self.content_widgets.append(create_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 450, window=create_btn)
        )

        back_btn = tk.Button(
            self.app.root, text="Back to Login", command=self.show_login_screen
        )
        self.content_widgets.append(back_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 500, window=back_btn)
        )

    def show_add_product(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="Add Product",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Product Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.prod_name = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.prod_name)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.app.prod_name, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Price:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.prod_price = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.prod_price)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.app.prod_price, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                250,
                text="Quantity:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.prod_quant = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.prod_quant)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 250, window=self.app.prod_quant, width=200
            )
        )

        add_btn = tk.Button(
            self.app.root, text="Add Product", command=self.app.actions.add_product
        )
        self.content_widgets.append(add_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 300, window=add_btn)
        )

    def show_view_products(self):
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="View Products",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )

        products = self.app.db.get_products()
        text_widget = tk.Text(self.app.root, height=20, width=80, font=("Arial", 12))
        text_widget.insert(tk.END, "ID\tName\tPrice\tQuantity\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")
        for product in products:
            text_widget.insert(
                tk.END, f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}\n"
            )
        text_widget.config(state="disabled")
        self.content_widgets.append(text_widget)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 350, window=text_widget)
        )

    def show_update_product(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="Update Product",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )

        # Display current products
        products = self.app.db.get_products()
        text_widget = tk.Text(self.app.root, height=5, width=80, font=("Arial", 12))
        text_widget.insert(tk.END, "ID\tName\tPrice\tQuantity\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")
        for product in products:
            text_widget.insert(
                tk.END, f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}\n"
            )
        text_widget.config(state="disabled")
        self.content_widgets.append(text_widget)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 200, window=text_widget)
        )

        # Input fields for updating
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                300,
                text="Product ID:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.update_prod_id = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.update_prod_id)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 300, window=self.app.update_prod_id, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                350,
                text="New Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.update_prod_name = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.update_prod_name)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 350, window=self.app.update_prod_name, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                400,
                text="New Price:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.update_prod_price = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.update_prod_price)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50,
                400,
                window=self.app.update_prod_price,
                width=200,
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                450,
                text="New Quantity:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.update_prod_quant = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.update_prod_quant)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50,
                450,
                window=self.app.update_prod_quant,
                width=200,
            )
        )

        update_btn = tk.Button(
            self.app.root,
            text="Update Product",
            command=self.app.actions.update_product,
        )
        self.content_widgets.append(update_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 500, window=update_btn)
        )

    def show_delete_product(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="Delete Product",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )

        # Display current products
        products = self.app.db.get_products()
        text_widget = tk.Text(self.app.root, height=5, width=80, font=("Arial", 12))
        text_widget.insert(tk.END, "ID\tName\tPrice\tQuantity\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")
        for product in products:
            text_widget.insert(
                tk.END, f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}\n"
            )
        text_widget.config(state="disabled")
        self.content_widgets.append(text_widget)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 200, window=text_widget)
        )

        # Input field for deletion
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                300,
                text="Product ID to Delete:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.delete_prod_id = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.delete_prod_id)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 300, window=self.app.delete_prod_id, width=200
            )
        )

        delete_btn = tk.Button(
            self.app.root,
            text="Delete Product",
            command=self.app.actions.delete_product,
        )
        self.content_widgets.append(delete_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 350, window=delete_btn)
        )

    def show_place_order(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="Place Order",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Price:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.order_price = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.order_price)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.app.order_price, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Quantity:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.order_quant = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.order_quant)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.app.order_quant, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                250,
                text="Product Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.order_prod = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.order_prod)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 250, window=self.app.order_prod, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                300,
                text="Order Date (YYYY-MM-DD):",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.order_date = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.order_date)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 300, window=self.app.order_date, width=200
            )
        )

        order_btn = tk.Button(
            self.app.root, text="Place Order", command=self.app.actions.add_order
        )
        self.content_widgets.append(order_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 350, window=order_btn)
        )

    def show_view_orders(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="View Orders",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )

        orders = self.app.db.get_orders(self.app.current_user_id)
        text_widget = tk.Text(self.app.root, height=20, width=80, font=("Arial", 12))
        text_widget.insert(
            tk.END, "Order ID\tUser ID\tPrice\tQuantity\tProduct Name\tOrder Date\n"
        )
        text_widget.insert(tk.END, "-" * 80 + "\n")
        for order in orders:
            text_widget.insert(
                tk.END,
                f"{order[0]}\t{order[1]}\t{order[2]}\t{order[3]}\t{order[4]}\t{order[5]}\n",
            )
        text_widget.config(state="disabled")
        self.content_widgets.append(text_widget)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 350, window=text_widget)
        )

    def show_add_review(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="Add Review",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Product ID:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.rev_prod = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.rev_prod)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.app.rev_prod, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Rating (1-5):",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.rev_rating = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.rev_rating)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.app.rev_rating, width=200
            )
        )

        review_btn = tk.Button(
            self.app.root, text="Add Review", command=self.app.actions.add_review
        )
        self.content_widgets.append(review_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 250, window=review_btn)
        )

    def show_view_reviews(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="View Reviews",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )

        reviews = self.app.db.get_reviews(self.app.current_user_id)
        text_widget = tk.Text(self.app.root, height=20, width=80, font=("Arial", 12))
        text_widget.insert(tk.END, "Review ID\tProduct ID\tUser ID\tRating\n")
        text_widget.insert(tk.END, "-" * 50 + "\n")
        for review in reviews:
            text_widget.insert(
                tk.END, f"{review[0]}\t{review[1]}\t{review[2]}\t{review[3]}\n"
            )
        text_widget.config(state="disabled")
        self.content_widgets.append(text_widget)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 350, window=text_widget)
        )

    def show_add_to_wishlist(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="Add to Wishlist",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Product ID:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.wish_prod = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.wish_prod)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.app.wish_prod, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Product Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.wish_name = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.wish_name)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.app.wish_name, width=200
            )
        )

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2 - 100,
                250,
                text="Quantity:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.app.wish_quant = tk.Entry(self.app.root)
        self.content_widgets.append(self.app.wish_quant)
        self.content_widgets.append(
            self.app.canvas.create_window(
                screen_width // 2 + 50, 250, window=self.app.wish_quant, width=200
            )
        )

        wish_btn = tk.Button(
            self.app.root,
            text="Add to Wishlist",
            command=self.app.actions.add_to_wishlist,
        )
        self.content_widgets.append(wish_btn)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 300, window=wish_btn)
        )

    def show_view_wishlist(self):
        if not self.app.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.app.root.winfo_screenwidth()

        self.content_widgets.append(
            self.app.canvas.create_text(
                screen_width // 2,
                100,
                text="View Wishlist",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )

        wishlist = self.app.db.get_wishlist(self.app.current_user_id)
        text_widget = tk.Text(self.app.root, height=20, width=80, font=("Arial", 12))
        text_widget.insert(
            tk.END, "Wishlist ID\tUser ID\tProduct ID\tProduct Name\tQuantity\n"
        )
        text_widget.insert(tk.END, "-" * 80 + "\n")
        for item in wishlist:
            text_widget.insert(
                tk.END, f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\t{item[4]}\n"
            )
        text_widget.config(state="disabled")
        self.content_widgets.append(text_widget)
        self.content_widgets.append(
            self.app.canvas.create_window(screen_width // 2, 350, window=text_widget)
        )
