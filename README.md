# 🛒 E-Commerce Portal using Django

## 📖 Project Overview
This project is a **full-stack E-commerce web application** developed using **Django** as part of an academic assignment.  
The application allows users to create accounts, browse products, add products to a cart, place orders, and view their order history.  
Administrators can manage customers, products, and orders through Django’s built-in admin panel.

The goal of this project is to demonstrate understanding of:
- User authentication (login & signup)
- CRUD operations
- Database relationships
- Order management and pricing logic
- Clean and maintainable Django code

---

## ✨ Features

### 👤 User Features
- User registration (Signup)
- User authentication (Login & Logout)
- View product catalog with images
- Add products to cart
- Remove products from cart
- Checkout and place orders
- Automatic price calculation with tax
- View personal order history

### 🔐 Admin Features
- Secure admin login
- Create, update, and delete products
- Upload product images
- Manage customers
- View all orders and order items

---

## 🛠️ Technology Stack
- **Programming Language:** Python
- **Framework:** Django
- **Frontend:** HTML, Bootstrap 5
- **Backend:** Django Views & Models
- **Database:** SQLite
- **Authentication:** Django built-in authentication system
- **Version Control:** Git & GitHub

---

## 🗄️ Database Design

### 📋 Tables

#### Customers
- id
- user (OneToOne relationship with Django User)
- created_at

#### Products
- id
- name
- description
- price
- stock
- image

#### Orders
- id
- customer_id
- total_price
- order_date

#### OrderItems
- id
- order_id
- product_id
- quantity
- price

---

### 🔗 Relationships
- One customer can place **many orders**
- One order can contain **many products**
- One product can appear in **many orders**

---

## 🚀 Installation & Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ecommerce-django.git
cd ecommerce-django

2️⃣ Create and Activate Virtual Environment
python -m venv venv
Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install Required Dependencies
pip install -r requirements.txt

4️⃣ Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (Admin)
python manage.py createsuperuser

6️⃣ Run the Development Server
python manage.py runserver

7️⃣ Access the Application

Website: http://127.0.0.1:8000/products/

Admin Panel: http://127.0.0.1:8000/admin/

🖼️ Product Image Upload

Login to the Django admin panel

Navigate to Products

Add or edit a product

Upload an image using the image field

Images are stored in the media/ directory

🧮 Pricing Logic

Subtotal = Product Price × Quantity

Tax = 5% of Subtotal

Total Price = Subtotal + Tax

Product price at the time of order is saved to maintain order history accuracy

🔐 Security Features

Passwords are securely hashed using Django’s authentication system

CSRF protection enabled for all forms

Role-based access (Admin vs Customer)

Admin-only access for product and customer management

📁 Project Structure
ecommerce/
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
├── media/
├── manage.py
├── requirements.txt
└── README.md

📌 Future Enhancements

Payment gateway integration

Discount and coupon system

Product search and filtering

Pagination

Email notifications

REST API integration

🎓 Academic Use

This project was developed strictly for educational purposes to fulfill course requirements.
It demonstrates backend development, database management, and frontend integration using Django.

👨‍💻 Author

Ikramul Haque

✅ Assignment Completion Checklist

✔ Login & Signup

✔ Customer Management (CRUD)

✔ Product Management (CRUD)

✔ Order & Order Items

✔ Pricing Logic

✔ Database Relationships

✔ Clean User Interface

✔ GitHub Repository

✔ Documentation
