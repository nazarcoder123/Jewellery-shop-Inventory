<!-- # Jewellery-shop-Inventory using flask

> To run this in your local system 

> git clone https://github.com/nazarcoder123/Jewellery-shop-Inventory.git

> pip install -r requirements.txt

> create a database name jewellery_shop in your database(Oracle 23ai or PgAdmin)

> Then copy the query from run_sql.py to database execute it. Hence your tables are created

> Then execute this command in your vs code terminal python console.py

> Last but not the least flask run

Note: you should have python version 3.10.0 install in your system
      And create a virtual Env with py==3.10.0 & activate it (.venv\Scripts\activate).   -->


💎 Jewellery Shop Inventory (Flask Application)

📌 Overview
This is a Flask-based Jewellery Shop Inventory management system. It helps in managing inventory, tracking sales, and organizing jewellery stock efficiently.

🚀 Getting Started

1️⃣ Clone the Repository
git clone https://github.com/nazarcoder123/Jewellery-shop-Inventory.git
cd Jewellery-shop-Inventory

2️⃣ Set Up a Virtual Environment
Ensure Python 3.10.0 is installed, then create and activate a virtual environment:

🔹 Windows
python -m venv .venv
.venv\Scripts\activate

🔹 macOS/Linux
python -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up the Database

Create a database named jewellery_shop in Oracle 23ai or PostgreSQL (PgAdmin).

Open run_sql.py, copy the SQL queries, and execute them in your database to create the required tables.

python console.py (This will insert some data in your database)

5️⃣ Run the Application

flask run

The Flask application should now be running at Running on http://127.0.0.1:5000  🎉

🛠 Requirements

Python 3.10.0

Oracle 23ai or PostgreSQL (PgAdmin)