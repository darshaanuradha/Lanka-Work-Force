# Lanka Work Force

Localized service marketplace for connecting clients with daily-wage workers across Sri Lanka.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.3-0C4B33?logo=django&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Development-1F6FEB)

## Table of Contents

- [Project Overview](#project-overview)
- [Feature Highlights](#feature-highlights)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Quick Start (Complete Setup)](#quick-start-complete-setup)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [Run, Test, and Common Commands](#run-test-and-common-commands)
- [Troubleshooting](#troubleshooting)
- [Team](#team)

## Project Overview

Lanka Work Force is designed to digitize informal labor hiring in Sri Lanka.
It helps clients find workers faster and helps workers become visible to local demand.

The platform focus:

- simple onboarding flow
- mobile-first UX
- bilingual-friendly experience (Sinhala and English)
- practical, direct communication paths

## Feature Highlights

| Area            | Description                                            |
| --------------- | ------------------------------------------------------ |
| Worker Profiles | Worker registration, profile setup, service visibility |
| Discovery       | Search/filter workers by category and location         |
| Trust Signals   | Ratings and review flow                                |
| Accessibility   | Mobile responsive and local UX focus                   |

## Technology Stack

- Python 3.10+
- Django 6.0.3
- mysqlclient
- python-dotenv
- whitenoise
- gunicorn

## Project Structure

```text
.
|-- accounts/
|-- core_project/
|-- labor_directory/
|-- reviews/
|-- manage.py
|-- README.md
|-- requirements.in
|-- requirements.txt
|-- docs/
|-- data/
|-- src/
`-- tests/
```

## Quick Start (Complete Setup)

Follow these steps when cloning this project for the first time.

### 1) Clone repository

```bash
git clone https://github.com/your-username/lanka-work-force.git
cd "Lanka Work Force"
```

### 2) Create virtual environment

Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Create environment file

Create a file named `.env` in the project root and copy the template below.

```env
# Django
DJANGO_SECRET_KEY=change-this-to-a-long-random-secret
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database mode: sqlite or mysql
DB_ENGINE=sqlite

# SQLite (used when DB_ENGINE=sqlite)
DB_NAME=db.sqlite3

# MySQL (used when DB_ENGINE=mysql)
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=lanka_work_force
DB_USER=root
DB_PASSWORD=your_mysql_password
```

### 5) Prepare database and run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6) Create admin user (optional but recommended)

```bash
python manage.py createsuperuser
```

### 7) Run development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/

## Environment Variables

This project loads environment variables from `.env` in [core_project/settings.py](core_project/settings.py).

Required for all setups:

- DJANGO_SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DB_ENGINE

Database-specific:

- SQLite: DB_NAME
- MySQL: DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

## Database Setup

### Option A: SQLite (fast local setup)

Use in `.env`:

```env
DB_ENGINE=sqlite
DB_NAME=db.sqlite3
```

Then run:

```bash
python manage.py migrate
```

### Option B: MySQL (recommended for production-like development)

1. Install and start MySQL server.
2. Create database:

```sql
CREATE DATABASE lanka_work_force CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. Set `.env` values:

```env
DB_ENGINE=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=lanka_work_force
DB_USER=root
DB_PASSWORD=your_mysql_password
```

4. Run migrations:

```bash
python manage.py migrate
```

## Run, Test, and Common Commands

Run app:

```bash
python manage.py runserver
```

Run tests:

```bash
python manage.py test
```

Create new app:

```bash
python manage.py startapp app_name
```

Collect static files:

```bash
python manage.py collectstatic
```

## Troubleshooting

### mysqlclient build error on Windows

If installation fails with a C++ build tools error, do one of the following:

1. Upgrade pip and retry (newer wheels may be available):

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

2. Install Microsoft C++ Build Tools if a wheel is unavailable for your Python version.

### .env not applied

Confirm the file is named exactly `.env` and located in project root (same level as `manage.py`).

### Database connection errors

- verify DB_ENGINE value
- verify DB_HOST, DB_PORT, DB_USER, DB_PASSWORD
- confirm database exists before running migrations

## Team

Replace placeholders with final team details.

| Name     | Student ID | Role                 | Responsibilities                 |
| -------- | ---------- | -------------------- | -------------------------------- |
| Member 1 | ID         | Project Manager      | Sprint planning and coordination |
| Member 2 | ID         | Domain Research      | Market and user-flow analysis    |
| Member 3 | ID         | Lead Developer       | Backend architecture and models  |
| Member 4 | ID         | Lead Developer       | Auth and service logic           |
| Member 5 | ID         | QA and Testing       | Validation and testing workflow  |
| Member 6 | ID         | UI and Documentation | Templates, i18n, documentation   |

## License

Add your preferred license and include a LICENSE file.
