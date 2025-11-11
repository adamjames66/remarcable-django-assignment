This repository includes a pre-populated SQLite database with sample data. To run the project immediately:

1. Clone the repository:
```bash
git clone https://github.com/adamjames66/remarcable-django-assignment.git
cd remarcable-django-assignment
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install Django:
```bash
pip install Django
```

4. Run the server:
```bash
python manage.py runserver
```

5. Visit http://127.0.0.1:8000/ to see the application

### Admin Access

The database includes a superuser account:
- Username: `admin`
- Password: `admin321`

Visit http://127.0.0.1:8000/admin/ to access the admin interface.

### Included Sample Data

The database contains:
- Categories (Burgers, Pizza, Chicken, Mexican, Sandwiches)
- Tags (Fast Service, Drive-Thru, Breakfast Available, etc.)
- Fast Food Chains (McDonald's, Burger King, Subway, etc.)

## AI Usage Disclosure

This project was developed with assistance from Claude AI for:
- Django project structure setup
- QuerySet optimization suggestions
- HTML template structure
- Documentation formatting

All code was reviewed, understood, and tested by the developer. The core logic for search and filtering functionality was implemented with full understanding of Django's ORM and template system.
