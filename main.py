import tkinter as tk
from PIL import Image, ImageTk
from database import Database
from ui_manager import UIManager
from actions import Actions


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

        # Initialize UI manager and actions
        self.ui_manager = UIManager(self)
        self.actions = Actions(self)

        # Create horizontal menu
        self.ui_manager.create_horizontal_menu()

        # Show initial login screen
        self.ui_manager.show_login_screen()

    def on_closing(self):
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = EcommerceApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
