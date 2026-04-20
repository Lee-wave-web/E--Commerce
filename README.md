A simple full-stack E-Commerce Management System built using Django. This project demonstrates CRUD operations, REST-style APIs, and frontend-backend integration using JavaScript (Fetch API).
Features :
Product Management (Add, Edit, Delete, View)
Customer Management Order Management with stock handling
REST APIs for Product, Customer, and Order
AJAX-based form submission using Fetch API
Clean UI with HTML, CSS, and JavaScript
 Real-time updates without page reload
 Tech Stack:
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: MySQL
API Communication: JSON (Fetch API)
Project Structure :
ecommerce_project/
│
├── manage.py
├── ecommerce_project/
├── store/
├── static/
│   └── store/
│       ├── css/
│       └── js/
⚙️ Setup Instructions
Clone the repository
git clone https://github.com/Lee-wave-web/ecommerce_project.git
cd ecommerce_project
Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
Install dependencies
pip install django python-decouple mysqlclient
Configure .env file
DB_NAME=your_db_name
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
Run migrations
python manage.py makemigrations
python manage.py migrate
Start server
python manage.py runserver
 API Endpoints
Product API
POST /api/product/create/
POST /api/product/update/<id>/
POST /api/product/delete/<id>/
Customer API
POST /api/customer/create/
POST /api/customer/update/<id>/
POST /api/customer/delete/<id>/
Order API
POST /api/order/create/
POST /api/order/delete/<id>/
 How It Works
User submits form in frontend
JavaScript sends data via Fetch API
Django receives JSON request
Database is updated
JSON response is sent back
UI updates dynamically
Debugging (Important)

Used browser developer tools:

Open Inspect → Network Tab
Enable Fetch/XHR
Check:
Headers (Request type)
Payload (JSON data)
Response (API output)
 Future Improvements
User authentication (Login/Register)
Payment integration
Admin dashboard with analytics
Order tracking system
REST Framework integration

GitHub: https://github.com/Lee-wave-web
