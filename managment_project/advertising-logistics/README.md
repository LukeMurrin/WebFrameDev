# Advertising Logistics Project

This Django project is designed for an advertising company that manages the logistics of parcels and their contents. It includes features for handling different user roles and managing parcel information efficiently.

## Project Structure

```
advertising-logistics
├── advertising_logistics
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── parcels
│   ├── migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── users
│   ├── migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── templates
│   ├── base.html
│   ├── parcels
│   │   └── parcel_list.html
│   └── users
│       └── user_dashboard.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
└── README.md
```

## User Roles

The application supports the following user roles:

1. **Customer**: Users who send and receive parcels.
2. **Delivery Personnel**: Users responsible for delivering parcels to customers.
3. **Warehouse Staff**: Users who manage the storage and handling of parcels in the warehouse.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd advertising-logistics
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```
   python manage.py migrate
   ```

5. **Run the development server**:
   ```
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Features

- User registration and authentication.
- Parcel management including creation, tracking, and status updates.
- Role-based access control for different user functionalities.
- User dashboards for personalized access to features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.