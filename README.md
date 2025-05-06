# Ecommerce Project

## Project Overview

The Ecommerce Project is a desktop application designed to simulate a fully functional online shopping platform. Built using Python, this application leverages Tkinter for the graphical user interface (GUI), SQLite for persistent data storage, and Pillow for image handling. The project aims to provide a seamless shopping experience for users while offering administrators the tools to manage products, orders, and other entities. It is an excellent demonstration of a full-stack application with a focus on user authentication, product management, order processing, and database integration.

### Idea Behind the Project

The primary idea behind this project is to create a user-friendly e-commerce platform that allows customers to browse products, place orders, manage their accounts, and leave reviews, while administrators can oversee inventory, suppliers, and payments. This project was inspired by the growing trend of online shopping and the need for small businesses to have accessible, customizable e-commerce solutions. It serves as a practical learning tool for understanding GUI development, database management, and application packaging, making it a valuable addition to a developer's portfolio.

## Features

- **User Authentication**:
  - Register with personal details (name, phone number, address, date of birth, age, password).
  - Login using a unique user ID and password.
- **Product Management**:
  - Add, view, update, and delete products with details like name, price, quantity, category, and supplier.
- **Order Management**:
  - Place orders with details such as price, quantity, product name, and order date.
  - View orders specific to the logged-in user.
- **Review System**:
  - Submit product reviews with ratings (1-5).
  - View reviews submitted by the logged-in user.
- **Wishlist**:
  - Add products to a wishlist for future reference.
  - View wishlist items specific to the logged-in user.
- **Supplier and Category Management**:
  - Add and view suppliers and categories with relevant details.
- **Payment Tracking**:
  - Record payments linked to orders (amount, payment method, order ID).
  - View all payments.
- **GUI**:
  - Intuitive Tkinter-based interface with a background image (`ecommerce_image.jpg`) for enhanced aesthetics.
- **Database**:
  - SQLite database (`ecommerce.db`) for persistent storage of all data.

## Tech Stack

- **Python**: Core programming language for the application.
- **Tkinter**: Used for creating the graphical user interface.
- **SQLite**: Lightweight database for storing user data, products, orders, and more.
- **Pillow (PIL)**: For handling and displaying the background image in the GUI.
- **PyInstaller**: For packaging the application into a standalone `.exe` file for Windows.

## Project Structure

```
Ecommerce_project/
│
├── main.py             # Entry point of the application
├── database.py         # Handles SQLite database operations
├── ui_manager.py       # Manages the Tkinter GUI components
├── actions.py          # Contains logic for user actions (e.g., login, add product)
├── ecommerce_image.jpg # Background image for the GUI
├── ecommerce.db        # SQLite database file (created on first run)
└── README.md           # Project documentation
```

## Installation

### Prerequisites

- **Python 3.6 or higher**: Ensure Python is installed on your system.
- **Pillow Library**: Required for image handling.
- **Operating System**: Tested on Windows, but compatible with macOS and Linux with minor adjustments.

### Steps

1. **Clone the Repository**:

   - Clone the project from GitHub:

     ```
     git clone https://github.com/tarunganesh2004/Ecommerce_project.git
     ```
   - Navigate to the project directory:

     ```
     cd Ecommerce_project
     ```

2. **Install Dependencies**:

   - Install the required Python libraries:

     ```
     pip install Pillow
     ```
   - Tkinter and SQLite are included with Python, so no additional installation is needed for them.

3. **Run the Application**:

   - Execute the main script:

     ```
     python main.py
     ```
   - The application window will open, displaying the login screen.

## Usage

1. **Account Creation**:

   - On the login screen, click "Create Account".
   - Fill in your details (name, phone number, address, date of birth, age, password).
   - Submit the form to create an account. Note the user ID generated for login.

2. **Login**:

   - Use your user ID and password to log in.
   - Upon successful login, you’ll be taken to the main application interface.

3. **Browse and Manage Products**:

   - Navigate to the "Products" menu to add, view, update, or delete products.
   - Ensure you have category and supplier IDs when adding or updating products.

