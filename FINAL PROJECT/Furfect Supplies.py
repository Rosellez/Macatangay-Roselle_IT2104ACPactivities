import sqlite3
from datetime import datetime

class Database:
    """Handles database connection and initialization."""

    def __init__(self, db_name="inventory_system.db"):
        # Initialize database connection with the provided or default database name
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.initialize_database()

    def initialize_database(self):
        """Sets up the database tables if they don't exist."""
        cursor = self.conn.cursor()

        # Create products table to store product details
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL,
                reorder_level INTEGER NOT NULL
            )
        """)

        # Create sales table to track sales records
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                sale_date TEXT,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        """)
        self.conn.commit()

    def get_connection(self):
        """Returns the active database connection."""
        return self.conn


class Product:
    """Represents a single product."""

    def __init__(self, name, category, price, stock, reorder_level):
        # Initialize product details
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.reorder_level = reorder_level


class InventoryManager:
    """Manages inventory-related operations."""

    def __init__(self, db):
        # Accept a Database instance for executing queries
        self.db = db

    #FOR ADDING PRODUCT/S
    def add_product(self, product):
        """Adds a new product to the inventory."""
        cursor = self.db.conn.cursor()
        cursor.execute("""
            INSERT INTO products (name, category, price, stock, reorder_level)
            VALUES (?, ?, ?, ?, ?)
        """, (product.name, product.category, product.price, product.stock, product.reorder_level))
        self.db.conn.commit()
        print(f"\n\t\t\t\tProduct '{product.name}' added successfully!")
        print("\t\t\t\t------------------------------------------")

    #FOR VIEWING INVENTORY
    def view_inventory(self):
        """Displays all products in the inventory."""
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        print("\n\n\t\t\t\t\t-------------------")
        print("\t\t\t\t\t     INVENTORY     ")
        print("\t\t\t\t\t-------------------")
        for product in products:
            id, name, category, price, stock, reorder_level = product
            low_stock = " (Low Stock)" if stock <= reorder_level else ""
            print(f"\t\tID: {id} | Name: {name} | Category: {category} | Price: P{price:.2f} | Stock: {stock}{low_stock}")

    #FOR REMOVING PRODUCT/S
    def remove_product(self, product_id):
        """Removes a product by ID."""
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        if not product:
            print("\n\t\t\t\tInvalid product ID.")
        else:
            confirm = input(f"\t\t\t\tSure to remove '{product[0]}'? (y/n): ").lower()
            if confirm == 'y':
                cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
                self.db.conn.commit()
                print(f"\n\t\t\t\tProduct '{product[0]}' has been ")
                print("\t\t\t\tremoved from inventory.")
            else:
                print("\n\t\t\t\tOperation canceled.")
        print("\t\t\t\t------------------------------------------")

    #FOR UPDATING PRODUCT STOCK/S
    def update_stock(self, product_id, quantity):
        """Updates the stock of a product."""
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name, stock FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()
        if not product:
            print("\n\t\t\t\tInvalid product ID.")
        else:
            name, current_stock = product
            new_stock = current_stock + quantity
            cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
            self.db.conn.commit()
            print(f"\n\t\t\t\tStock for '{name}' updated to {new_stock}.")
            print("\t\t\t\t------------------------------------------")


