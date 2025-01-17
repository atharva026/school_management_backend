# School Management System

A robust backend system for managing a school environment using Django, Django REST Framework (DRF), PostgreSQL, Celery, and Redis with JWT-based authentication

## Features

- CRUD Operations for Students, Teachers, and Courses
- JWT-based Authentication for secure access
- Django Admin Panel Customization for easy management

## Technologies Used

- Backend Framework: Django + Django REST Framework (DRF)
- Database: PostgreSQL
- Authentication: JWT (JSON Web Token)
- Admin Management: Django Admin 5.0.4

## Setup and Installation

#### Prerequisites
- Python 3.8+
- PostgreSQL

#### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/atharva026/school_management_backend.git
cd school_management_backend
```

2. Install dependencies:
```bash
pip install Django django-admin djangorestframework-simplejwt psycopg2
```
3. Set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```
4. Create a superuser:
```bash
python manage.py createsuperuser
```
5. Run the development server:
```bash
python manage.py runserver
```
### JWT Authentication
JWT token-based authentication is used to secure the API. Include the token in the Authorization header for each request
Authorization > Auth Type > Bearer Token | Paste **access** token generated from get-token or user-login

### Postman API Collection 
In z_postman folder provided Postman collection, import it in your postman to test API's
