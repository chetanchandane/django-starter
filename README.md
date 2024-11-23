# Basic Starter Django Project

This is a basic Django project. The following steps will guide you on how to set up and run the project locally.

## Prerequisites
- Python (3.8 or later)
- Pip (Python package manager)
- Virtual environment (optional but recommended)
- Git (optional for cloning the repository)

## Setup Instructions

### 1. Clone the Repository
If the project is hosted on GitHub, clone it using:
```bash
git clone https://github.com/chetanchandane/django-starter.git 
cd django-starter
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies:
```bash
python3 -m venv .venv
# On Linux/macOs: source .venv/bin/activate
# On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Apply database migrations to set up the database schema:
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
If the project uses Django's admin interface, create a superuser to access it:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the superuser account.

### 6. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

If you created a superuser and need to access the admin interface, visit:
```
http://127.0.0.1:8000/admin/
```

## Additional Notes

### Static Files
If your project includes static files (CSS, JavaScript, etc.), ensure they are properly collected:
```bash
python manage.py collectstatic
```
This is usually required for production setups.

### Environment Variables
Some projects use environment variables for sensitive data (e.g., database credentials, secret keys). Use a `.env` file or export them manually:
```bash
export SECRET_KEY='your_secret_key'
export DEBUG=True  # Or False for production
```
For Windows, use:
```bash
set SECRET_KEY=your_secret_key
set DEBUG=True
```

### Debugging
Ensure `DEBUG=True` in the `settings.py` file during development. In production, set it to `False` and configure allowed hosts.

## Common Commands
- Run the server:
  ```bash
  python manage.py runserver
  ```
- Apply migrations:
  ```bash
  python manage.py migrate
  ```
- Create a superuser:
  ```bash
  python manage.py createsuperuser
  ```
- Collect static files:
  ```bash
  python manage.py collectstatic
  ```


Can also refer to the Django documentation at [https://docs.djangoproject.com/](https://docs.djangoproject.com/).

