import sqlite3
from datetime import datetime

# Database Initialization
def initialize_database():
    """
    Initializes the database by creating the required tables if they don't exist.
    This includes 'products' and 'sales' tables.
    """
    conn = sqlite3.connect("inventory_system.db")
    cursor = conn.cursor()

    # Create 'products' table to store product information.
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

    # Create 'sales' table to log details of each sale.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,  -- Links to the 'products' table
            quantity INTEGER,    -- Number of items sold
            total_price REAL,    -- Total revenue from this sale
            sale_date TEXT,      -- Date and time of the sale
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)
    conn.commit()
    conn.close()

# Admin Functions
def add_product():
    """
    Adds a new product to the inventory.
    Collects product details from the user and stores them in the database.
    """
    conn = sqlite3.connect("inventory_system.db")
    cursor = conn.cursor()

    # Collect product information from the user.
    print("\n\t\t\t\t------------------------------------------")
    name = input("\t\t\t\tEnter product name: ")
    category = input("\t\t\t\tEnter product category: ")
    price = float(input("\t\t\t\tEnter product price: "))  # Product price (must be numeric)
    stock = int(input("\t\t\t\tEnter initial stock: "))    # Initial stock level
    reorder_level = int(input("\t\t\t\tEnter reorder level: "))  # Threshold for low-stock warning

    # Insert the new product into the 'products' table.
    cursor.execute("""
        INSERT INTO products (name, category, price, stock, reorder_level)
        VALUES (?, ?, ?, ?, ?)
    """, (name, category, price, stock, reorder_level))

    conn.commit()
    conn.close()

    # Confirmation message for the user.
    print(f"\n\t\t\t\tProduct '{name}' added successfully!")
    print("\t\t\t\t------------------------------------------")

def view_inventory():
    """
    Displays all products in the inventory along with their details.
    Highlights products with stock levels below or equal to the reorder level.
    """
    conn = sqlite3.connect("inventory_system.db")
    cursor = conn.cursor()

    # Fetch all products from the database.
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # Display inventory with a heading.
    print("\n\n\t\t\t\t\t-------------------")
    print("\t\t\t\t\t     INVENTORY     ")
    print("\t\t\t\t\t-------------------")
    for product in products:
        id, name, category, price, stock, reorder_level = product
        # Highlight low-stock items for attention.
        low_stock_warning = " (Low Stock)" if stock <= reorder_level else ""
        print(f"\t\tID: {id} | Name: {name} | Category: {category} | Price: ${price:.2f} | Stock: {stock}{low_stock_warning}\n")
    
    conn.close()

