# Lanka Work Force

Localized service marketplace for connecting clients with daily-wage workers in Sri Lanka.

## Overview

Lanka Work Force is a web platform focused on digitizing informal labor hiring workflows in Sri Lanka. It helps clients discover workers and helps workers gain visibility without requiring complex onboarding steps.

The project is built around local accessibility:

- simple registration and login
- mobile-first interactions
- bilingual-friendly user experience
- practical communication options for faster hiring

## Problem and Solution

### Problem

Daily-wage hiring is often managed through offline word-of-mouth networks, which makes worker discovery slow and inconsistent.

### Gap

Many global gig platforms are not well suited to this use case due to email-first authentication, high digital literacy requirements, and complex user flows.

### Proposed Solution

Lanka Work Force addresses this by providing:

- phone number and PIN style onboarding
- worker listing and search by category and location
- lightweight review and trust signals
- direct communication channels suitable for local users

## Key Features

- Worker registration and profile management
- Client-side worker search and filtering
- Ratings and reviews
- Bilingual interface support
- Mobile-responsive layouts

## Architecture Summary

Suggested modular structure:

- Interface layer: Django templates and frontend assets
- Domain layer: business logic for accounts, worker directory, reviews
- Data layer: Django ORM with relational database

Possible core entities:

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

## Setup and Installation

### Prerequisites

- Python 3.10 or newer
- pip
- Git

### 1. Clone repository

```bash
git clone https://github.com/your-username/lanka-work-force.git
cd "Lanka Work Force"
```

### 2. Create and activate virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a .env file in the project root, then add required values:

```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Usage

### For clients

- browse worker directory
- filter by category and location
- open direct contact method
- submit rating and review after a completed job

### For workers

- register profile
- select skill category and location
- set expected daily wage
- become searchable to local clients

## Testing

Run the test suite with:

```bash
python manage.py test
```

If Selenium tests are used, make sure browser drivers are installed and available in your PATH.

## Deployment Notes

For production hosting:

- run with gunicorn
- use whitenoise for static files
- set DEBUG to False
- configure ALLOWED_HOSTS for your domain

## Documentation

Supporting proposal documents are available in the docs directory.

## Team

Fill in the final team list before submission:

| Name     | Student ID | Role                 | Responsibilities                |
| -------- | ---------- | -------------------- | ------------------------------- |
| Member 1 | ID         | Project Manager      | Sprint planning, coordination   |
| Member 2 | ID         | Domain Research      | Market analysis, labor taxonomy |
| Member 3 | ID         | Lead Developer       | Backend architecture, models    |
| Member 4 | ID         | Lead Developer       | Authentication, service logic   |
| Member 5 | ID         | QA and Testing       | Validation, testing, reports    |
| Member 6 | ID         | UI and Documentation | Frontend templates, i18n, docs  |

## Academic Integrity

All code in this repository is original project work. Third-party dependencies are listed in requirements.txt.

## License

Add your preferred license and include a LICENSE file.
