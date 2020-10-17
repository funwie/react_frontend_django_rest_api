Django project for orders with a backend api written in Django Rest Framework and a separate frontend in React

Separate projects for api and frontend enable separation of concerns and independent deployment and scaling. 

The api app is order_search
**/winterfell_dry_cleaners/order_search**

### install packages
pip install -r requirements.txt (WAIT, are you in a virtual environment?)

### setup database
in **/winterfell_dry_cleaners/settings.py**
- Add the database, user credentials and host/port to point to a valid server

## run migration
python manage.py migrate

### Run the Backend API
In the project directory **/winterfell_dry_cleaners**
- python manage.py runserver

### Run tests
python manage.py test

### Try out api at
- {host}/api/
- Post models using json 

### Read **/frontend/README.md next**

### Remarks
See test_views.py for tests


