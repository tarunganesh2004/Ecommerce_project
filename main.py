import tkinter as tk
from tkinter import messagebox, ttk
from database import Database
from PIL import Image, ImageTk


class EcommerceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ecommerce App")
        self.db = Database()
        self.current_user_id = None

        # Maximize the window
        self.root.state("zoomed")

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Load and resize the background image
        self.image = Image.open("ecommerce_image.jpg")
        self.image = self.image.resize(
            (screen_width, screen_height), Image.Resampling.LANCZOS
        )
        self.bg_image = ImageTk.PhotoImage(self.image)

        # Main frame with background
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        # Canvas for background image
        self.canvas = tk.Canvas(
            self.main_frame, width=screen_width, height=screen_height
        )
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Horizontal menu frame at the top
        self.menu_frame = tk.Frame(self.main_frame, bg="#333")
        self.menu_frame.place(x=0, y=0, width=screen_width, height=50)

        # Horizontal menu options
        self.create_horizontal_menu()

        # Content area directly on the canvas
        self.content_widgets = []
        self.show_login_screen()

    def create_horizontal_menu(self):
        # Products Menu
        products_menu = tk.Menubutton(
            self.menu_frame,
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
            label="View Products",
            command=lambda: messagebox.showinfo(
                "Info", "View Products feature coming soon!"
            ),
        )
        products_submenu.add_command(
            label="Update Product",
            command=lambda: messagebox.showinfo(
                "Info", "Update Product feature coming soon!"
            ),
        )
        products_submenu.add_command(
            label="Delete Product",
            command=lambda: messagebox.showinfo(
                "Info", "Delete Product feature coming soon!"
            ),
        )

        # Orders Menu
        orders_menu = tk.Menubutton(
            self.menu_frame,
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
        orders_submenu.add_command(
            label="View Orders",
            command=lambda: messagebox.showinfo(
                "Info", "View Orders feature coming soon!"
            ),
        )

        # Reviews Menu
        reviews_menu = tk.Menubutton(
            self.menu_frame,
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
            label="View Reviews",
            command=lambda: messagebox.showinfo(
                "Info", "View Reviews feature coming soon!"
            ),
        )

        # Wishlist Menu
        wishlist_menu = tk.Menubutton(
            self.menu_frame,
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
            label="View Wishlist",
            command=lambda: messagebox.showinfo(
                "Info", "View Wishlist feature coming soon!"
            ),
        )

    def clear_content(self):
        for widget in self.content_widgets:
            if isinstance(widget, int):  # Canvas text or window IDs
                self.canvas.delete(widget)
            else:  # Tkinter widgets
                widget.destroy()
        self.content_widgets = []

    def show_login_screen(self):
        self.clear_content()
        screen_width = self.root.winfo_screenwidth()

        # Login widgets directly on canvas
        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2,
                100,
                text="Login",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="User ID:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.login_user_id = tk.Entry(self.root)
        self.content_widgets.append(self.login_user_id)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.login_user_id, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Password:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.login_password = tk.Entry(self.root, show="*")
        self.content_widgets.append(self.login_password)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.login_password, width=200
            )
        )

        login_btn = tk.Button(self.root, text="Login", command=self.login)
        self.content_widgets.append(login_btn)
        self.content_widgets.append(
            self.canvas.create_window(screen_width // 2, 250, window=login_btn)
        )

        create_btn = tk.Button(
            self.root, text="Create Account", command=self.show_create_account
        )
        self.content_widgets.append(create_btn)
        self.content_widgets.append(
            self.canvas.create_window(screen_width // 2, 300, window=create_btn)
        )

    def show_create_account(self):
        self.clear_content()
        screen_width = self.root.winfo_screenwidth()

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2,
                100,
                text="Create Account",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.create_name = tk.Entry(self.root)
        self.content_widgets.append(self.create_name)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.create_name, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Phone Number:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.create_phone = tk.Entry(self.root)
        self.content_widgets.append(self.create_phone)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.create_phone, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                250,
                text="Address:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.create_address = tk.Entry(self.root)
        self.content_widgets.append(self.create_address)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 250, window=self.create_address, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                300,
                text="Date of Birth (YYYY-MM-DD):",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.create_dob = tk.Entry(self.root)
        self.content_widgets.append(self.create_dob)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 300, window=self.create_dob, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                350,
                text="Age:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.create_age = tk.Entry(self.root)
        self.content_widgets.append(self.create_age)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 350, window=self.create_age, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                400,
                text="Password:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.create_password = tk.Entry(self.root, show="*")
        self.content_widgets.append(self.create_password)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 400, window=self.create_password, width=200
            )
        )

        create_btn = tk.Button(self.root, text="Create", command=self.create_account)
        self.content_widgets.append(create_btn)
        self.content_widgets.append(
            self.canvas.create_window(screen_width // 2, 450, window=create_btn)
        )

        back_btn = tk.Button(
            self.root, text="Back to Login", command=self.show_login_screen
        )
        self.content_widgets.append(back_btn)
        self.content_widgets.append(
            self.canvas.create_window(screen_width // 2, 500, window=back_btn)
        )

    def create_account(self):
        name = self.create_name.get()
        phone = self.create_phone.get()
        address = self.create_address.get()
        dob = self.create_dob.get()
        age = int(self.create_age.get())
        password = self.create_password.get()

        self.db.cursor.execute(
            "INSERT INTO User (ph_no, address, name, date_of_birth, age, password) VALUES (?, ?, ?, ?, ?, ?)",
            (phone, address, name, dob, age, password),
        )
        self.db.conn.commit()
        user_id = self.db.cursor.lastrowid
        messagebox.showinfo("Success", f"Account created! Your User ID is {user_id}")
        self.show_login_screen()

    def login(self):
        user_id = int(self.login_user_id.get())
        password = self.login_password.get()
        self.db.cursor.execute(
            "SELECT * FROM User WHERE user_id = ? AND password = ?", (user_id, password)
        )
        user = self.db.cursor.fetchone()
        if user:
            self.current_user_id = user_id
            messagebox.showinfo("Success", "Logged in successfully!")
            self.clear_content()
        else:
            messagebox.showerror("Error", "Invalid User ID or Password")

    def show_add_product(self):
        if not self.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.root.winfo_screenwidth()

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2,
                100,
                text="Add Product",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Product Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.prod_name = tk.Entry(self.root)
        self.content_widgets.append(self.prod_name)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.prod_name, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Price:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.prod_price = tk.Entry(self.root)
        self.content_widgets.append(self.prod_price)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.prod_price, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                250,
                text="Quantity:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.prod_quant = tk.Entry(self.root)
        self.content_widgets.append(self.prod_quant)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 250, window=self.prod_quant, width=200
            )
        )

        add_btn = tk.Button(self.root, text="Add Product", command=self.add_product)
        self.content_widgets.append(add_btn)
        self.content_widgets.append(
            self.canvas.create_window(screen_width // 2, 300, window=add_btn)
        )

    def show_place_order(self):
        if not self.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.root.winfo_screenwidth()

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2,
                100,
                text="Place Order",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Price:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.order_price = tk.Entry(self.root)
        self.content_widgets.append(self.order_price)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.order_price, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Quantity:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.order_quant = tk.Entry(self.root)
        self.content_widgets.append(self.order_quant)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.order_quant, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                250,
                text="Product Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.order_prod = tk.Entry(self.root)
        self.content_widgets.append(self.order_prod)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 250, window=self.order_prod, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                300,
                text="Order Date (YYYY-MM-DD):",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.order_date = tk.Entry(self.root)
        self.content_widgets.append(self.order_date)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 300, window=self.order_date, width=200
            )
        )

        order_btn = tk.Button(self.root, text="Place Order", command=self.add_order)
        self.content_widgets.append(order_btn)
        self.content_widgets.append(
            self.canvas.create_window(screen_width // 2, 350, window=order_btn)
        )

    def show_add_review(self):
        if not self.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.root.winfo_screenwidth()

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2,
                100,
                text="Add Review",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Product ID:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.rev_prod = tk.Entry(self.root)
        self.content_widgets.append(self.rev_prod)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.rev_prod, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Rating (1-5):",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.rev_rating = tk.Entry(self.root)
        self.content_widgets.append(self.rev_rating)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.rev_rating, width=200
            )
        )

        review_btn = tk.Button(self.root, text="Add Review", command=self.add_review)
        self.content_widgets.append(review_btn)
        self.content_widgets.append(
            self.canvas.create_window(screen_width // 2, 250, window=review_btn)
        )

    def show_add_to_wishlist(self):
        if not self.current_user_id:
            messagebox.showerror("Error", "Please login first!")
            return
        self.clear_content()
        screen_width = self.root.winfo_screenwidth()

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2,
                100,
                text="Add to Wishlist",
                font=("Arial", 16, "bold"),
                fill="yellow",
            )
        )
        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                150,
                text="Product ID:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.wish_prod = tk.Entry(self.root)
        self.content_widgets.append(self.wish_prod)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 150, window=self.wish_prod, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                200,
                text="Product Name:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.wish_name = tk.Entry(self.root)
        self.content_widgets.append(self.wish_name)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 200, window=self.wish_name, width=200
            )
        )

        self.content_widgets.append(
            self.canvas.create_text(
                screen_width // 2 - 100,
                250,
                text="Quantity:",
                font=("Arial", 12),
                fill="yellow",
                anchor="e",
            )
        )
        self.wish_quant = tk.Entry(self.root)
        self.content_widgets.append(self.wish_quant)
        self.content_widgets.append(
            self.canvas.create_window(
                screen_width // 2 + 50, 250, window=self.wish_quant, width=200
            )
        )

        wish_btn = tk.Button(
            self.root, text="Add to Wishlist", command=self.add_to_wishlist
        )
        self.content_widgets.append(wish_btn)
        self.content_widgets.append(
            self.canvas.create_window(screen_width // 2, 300, window=wish_btn)
        )

    def add_product(self):
        product_name = self.prod_name.get()
        price = float(self.prod_price.get())
        quantity = int(self.prod_quant.get())
        self.db.add_product(product_name, price, quantity)
        messagebox.showinfo("Success", "Product added!")
        self.prod_name.delete(0, tk.END)
        self.prod_price.delete(0, tk.END)
        self.prod_quant.delete(0, tk.END)

    def add_order(self):
        price = float(self.order_price.get())
        quantity = int(self.order_quant.get())
        product_name = self.order_prod.get()
        order_date = self.order_date.get()
        self.db.add_order(
            self.current_user_id, price, quantity, product_name, order_date
        )
        messagebox.showinfo("Success", "Order placed!")
        self.order_price.delete(0, tk.END)
        self.order_quant.delete(0, tk.END)
        self.order_prod.delete(0, tk.END)
        self.order_date.delete(0, tk.END)

    def add_review(self):
        product_id = int(self.rev_prod.get())
        rating = int(self.rev_rating.get())
        self.db.add_review(product_id, self.current_user_id, rating)
        messagebox.showinfo("Success", "Review added!")
        self.rev_prod.delete(0, tk.END)
        self.rev_rating.delete(0, tk.END)

    def add_to_wishlist(self):
        product_id = int(self.wish_prod.get())
        product_name = self.wish_name.get()
        quantity = int(self.wish_quant.get())
        self.db.add_to_wishlist(
            self.current_user_id, product_id, product_name, quantity
        )
        messagebox.showinfo("Success", "Added to wishlist!")
        self.wish_prod.delete(0, tk.END)
        self.wish_name.delete(0, tk.END)
        self.wish_quant.delete(0, tk.END)

    def on_closing(self):
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = EcommerceApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()