# Bobyard comment system django

quick django backend set up

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Ensure you have the following software installed on your machine:

- Python (version 3.0 or higher)
- pip3 (Python package installer)

### Installing Dependencies

Run the following command to install the project dependencies:

```
python -m venv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```

### Database Setup

```
(venv) python manage.py makemigrations
(venv) python manage.py migrate
(venv) python manage.py shell < load_comments_and_users.py

```

### Running the Server
```
(venv) python manage.py runserver
```
