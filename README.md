This is the backend api of the Winterfell Dry Cleaners

Created separate projects. This enables us to work on them or deploy them separately

The api app is order_search
**/winterfell_dry_cleaners/order_search**

### install packages
pip install -r requirements.txt (WAIT, are you in a virtual environment?)

### setup database
in **/winterfell_dry_cleaners/settings.py**
- Add the database, user credentials and host/port to point to a valid server


### Run App
In the project directory **/winterfell_dry_cleaners**, run
- python manage.py runserver

### Try out api at
- {host}/api/
- Only Item and Order supported. 

### Read **/frontend/README.md next**

### Remarks
Testing is limited because of time but more will certainly be written before feature is completed. see test_views.py


