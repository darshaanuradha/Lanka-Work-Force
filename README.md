# Lanka Work Force

> Localized service marketplace for connecting clients with daily-wage workers across Sri Lanka.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0.3-0C4B33?logo=django&logoColor=white)
![Status](https://img.shields.io/badge/Status-Academic%20Project-1F6FEB)

---

## Why This Project Matters

Lanka Work Force was created to digitize informal labor hiring workflows that are still largely offline.
Many workers struggle to get regular visibility, while clients struggle to quickly find trusted local workers.

This platform focuses on practical local accessibility:
- simple onboarding and login
- mobile-first experience
- bilingual-friendly user interface (Sinhala/English)
- direct and fast communication paths

## The Problem, Gap, and Solution

### Problem
Daily-wage hiring often depends on word-of-mouth networks, which are slow, inconsistent, and hard to scale.

### Gap
Most global gig platforms are not optimized for this context due to email-first signups, complex user flows, and higher digital literacy assumptions.

### Solution
Lanka Work Force bridges this gap by offering:
- phone number + PIN style onboarding
- worker discovery by category and location
- lightweight trust signals through ratings/reviews
- communication options that fit local usage patterns

## Feature Highlights

| Area | What It Supports |
|---|---|
| Worker Profiles | Registration, profile setup, visibility to clients |
| Worker Discovery | Search and filter by service type and location |
| Trust Layer | Ratings and reviews after completed work |
| Accessibility | Mobile-responsive and bilingual-friendly UX |

## Architecture Snapshot

The project follows a modular Django structure:

- Interface layer: templates and frontend assets
- Domain layer: apps for accounts, labor directory, and reviews
- Data layer: Django ORM with relational database support

Core entities include:
- CustomUser
- WorkerProfile
- Category
- Review

## Technology Stack

- Python 3.10+
- Django 5.0.3
- requests
- python-dotenv
- selenium
- gunicorn
- whitenoise

## Project Structure

```text
.
|-- README.md
|-- requirements.txt
|-- data/
|-- docs/
|-- src/
`-- tests/
```

---

## Quick Start

### Prerequisites

- Python 3.10+
- pip
- Git

### 1) Clone the repository

```bash
git clone https://github.com/your-username/lanka-work-force.git
cd "Lanka Work Force"
```

### 2) Create and activate virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5) Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6) Run the app

```bash
python manage.py runserver
```

Open: http://127.0.0.1:8000/

## Usage Flow

### For Clients

- browse the worker directory
- filter by category and location
- contact workers directly through available channels
- submit rating/review after completed work

### For Workers

- create a worker profile
- choose service category and location
- set expected daily wage
- become discoverable to nearby clients

## Testing

Run all tests:

```bash
python manage.py test
```

If Selenium-based tests are enabled, ensure browser drivers are installed and available in PATH.

## Deployment Notes

For production deployment:
- use gunicorn as the application server
- serve static files with whitenoise
- set `DEBUG=False`
- set production `ALLOWED_HOSTS`

## Documentation

Project proposal files are available in the `docs` directory.

## Team

Replace placeholders with final team details:

| Name | Student ID | Role | Responsibilities |
|---|---|---|---|
| Member 1 | ID | Project Manager | Sprint planning, coordination |
| Member 2 | ID | Domain Research | Market analysis, labor taxonomy |
| Member 3 | ID | Lead Developer | Backend architecture, models |
| Member 4 | ID | Lead Developer | Authentication, service logic |
| Member 5 | ID | QA and Testing | Validation, testing, reports |
| Member 6 | ID | UI and Documentation | Frontend templates, i18n, docs |

## Academic Integrity

All code in this repository is original project work. Third-party dependencies are documented in `requirements.txt`.

## License

Add your preferred license and include a LICENSE file.
