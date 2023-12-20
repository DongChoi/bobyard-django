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


Your README looks good for a quick Django backend setup. It provides clear instructions for setting up and running the project. However, you might want to include a brief description of what the project is about, especially if it's not evident from the title. Here's an enhanced version:

markdown
Copy code
# Bobyard Comment System Django

A quick Django backend setup for the Bobyard Comment System.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Ensure you have the following software installed on your machine:

- Python (version 3.0 or higher)
- pip3 (Python package installer)

### Installing Dependencies

Run the following commands to set up a virtual environment and install the project dependencies:

```bash
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
