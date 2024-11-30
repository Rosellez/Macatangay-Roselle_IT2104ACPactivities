<p align="center">
<img width="500" height="400" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/SYSTEM%20LOGO.png">
</p>


## Table of Contents

  - I. [Project Overview](#I-project-overview)   
  - II. [Python Concepts and Libraries](#II-python-concepts-and-libraries)  
  - III. [Integration with SDG 12](#III-integration-with-sdg-12)  
  - IV. [Instructions](#IV-instructions) 

------

## I. Project Overview
Furfect Supplies: A Pet Product Inventory System is a software solution developed using Python and connected to a SQLite database for efficient data storage and management. This system is designed specifically for pet product sellers to streamline their inventory processes, track product stock levels, and ensure smooth business operations. The system leverages Python's robust capabilities for user interaction and business logic. 


## Key Features
**Inventory Management:**
- Add, view, update, and remove products.
- Manage stock levels, including a low-stock warning based on reorder levels.

**Sales Tracking:**
- Track sales with product, quantity, total price, and sale date.
- Maintain a history of all sales transactions.

**Purchase Functionality:**
- Select products, add to a cart, and proceed to checkout.
- Automatically updates inventory after a successful purchase.

**User-Friendly Interface:**
- Clear menu system for navigating inventory and sales functions.

**Database Integration:**
- Uses SQLite for persistent data storage.


## How It Works
**Database Initialization:**
- Creates tables (products and sales) to store inventory and sales data.

**Admin Functions:**
- Add, remove, and update products in the inventory.
- View current stock with warnings for low inventory.

**Purchase Interaction:**
- Can purchase products, and the system ensures stock is sufficient before proceeding.
- Sales are logged with details, including the date and total amount.

**Real-Time Updates:**
- Inventory and sales data are updated immediately after actions are performed.

------


## II. Python Concepts and Libraries

### Core Python Concepts:
**Core Functionality**
- *Manage Inventory:*
Add, view, update, and remove products.
Provide low-stock warnings.
- *Track Sales:*
Record sales transactions with product details, quantities, and timestamps.
- *Facilitate Purchases:*
Allow customers to build a cart and complete purchases, updating inventory in real time.

**Data Handling**
- *Database:*
Uses SQLite (sqlite3) for persistent data storage.
- *Tables:*
products: Stores product information.
sales: Records sales transactions.
- *CRUD Operations:*
Create: Insert new products or sales records.
Read: Retrieve inventory and sales data.
Update: Adjust stock levels or product details.
Delete: Remove products from the inventory.

**Error Handling**
- *User Input Validation:*
Ensures valid product IDs and quantities when adding/updating stock or processing purchases.
Guards against invalid data types (e.g., non-numeric input for price/quantity).
- *Database Integrity:*
Uses foreign keys to ensure consistency between products and sales.
- *Graceful Failure:*
Handles invalid inputs (e.g., product ID not found) with error messages instead of crashes.

**Modular Code**
- *Functions:*
Each task (e.g., adding a product, viewing inventory, purchasing products) is encapsulated in a separate function.
Promotes reusability and improves readability.
- *Initialization:*
initialize_database() ensures the database is set up before other operations.
- *Menu System:*
Centralized main_menu() function calls other functions based on user choices.

**Abstraction**
- *Hides Complexity:*
Users interact with a menu-driven interface without needing to understand how the database works internally.
- *Encapsulation of Tasks:*
Database operations (e.g., SQL queries) and business logic are handled within individual functions.

**Encapsulation**
- *Implemented Through Functions:*
Each function encapsulates specific behavior, such as interacting with the database, updating stock, or recording sales.
- *Scope Control:*
Variables used within functions are local, ensuring they don’t interfere with other parts of the program.

**Control Flow**
- *Decision Making:*
if-elif-else constructs are used for menu navigation and handling user choices.
- *Loops:*
while loops manage the main menu and allow users to repeatedly interact with the program until they choose to exit.
- *Exception Handling:*
Indirectly present by prompting users for correct input and ensuring valid operations on the database.

**Optional Features**
- *Sales Reporting:*
View all sales records, including product names, quantities, and dates.
- *Low-Stock Alerts:*
Highlight products that are at or below their reorder levels.
- *Checkout System:*
Simulates a real-world shopping cart with payment and change calculation.
- *Database Flexibility:*
The SQLite database can be migrated to more advanced systems like MySQL or PostgreSQL for larger-scale use.


## Libraries:
  - sqlite3: For database management and interaction.
  - datetime: To log the date and time of sales transactions.

------


## III. Integration with SDG 12
Furfect Supplies supports Sustainable Development Goal 12 by:

 - **Efficient Resource Management:**
The system enables inventory management by tracking product stock, sales, and reorder levels. This ensures optimal stock utilization, minimizing waste and overproduction.
 - **Sustainable Business Practices:**
By automating stock tracking and purchase logging, it helps businesses streamline operations, making resource use more efficient and sustainable.
 - **Supporting Responsible Consumption:**
Features like low-stock alerts and precise sales recording ensure that the products align with demand, avoiding unnecessary surplus or shortages.

This falls under SDG 12: Responsible Consumption and Production.

------


## IV. Instructions

## Setup Instructions
**Prerequisites**
- **Python 3.7 or higher**: Download it from [python.org](https://www.python.org/downloads/).  
- **SQLite**: Pre-installed with Python, no additional installation required.  

### Installation
1. `Clone this code`:
   git clone https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/Furfect%20Supplies.py
   
2. `Install Dependencies`:
No external libraries are required; sqlite3 and datetime are included with Python.

3. `Run the program`:
Run the script using python Furfect_Supplies.py.


## Usage Instructions
1. Launch the Program: Run python Furfect_Supplies.py in the terminal.
2. Main Menu Options: Choose from the following options by entering the corresponding number.
3. Add Product: Add new products to the inventory with details like name, category, price, and stock.
4. View Inventory: See all products with stock details and low-stock warnings.
5. Remove Product: Delete a product by entering its ID.
6. Update Stock: Increase the stock quantity of an existing product.
7. Purchase Products: Simulate a customer purchase with a shopping cart.
7. View Sales: Display a log of all sales transactions.
8. Exit: Close the program.

*Special Notes:*
Ensure the database (inventory_system.db) is in the same directory as the script.
Backup the database periodically to avoid data loss.


  **WELCOME PAGE**
<p align="center">
  <img width="800" height="300" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/WELCOME%20PAGE.png">
</p>

   **MENU DISPLAY**
<p align="center">
  <img width="500" height="400" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/MENU%20DISPLAY.png">
</p>

   **ADD PRODUCT**
<p align="center">
  <img width="500" height="400" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/ADD%20PRODUCT.png">
</p>

   **VIEW INVENTORY**
<p align="center">
  <img width="700" height="300" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/VIEW%20INVENTORY.png">
</p>

   **REMOVE PRODUCT**
<p align="center">
  <img width="600" height="400" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/REMOVE%20PRODUCT.png">
</p>

  **UPDATE STOCK**
<p align="center">
  <img width="700" height="400" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/UPDATE%20STOCK.png">
</p>

  **PURCHASE PRODUCT**
<p align="center">
  <img width="600" height="600" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/PURCHASE%20PRODUCT.png">
</p>

   **VIEW SALE**
<p align="center">
  <img width="800" height="200" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/VIEW%20SALE.png">
</p>

 **EXIT**
<p align="center">
  <img width="400" height="100" src="https://github.com/Rosellez/Macatangay-Roselle_IT2104ACPactivities/blob/main/FINAL%20PROJECT/EXIT.png">
</p>


