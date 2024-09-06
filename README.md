# Simple Note Taking API

This is a Django-based API for note-taking.

## Setup Instructions

1. Clone the repository.
    git clone <repository_url>


2. Create a virtual environment and activate it.

    python -m venv envname
    source envname/bin/activate  # On Windows use `envname\Scripts\activate`

3. Install dependencies:
    
    pip install -r requirements.txt

4. Set up the PostgreSQL database and update settings.py.

# In settings.py :

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',      # Replace with your PostgreSQL database name
        'USER': 'your_database_user',      # Replace with your PostgreSQL user
        'PASSWORD': 'your_database_password',  # Replace with your PostgreSQL user's password
        'HOST': 'localhost',               # Set to your PostgreSQL server's address, 'localhost' if it's on the same machine
        'PORT': '5432',                    # Default PostgreSQL port, change if different
    }
}

5. Run migrations:
    
    python manage.py makemigrations
    python manage.py migrate

6. Run the development server:
    
    python manage.py runserver


## API Endpoints

- POST /api/notes/create/: Create a new note.
- GET /api/notes/<id>/retrieve/: Fetch a note by ID.
- GET /api/notes/?title=<substring>: Query notes by title substring.
- PUT /api/notes/<id>/update/: Update a note.