def remove_product():
    """
    Removes a product from the inventory based on the provided product ID.
    Confirms the action with the user before deletion.
    """
    conn = sqlite3.connect("inventory_system.db")
    cursor = conn.cursor()

    # Display the inventory to help the user select the product to remove.
    view_inventory()
    print("\n\t\t\t\t------------------------------------------")
    product_id = int(input("\t\t\t\tEnter the product ID to remove: "))
    cursor.execute("SELECT name FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()

    if not product:
        # Inform the user if the product ID is invalid.
        print("\n\t\t\t\tInvalid product ID.")
    else:
        name = product[0]
        # Confirm the deletion with the user.
        confirm = input(f"\t\t\t\tSure to remove '{name}'? (y/n): ").lower()
        if confirm == "y":
            # Perform the deletion.
            cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            conn.commit()
            print(f"\n\t\t\t\tProduct '{name}' has been removed from inventory.")
        else:
            print("\n\t\t\t\tOperation canceled.")

    conn.close()
    print("\t\t\t\t------------------------------------------")

def update_stock():
    """
    Updates the stock quantity for a specific product based on the provided product ID.
    Adds the specified amount to the current stock.
    """
    conn = sqlite3.connect("inventory_system.db")
    cursor = conn.cursor()

    # Display the inventory to help the user select the product.
    view_inventory()
    print("\n\t\t\t\t------------------------------------------")
    product_id = int(input("\t\t\t\tEnter the product ID to update stock: "))
    additional_stock = int(input("\t\t\t\tEnter the quantity to add: "))  # Quantity to add to stock.

    cursor.execute("SELECT name, stock FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()

    if not product:
        # Handle invalid product ID.
        print("\n\t\t\t\tInvalid product ID.")
    else:
        name, current_stock = product
        # Calculate the new stock level.
        new_stock = current_stock + additional_stock
        cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
        conn.commit()
        print(f"\n\t\t\t\tStock for '{name}' updated to {new_stock}.")

    conn.close()
    print("\t\t\t\t------------------------------------------")

def purchase_products():
    """
    Facilitates the purchase process for products.
    Allows the user to add items to a cart, checkout, and records the sale.
    Updates stock levels for purchased items.
    """
    conn = sqlite3.connect("inventory_system.db")
    cursor = conn.cursor()

    # Shopping cart to hold selected items.
    cart = []
    view_inventory()

    while True:
        print("\n\t\t\t\t------------------------------------------")
        product_id = int(input("\t\t\t\tID to purchase (0 to checkout): "))
        if product_id == 0:  # Exit loop when user is ready to checkout.
            break

        # Fetch product details based on the selected ID.
        cursor.execute("SELECT name, stock, price FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()

        if not product:
            # Handle invalid product ID.
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
        # Handle empty cart scenario.
        print("\n\t\t\t\tNo items in the cart.")
        print("\t\t\t\tReturning to the main menu...")
        print("\t\t\t\t------------------------------------------")
        return

    # Display the items in the cart.
    print("\n\n\t\t\t\t\t-----------------")
    print("\t\t\t\t\t      CART     ")
    print("\t\t\t\t\t-----------------")
    total_price = 0
    for item in cart:
        product_id, name, quantity, price = item
        item_total = quantity * price
        total_price += item_total
        print(f"\t\t\t\t\t'{name}'")
        print(f"\t\t\t\t\tQuantity: {quantity}")
        print(f"\t\t\t\t\tUnit Price: ${price:.2f}")
        print(f"\t\t\t\t\tItem Total: ${item_total:.2f}")

    print(f"\n\t\t\t\t\tTotal Amount: ${total_price:.2f}")
    print("\n\n\t\t\t\t1. Proceed to Checkout")
    print("\t\t\t\t2. Cancel Transaction")
    checkout_choice = input("\t\t\t\tEnter your choice: ")

    if checkout_choice == "1":
        # Handle payment process.
        payment = float(input("\t\t\t\tEnter payment amount: "))
        if payment < total_price:
            print("\n\t\t\t\tInsufficient money. Transaction canceled.")
        else:
            change = payment - total_price
            print(f"\n\t\t\t\tPurchase successful! Change: ${change:.2f}")

            # Update stock levels and record the sale.
            for item in cart:
                product_id, _, quantity, price = item
                cursor.execute("UPDATE products SET stock = stock - ? WHERE id = ?", (quantity, product_id))
                sale_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("""
                    INSERT INTO sales (product_id, quantity, total_price, sale_date)
                    VALUES (?, ?, ?, ?)
                """, (product_id, quantity, quantity * price, sale_date))

            conn.commit()
            print("\t\t\t\tAll items purchased successfully!")
    elif checkout_choice == "2":
        print("\n\t\t\t\tTransaction canceled. Returning to the main menu...")
    else:
        print("\n\t\t\t\tInvalid choice. Returning to the main menu...")

    conn.close()

def view_sales():
    """
    Displays all recorded sales with details such as product name, quantity, total price, and sale date.
    """
    conn = sqlite3.connect("inventory_system.db")
    cursor = conn.cursor()

    # Fetch sales data by joining 'sales' and 'products' tables.
    cursor.execute("""
        SELECT s.id, p.name, s.quantity, s.total_price, s.sale_date
        FROM sales s
        JOIN products p ON s.product_id = p.id
    """)
    sales = cursor.fetchall()

    # Display sales records.
    print("\n\n\t\t\t\t\t-------------------")
    print("\t\t\t\t\t       SALES      ")
    print("\t\t\t\t\t-------------------")
    for sale in sales:
        id, name, quantity, total_price, sale_date = sale
        print(f"\tSale ID: {id} | Product: {name} | Quantity: {quantity} | Total Price: ${total_price:.2f} | Date: {sale_date}\n")
    
    conn.close()

# Main Menu
def main_menu():
    """
    Displays the main menu and provides options for the user to interact with the system.
    """
    initialize_database()  # Ensure the database is set up before interacting with it.

    # Display a welcome message.
    print("\n\n\t\t\t\t******************************************")
    print("\t\t\t\t     Hi! Welcome to Furfect Supplies")
    print("\t\t\t\t    Our Pet Product Inventory System!")
    print("\t\t\t\t******************************************")
    print("\t\tThis system is designed to help pet product sellers efficiently manage their inventory,")
    print("\t\ttrack stock levels, and streamline their sales process. With Furfect Supplies, you can ")
    print("\tfocus on providing the best for your furry customers while keeping your business organized and thriving!")
    print("\t\t\t\t******************************************")

    while True:
        # Display the main menu options.
        print("\n\n\t\t\t\t=== Pet Inventory Management System ===\n")
        print("\t\t\t\t\t1. Add Product")
        print("\t\t\t\t\t2. View Inventory")
        print("\t\t\t\t\t3. Remove Product")
        print("\t\t\t\t\t4. Update Stock")
        print("\t\t\t\t\t5. Purchase Products")
        print("\t\t\t\t\t6. View Sales")
        print("\t\t\t\t\t7. Exit\n")
        print("\t\t\t\t==========================================\n")
        choice = input("\t\t\t\tEnter your choice: ")

        if choice == "1":
            add_product()  # Option to add a new product.
        elif choice == "2":
            view_inventory()  # Option to view all products.
        elif choice == "3":
            remove_product()  # Option to remove a product.
        elif choice == "4":
            update_stock()  # Option to update stock for a product.
        elif choice == "5":
            purchase_products()  # Option to purchase products and record sales.
        elif choice == "6":
            view_sales()  # Option to view all sales records.
        elif choice == "7":
            print("\n\t\t\t\tExiting the program. Goodbye!")
            break
        else:
            # Handle invalid menu choices.
            print("\n\t\t\t\tInvalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
