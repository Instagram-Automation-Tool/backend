# Requirements
[Install Python](https://www.python.org/downloads/), then we will setup the [Python Django](https://www.djangoproject.com/) virtual enviroment as instructed below.

## Windows installation
### .bat files
1. [Install Python](https://www.python.org/downloads/)
2. Clone repository
3. Run ```setup.bat``` to create the Django virtual enviroment and install all dependencies
4. Run ```start.bat``` to start the server

### Manual setup trough and execution trough Command Prompt
1. [Install Python](https://www.python.org/downloads/)
2. Clone repository
3. Open Command Prompt
4. CD to desired directory
```cd C:/{your path}```
5. Install the virtualenv package
```pip install virtualenv```
6. Create a virtualenv named `IgBotEnv`
```py -m venv IgBotEnv```
7. CD to the `Scripts` folder
```cd "IgBotEnv/Scripts"```
8. Activate the virtual enviroment to install required packages
```call activate.bat```
9. Install dependencies
```pip install django django-cors-headers psycopg2 selenium requests djangorestframework-simplejwt```
10. CD to the Project's folder
```cd "../../IgBotPrj"```
11. Create local migrations
```python manage.py makemigrations```
```python manage.py migrate --fake```
12. Start the server
```python manage.py runserver```
