# MediLink — Digital Hospital Management System

> Version 1.0 · Lahore, Pakistan · Built by Anas Fahim & Mazan Khan

---

## ⚡ Quick Start (Windows)

Just double-click **`start.bat`** — it does everything automatically:
1. Creates a virtual environment
2. Installs Django
3. Runs migrations
4. Seeds the database with 8 doctors
5. Starts the server

Then open your browser: **http://127.0.0.1:8000**

---

## Manual Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

# 2. Install Django
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Seed the database with doctors
python seed_data.py

# 5. (Optional) Create admin account
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver
```
http://127.0.0.1:8000  
Open: 
Admin: http://127.0.0.1:8000/admin

---

## Project Structure

```
medilink/
├── medilink/               ← Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── doctors/                ← Doctor app
│   ├── models.py           ← Doctor model
│   ├── views.py            ← doctor_list view
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── patients/               ← Patient app
│   ├── models.py           ← Patient model
│   ├── views.py            ← book_appointment API view
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/              ← HTML templates
│   ├── base.html           ← Nav, footer, modals
│   └── doctors/
│       └── doctor_list.html ← Full page
│
├── static/
│   ├── css/
│   │   └── style.css       ← All styles
│   └── js/
│       └── main.js         ← All JavaScript
│
├── seed_data.py            ← Adds 8 sample doctors
├── manage.py
├── requirements.txt
└── start.bat               ← One-click startup (Windows)
```

---

## Features

- **Hero Section** — Animated stats, floating cards
- **Smart Doctor Search** — Filter by specialization, search by name/location
- **Doctor Cards** — Profile, experience bar, Book Now button
- **Patient Form** — Enter details + describe health problem
- **AI Matching** — Keywords matched to correct specialist
- **Appointment Confirmation** — Saves to SQLite database
- **Django Admin** — Manage doctors & patients at /admin
- **Responsive** — Works on mobile and desktop

---

## Admin Panel

```
URL:      http://127.0.0.1:8000/admin
Username: (set during createsuperuser)
```

From admin you can:
- Add / edit / delete doctors
- View all booked patient appointments
- Filter and search records