4. **Place Orders**:

   - Go to the "Orders" menu, select "Place Order", and enter order details.
   - Note the order ID for tracking or payment purposes.

5. **Manage Reviews, Wishlist, Suppliers, Categories, and Payments**:

   - Use the respective menus to add, view, or manage reviews, wishlist items, suppliers, categories, and payments.

## Database

- **File**: `ecommerce.db` (SQLite database file, created automatically on first run).
- **Location**: Stored in the project directory (or the directory of the `.exe` if using the executable).
- **Tables**:
  - `User`: Stores user details.
  - `Product`: Stores product information.
  - `Orders`: Stores order details.
  - `Review`: Stores product reviews.
  - `Wishlist`: Stores wishlist items.
  - `Supplier`: Stores supplier details.
  - `Category`: Stores category information.
  - `Payments`: Stores payment records.

### Viewing the Database

To view or edit the database:

1. **Use DB Browser for SQLite**:
   - Download and install DB Browser for SQLite from https://sqlitebrowser.org/.
   - Open `ecommerce.db` in DB Browser for SQLite.
   - Use the "Browse Data" tab to view table contents or the "Execute SQL" tab to run custom queries.
2. **Use SQLite Command-Line Tool**:
   - Download SQLite tools from https://www.sqlite.org/download.html.
   - Run `sqlite3 ecommerce.db` in a terminal and use commands like `.tables` and `SELECT * FROM Product;` to explore the data.

## Converting to a Standalone Executable (.exe)

You can package the application into a standalone `.exe` file for Windows using PyInstaller.

### Steps

1. **Install PyInstaller**:

   ```
   pip install pyinstaller
   ```

2. **Run PyInstaller**:

   - Navigate to the project directory:

     ```
     cd path\to\Ecommerce_project
     ```
   - Run the following command:

     ```
     pyinstaller --onefile --add-data "ecommerce_image.jpg;." --name EcommerceApp main.py
     ```
     - On macOS/Linux, replace `;` with `:` in the `--add-data` option:

       ```
       pyinstaller --onefile --add-data "ecommerce_image.jpg:." --name EcommerceApp main.py
       ```

3. **Locate the Executable**:

   - The `EcommerceApp.exe` file will be created in the `dist` folder.

4. **Run the Executable**:

   - Navigate to the `dist` folder and run:

     ```
     EcommerceApp.exe
     ```

### Notes

- The `ecommerce.db` file will be created in the same directory as the `.exe` when you run it.
- If you have an existing `ecommerce.db` with data, place it in the same directory as the `.exe`.

## Uses of the Project

- **Educational Purpose**: Ideal for students learning Python, GUI development with Tkinter, and database management with SQLite.
- **Portfolio Project**: A great addition to a developer’s portfolio to showcase skills in full-stack application development.
- **Small Business Solution**: Can be adapted for small businesses to manage inventory, orders, and customer interactions.
- **Prototype for Larger Systems**: Serves as a prototype for more complex e-commerce platforms that can be scaled with additional features like online payments or web deployment.

## Future Improvements

- **Input Validation**: Add robust validation for all user inputs to prevent errors.
- **Enhanced UI**: Improve the GUI with modern styling, animations, or a web-based frontend using frameworks like Django or Flask.
- **Payment Integration**: Integrate real payment gateways (e.g., Stripe, PayPal) for actual transactions.
- **Search and Filter**: Add search and filter options for products, orders, and other entities.
- **Admin Panel**: Create a dedicated admin panel with advanced controls for managing all aspects of the platform.
- **Cross-Platform Support**: Optimize the application for macOS and Linux, ensuring compatibility with different operating systems.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request with a detailed description of your changes.



## Contact

For questions, suggestions, or support, feel free to reach out:

- **GitHub**: tarunganesh2004
- **Email**: enstarunganesh@gmail.com

---

⭐ If you find this project helpful, please give it a star on GitHub! ⭐