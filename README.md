# Lanka Work Force

A Localized Service E-commerce and Human Logistics Platform

Module: IT304040 Python Programming  
Project Domain: E-commerce and Logistics  
Team Size: 5 to 8 members  
Project Duration: 4 weeks

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.3-0C4B33?logo=django&logoColor=white)
![Database](https://img.shields.io/badge/Database-MySQL%20or%20SQLite-005C84)
![Status](https://img.shields.io/badge/Status-Academic%20Final%20Project-1F6FEB)

## Table of Contents

- [1. Overview and Problem Statement](#1-overview-and-problem-statement)
- [2. Situational Analysis](#2-situational-analysis)
- [3. User Pain Point Identification](#3-user-pain-point-identification)
- [4. Software Architecture and Design](#4-software-architecture-and-design)
- [5. Entity Relationship Design](#5-entity-relationship-design)
- [6. Agile Implementation and Team Structure](#6-agile-implementation-and-team-structure)
- [7. Git Repository and Cloud Deployment](#7-git-repository-and-cloud-deployment)
- [8. Python Implementation Best Practices](#8-python-implementation-best-practices)
- [9. Research and Problem-Solving Methodology](#9-research-and-problem-solving-methodology)
- [10. Evaluation Alignment](#10-evaluation-alignment)
- [11. Expected Deliverables](#11-expected-deliverables)
- [12. Complete Setup Instructions](#12-complete-setup-instructions)
- [13. Environment Variables](#13-environment-variables)
- [14. Database Setup](#14-database-setup)
- [15. Run and Test Commands](#15-run-and-test-commands)
- [16. Project Structure](#16-project-structure)
- [17. Troubleshooting](#17-troubleshooting)
- [18. Team Members and Roles](#18-team-members-and-roles)
- [19. Live Links](#19-live-links)
- [20. Conclusion](#20-conclusion)

## 1. Overview and Problem Statement

Lanka Work Force addresses a critical gap in digital matching of local informal labor with client demand in Sri Lanka.
Daily-wage workers such as masons, agricultural laborers, and technicians still rely on offline word-of-mouth systems.

Existing global gig platforms are poorly aligned with this user base due to:

- high digital literacy requirements
- email-first authentication
- complex payment systems
- poor localization for bilingual users

Problem statement:  
There is currently no accessible, low-tech, bilingual digital platform that enables efficient labor matching for Sri Lankan service workers and clients.
This causes income instability for workers and delays for clients.

## 2. Situational Analysis

### 2.1 Desk Review

Global labor platforms such as Upwork and Fiverr do not penetrate Sri Lanka's informal labor segment effectively.
Findings indicate a strong need for a mobile-first, localized, and low-tech solution.

### 2.2 Stakeholder Mapping

- Workers: masons, laborers, agricultural and technical workers with inconsistent job access
- Clients: homeowners, farmers, and small businesses facing delay and reliability issues

### 2.3 Gap Analysis

| Current State                | Desired State                       | Identified Gap                                      |
| ---------------------------- | ----------------------------------- | --------------------------------------------------- |
| Physical searching for labor | Instant digital matching via mobile | No localized phone-authenticated bilingual platform |
| Mandatory email login        | Phone plus PIN login                | High barrier for low-tech users                     |
| English-only interfaces      | Sinhala and English support         | Accessibility and usability gap                     |

### 2.4 Five Whys

- Symptom: workers cannot find consistent jobs
- Why: workers lack visibility to local clients
- Why: hiring relies on physical networking
- Why: workers do not use existing digital platforms
- Why: those platforms require email and high English literacy
- Root cause: absence of localized low-tech bilingual labor marketplace

## 3. User Pain Point Identification

| Pain Type | Description                                        | Impact                             |
| --------- | -------------------------------------------------- | ---------------------------------- |
| Process   | Physical travel to find labor                      | Delays project completion          |
| Financial | Workers cannot advertise availability efficiently  | Income volatility and low earnings |
| Product   | Existing apps require email and complex English UI | High barrier to entry              |

## 4. Software Architecture and Design

### 4.1 Modular Layered Architecture

- Interface Layer: mobile-optimized Django front end with bilingual support and phone-based authentication
- Domain Layer: worker taxonomy, location filtering, and quick-tap rating logic
- Persistence Layer: MySQL via Django ORM with support for SQLite in local development

## 5. Entity Relationship Design

Core entities:

1. CustomUser

- id (PK)
- phone_number (unique)
- password_hash
- is_worker
- is_client

2. WorkerProfile

- id (PK)
- user_id (FK to CustomUser.id)
- category_id (FK to Category.id)
- location
- daily_rate
- average_rating

3. Category

- id (PK)
- name_en
- name_si
- icon_tag

4. Review

- id (PK)
- worker_id (FK to WorkerProfile.id)
- client_name
- star_rating (1 to 5)
- quick_tap_tag

Note: Add ER diagram image in docs for final submission.

## 6. Agile Implementation and Team Structure

### 6.1 Suggested Roles

| Role                            | Responsibilities                                       |
| ------------------------------- | ------------------------------------------------------ |
| Project Manager or Scrum Master | Sprint planning, deadline tracking, team alignment     |
| Domain Researcher               | Situational analysis and gap validation                |
| Lead Developers (2 to 3)        | Core Django and modular implementation                 |
| QA and Testing                  | Validation, edge-case testing, bug tracking            |
| UI and Documentation            | UX quality, bilingual content, README and presentation |

### 6.2 Four-Week Sprint Schedule

| Phase      | Week   | Deliverables                                     | Outcome                              |
| ---------- | ------ | ------------------------------------------------ | ------------------------------------ |
| Initiation | 1      | Problem statement, research, repo setup, DB plan | Validated gap and technical baseline |
| Execution  | 2 to 3 | Core features, auth flow, testing logs           | Functional prototype                 |
| Closing    | 4      | Deployment, presentation, final report           | Live app and complete documentation  |

Daily rhythm: 10-minute standup for progress, blockers, and daily goals.

## 7. Git Repository and Cloud Deployment

- Repository: GitHub or GitLab with meaningful commits from all team members
- Deployment target: DigitalOcean or Railway
- Submission requirement: publicly accessible and working production link

## 8. Python Implementation Best Practices

- Modular separation between interface, domain, and persistence
- PEP8 style compliance and readable naming
- Use a virtual environment and pinned dependencies
- Django and ORM-first development for consistency and maintainability

## 9. Research and Problem-Solving Methodology

1. Desk review of literature and industry behavior
2. Stakeholder mapping and user segmentation
3. Gap analysis to identify unmet needs
4. Five Whys root-cause analysis
5. Pain-point prioritization across process, financial, and product dimensions

## 10. Evaluation Alignment

| Criteria                                       | Project Approach                                             |
| ---------------------------------------------- | ------------------------------------------------------------ |
| Research and Design (40%)                      | Situational analysis, gap validation, architecture decisions |
| Implementation and Technical Proficiency (30%) | Django apps, ORM, phone-based auth approach, localization    |
| Testing and Validation (20%)                   | Unit tests, edge-case tests, logs, regression checks         |
| Documentation and Presentation (10%)           | README, presentation, collaborative git evidence             |

## 11. Expected Deliverables

- Live cloud application URL
- Public git repository with structured source and commit history
- ER diagram and technical report document
- Final week presentation

## 12. Complete Setup Instructions

Follow this section exactly when setting up after cloning.

### 12.1 Prerequisites

- Python 3.10 or newer
- pip
- Git
- MySQL server (optional for local if using SQLite)

### 12.2 Clone Repository

```bash
git clone https://github.com/your-username/lanka-work-force.git
cd "Lanka Work Force"
```

### 12.3 Create and Activate Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 12.4 Install Dependencies

```bash
pip install -r requirements.txt
```

### 12.5 Configure Environment File

Copy sample file and update values:

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

macOS or Linux:

```bash
cp .env.example .env
```

Then edit .env with your real values.

### 12.6 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 12.7 Create Superuser

```bash
python manage.py createsuperuser
```

### 12.8 Start Development Server

```bash
python manage.py runserver
```

App URL: http://127.0.0.1:8000/  
Admin URL: http://127.0.0.1:8000/admin/

## 13. Environment Variables

The project reads environment values from .env through settings.

Minimum required keys:

- DJANGO_SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DB_ENGINE
- DB_NAME

MySQL keys when DB_ENGINE is mysql:

- DB_HOST
- DB_PORT
- DB_USER
- DB_PASSWORD

Example .env:

```env
DJANGO_SECRET_KEY=replace-with-a-strong-secret
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_ENGINE=sqlite
DB_NAME=db.sqlite3

# For mysql mode
# DB_ENGINE=mysql
# DB_HOST=127.0.0.1
# DB_PORT=3306
# DB_NAME=lanka_work_force
# DB_USER=root
# DB_PASSWORD=your_mysql_password
```

## 14. Database Setup

### 14.1 SQLite Setup (Recommended for quick local start)

In .env:

```env
DB_ENGINE=sqlite
DB_NAME=db.sqlite3
```

Then run:

```bash
python manage.py migrate
```

### 14.2 MySQL Setup (Recommended for production-like behavior)

Create database:

```sql
CREATE DATABASE lanka_work_force CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Update .env:

```env
DB_ENGINE=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=lanka_work_force
DB_USER=root
DB_PASSWORD=your_mysql_password
```

Then run:

```bash
python manage.py migrate
```

## 15. Run and Test Commands

Run server:

```bash
python manage.py runserver
```

Run tests:

```bash
python manage.py test
```

Collect static files:

```bash
python manage.py collectstatic
```

Create new app:

```bash
python manage.py startapp app_name
```

## 16. Project Structure

```text
src/                application code
tests/              test scripts
data/               sample data
docs/               documentation and diagrams
requirements.txt    dependencies
```

## 17. Troubleshooting

### mysqlclient install error on Windows

If build fails due to C++ tools:

1. Upgrade pip and retry install.
2. Use a Python version that has wheel support for mysqlclient.
3. Install Microsoft C++ Build Tools only if no wheel is available.

### Environment file not loading

- Make sure .env is in repository root.
- Confirm keys are spelled exactly as documented.

### Database connection issue

- Verify DB_ENGINE, DB_HOST, DB_PORT, DB_NAME, DB_USER, and DB_PASSWORD.
- Ensure MySQL service is running before migration.

## 18. Team Members and Roles

Update with real names and student IDs before final submission.

| Name     | Student ID | Role                 | Responsibilities                        |
| -------- | ---------- | -------------------- | --------------------------------------- |
| Member 1 | ID         | Project Manager      | Sprint management and delivery tracking |
| Member 2 | ID         | Domain Researcher    | Research and gap validation             |
| Member 3 | ID         | Lead Developer       | Core architecture and backend           |
| Member 4 | ID         | Lead Developer       | Authentication and feature modules      |
| Member 5 | ID         | QA and Testing       | Test planning and defect handling       |
| Member 6 | ID         | UI and Documentation | Interface and project documentation     |

## 19. Live Links

- Production URL: add your final cloud link
- Repository URL: add your final git link

## 20. Conclusion

Lanka Work Force is designed to provide an accessible, bilingual, and phone-friendly service marketplace for Sri Lanka's informal labor sector.
The project directly targets worker visibility, income stability, and client hiring efficiency.
By using agile execution, modular Django architecture, and structured documentation, the solution aligns with IT304040 module goals and evaluation criteria.
