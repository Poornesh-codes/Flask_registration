# Flask Registration System

A simple user registration web application built using **Flask**, **Flask-WTF**, and **Flask-SQLAlchemy**.  
This project demonstrates form validation, database storage, and template inheritance.

---

## Features

- User registration form
- Email and password validation
- Flash messages for errors and success
- SQLite database for storing users
- Bootstrap styled UI
- Template inheritance using Jinja2

---

## Technologies Used

- Python
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- SQLite
- Bootstrap

---

## Project Structure

```
flask_registration/
│
├── app.py
├── forms.py
├── models.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── about.html
│   ├── register.html
│   └── confirm.html
│
└── static/
    ├── style.css
    └── flask.jpg
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/flask_registration.git
cd flask_registration
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Database

This project uses **SQLite** to store registered users.  
The database file (`users.db`) is automatically created when the application runs for the first time.
(can be found in the instance folder)

---

## Future Improvements

- User login system
- Password hashing
- Email uniqueness validation
- User dashboard
- Deployment to cloud platforms

---

## License

This project is for educational purposes.