class SalesManager:
    """Handles sales operations."""

    def __init__(self, db):
        # Accept a Database instance for executing queries
        self.db = db

    #FOR PURCHASING PRODUCT/S
    def purchase_products(self):
        """Facilitates the purchase process for customers."""
        cursor = self.db.conn.cursor()

        # Show inventory to the customer
        print("\n\n\t\t\t\t\tAvailable Products:")
        InventoryManager(self.db).view_inventory()

        # Initialize an empty cart
        cart = []

        while True:
            print("\n\t\t\t\t------------------------------------------")
            product_id = int(input("\t\t\t\tID to purchase (0 to checkout): "))
            if product_id == 0:  # Exit the loop when the customer finishes adding items
                break

            cursor.execute("SELECT name, stock, price FROM products WHERE id = ?", (product_id,))
            product = cursor.fetchone()

            if not product:
                print("\n\t\t\t\tInvalid product ID.")
                print("\t\t\t\t------------------------------------------")
            else:
                name, stock, price = product
                quantity = int(input(f"\t\t\t\tQuantity for '{name}': "))

                if quantity > stock:
                    # Warn if requested quantity exceeds available stock.
                    print("\n\t\t\t\tInsufficient stock for this purchase.")
                    print("\t\t\t\t------------------------------------------")
                else:
                    # Add valid items to the cart.
                    cart.append((product_id, name, quantity, price))

        if not cart:
            print("\n\t\t\t\tYour cart is empty.")
            print("\t\t\t\tReturning to the main menu.")
            print("\t\t\t\t------------------------------------------")
            return  # Exit the method if cart is empty

        # Calculate total price and display cart summary
        print("\n\n\t\t\t\t\t-----------------")
        print("\t\t\t\t\t      CART     ")
        print("\t\t\t\t\t-----------------")
        total_price = 0
        for item in cart:
            product_id, name, quantity, price = item
            item_total = quantity * price
            total_price += item_total
            print(f"\t\t\t\t\t'{name}'")
            print(f"\t\t\t\t\tQuantity: {quantity}x")
            print(f"\t\t\t\t\tUnit Price: P{price:.2f}")
            print(f"\t\t\t\t\tItem Total: P{item_total:.2f}")

        print(f"\n\t\t\t\t\tTotal Amount: P{total_price:.2f}")
        print("\n\n\t\t\t\t1. Proceed to Checkout") # Display checkout option
        print("\t\t\t\t2. Cancel Transaction") # Display cancel option
        checkout_choice = input("\t\t\t\tEnter your choice: ")

        if checkout_choice == "1":
            # Process payment
            payment = float(input("\t\t\t\tEnter payment amount: "))
            if payment < total_price:
                print("\n\t\t\t\tInsufficient payment. Transaction canceled.")
                print("\t\t\t\tReturning to the main menu...")
                print("\t\t\t\t------------------------------------------")
            else:
                # Calculate and display change
                change = payment - total_price
                print(f"\n\t\t\t\tPurchase successful! Change: P{change:.2f}")
                print("\t\t\t\tAll items purchased successfully!")
                print("\t\t\t\t------------------------------------------")

                # Update stock levels and record sales
                for item in cart:
                    product_id, _, quantity, price = item
                    cursor.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (quantity, product_id))
                    sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cursor.execute("""
                        INSERT INTO sales (product_id, quantity, total_price, sale_date)
                        VALUES (?, ?, ?, ?)
                    """, (product_id, quantity, quantity * price, sale_date))

                self.db.conn.commit()
        else:
            print("\n\t\t\t\tTransaction canceled.")
            print("\t\t\t\tReturning to the main menu...")
            print("\t\t\t\t------------------------------------------")

    #FOR VIEWING SALES OF SOLD PRODUCT/S
    def view_sales(self):
        """Displays all recorded sales."""
        cursor = self.db.conn.cursor()
        cursor.execute("""
            SELECT s.id, p.name, s.quantity, s.total_price, s.sale_date
            FROM sales s
            JOIN products p ON s.product_id = p.id
        """)
        sales = cursor.fetchall()
        print("\n\n\t\t\t\t\t-------------------")
        print("\t\t\t\t\t       SALES      ")
        print("\t\t\t\t\t-------------------")
        for sale in sales:
            id, name, quantity, total_price, sale_date = sale
            print(f"\tSale ID: {id} | Product: {name} | Quantity: {quantity} | Total: P{total_price:.2f} | Date: {sale_date}")


# Main Menu
def main_menu():
    """Provides the main user interface for the inventory and sales system."""
    db = Database()  # Initialize the database connection
    inventory = InventoryManager(db)  # Manage inventory operations
    sales = SalesManager(db)  # Manage sales operations

    print("\n\n\t\t\t\t******************************************")
    print("\t\t\t\t     Hi! Welcome to Furfect Supplies")
    print("\t\t\t\t    Our Pet Product Inventory System!")
    print("\t\t\t\t******************************************")
    print("\t\tThis system is designed to help pet product sellers efficiently manage their inventory,")
    print("\t\ttrack stock levels, and streamline their sales process. With Furfect Supplies, you can ")
    print("\tfocus on providing the best for your furry customers while keeping your business organized and thriving!")
    print("\t\t\t\t******************************************")

    while True:
        # Display the main menu
        print("\n\n\t\t\t\t=== Smart Inventory Management System ===\n")
        print("\t\t\t\t\t1. Add Product")
        print("\t\t\t\t\t2. View Inventory")
        print("\t\t\t\t\t3. Remove Product")
        print("\t\t\t\t\t4. Update Stock")
        print("\t\t\t\t\t5. Purchase Products")
        print("\t\t\t\t\t6. View Sales")
        print("\t\t\t\t\t7. Exit")
        print("\n\t\t\t\t==========================================")

        # Prompt the user for their choice
        choice = input("\n\t\t\t\tEnter your choice: ")

        if choice == "1":
            # to input in adding a new product
            print("\n\t\t\t\t------------------------------------------")
            name = input("\t\t\t\tEnter product name: ")
            category = input("\t\t\t\tEnter product category: ")
            price = float(input("\t\t\t\tEnter product price: "))
            stock = int(input("\t\t\t\tEnter initial stock: "))
            reorder_level = int(input("\t\t\t\tEnter reorder level: "))
            product = Product(name, category, price, stock, reorder_level)
            inventory.add_product(product)

        elif choice == "2":
            # View the inventory
            inventory.view_inventory()

        elif choice == "3":
            # Remove a product by ID
            inventory.view_inventory()
            print("\n\n\t\t\t\t------------------------------------------")
            product_id = int(input("\t\t\t\tEnter the product ID to remove: "))
            inventory.remove_product(product_id)

        elif choice == "4":
            # Update stock for a product
            inventory.view_inventory()
            print("\n\n\t\t\t\t------------------------------------------")
            product_id = int(input("\t\t\t\tEnter the product ID to update stock: "))
            quantity = int(input("\t\t\t\tEnter the quantity to add: "))
            inventory.update_stock(product_id, quantity)

        elif choice == "5":
            # Process a customer purchase
            sales.purchase_products()

        elif choice == "6":
            # View all sales records
            sales.view_sales()

        elif choice == "7":
            # Exit the program
            print("\n\t\t\t\tExiting the system. Goodbye!")
            db.conn.close()
            break
        else:
            print("\n\t\t\t\tInvalid choice! Please try again.")
            

# Run the program
if __name__ == "__main__":
    main_menu()
