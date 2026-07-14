# Successphere Backend

This repository contains the Django REST Framework backend for the Successphere project.

---

# Prerequisites

Before setting up the project, ensure you have the following installed:

* Python 3.12+ (or the version used by the team)
* PostgreSQL
* Git

---

# 1. Clone the Repository

```bash
git clone <repository-url>
cd SUCCESSPHERE_BACKEND
```

---

# 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Install PostgreSQL

Install PostgreSQL if it is not already installed.

Create a new database named:

```
successphere_db
```

You may use your own PostgreSQL username and password.

Example:

```
Database Name : successphere_db
Username      : postgres
Password      : <your_password>
Host          : localhost
Port          : 5432
```

---

# 5. Configure Environment Variables

A file named `.env.example` is included in the repository.

Create a new file named:

```
.env
```

Copy the contents of `.env.example` into `.env` and replace the placeholder values with your own configuration.

Example:

```env
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=successphere_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

**Important:**

* Do not commit the `.env` file.
* Keep your database password and secret key private.

---

# 6. Apply Database Migrations

Run:

```bash
python manage.py migrate
```

This creates all required database tables.

---

# 7. Load Initial Data (If Provided)

If the repository contains a `data.json` file, import it using:

```bash
python manage.py loaddata data.json
```

This will populate the database with the project's initial data (such as products, categories, etc.).

If no `data.json` is available, you can skip this step.

---

# 8. Create an Admin User (Optional)

To access the Django Admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your username and password.

---

# 9. Run the Development Server

```bash
python manage.py runserver
```

The backend will be available at:

```
http://127.0.0.1:8000/
```

---

# API Endpoints

Example:

```
http://127.0.0.1:8000/api/
```

Refer to the project documentation or `urls.py` for the complete list of endpoints.

---

# Project Structure

```
SUCCESSPHERE_BACKEND/
│
├── manage.py
├── requirements.txt
├── .env.example
├── media/
├── products/
├── successphere/
└── README.md
```

---

# Common Commands

Install dependencies

```bash
pip install -r requirements.txt
```

Create migrations

```bash
python manage.py makemigrations
```

Apply migrations

```bash
python manage.py migrate
```

Run the development server

```bash
python manage.py runserver
```

Create an admin user

```bash
python manage.py createsuperuser
```

Export project data

```bash
python manage.py dumpdata --indent 4 > data.json
```

Import project data

```bash
python manage.py loaddata data.json
```

---

# Notes

* Each developer should use their own local PostgreSQL installation.
* Each developer should create their own `.env` file.
* The `.env` file is intentionally excluded from Git and must never be committed.
* If the database schema changes, pull the latest code and run:

```bash
python manage.py migrate
```

* If new Python packages are installed, update the dependency list before pushing:

```bash
pip freeze > requirements.txt
```

---

# Troubleshooting

### ModuleNotFoundError

Run:

```bash
pip install -r requirements.txt
```

---

### Database Connection Error

Verify:

* PostgreSQL is running.
* The database exists.
* The values in `.env` are correct.
* The PostgreSQL username and password are valid.

---

### Migrations Not Applied

Run:

```bash
python manage.py migrate
```

---

### Media Files

Product images are stored in the `media/` directory. Ensure this folder is present if the project depends on uploaded media.
