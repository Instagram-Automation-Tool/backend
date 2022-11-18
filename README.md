# Requirements
[Install Python](https://www.python.org/downloads/), then we will setup the [Python Django](https://www.djangoproject.com/) enviroment as instructed below. Django has [Selenium](https://www.selenium.dev/) integrated.

# Windows installation

##.bat files
1. [Install Python](https://www.python.org/downloads/)
2. Clone repository
3. Run ```setup.bat``` to create the Django virtual enviroment and install all dependencies
4. Run ```start.bat``` to start the server


##Manual installation trough Command Prompt
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

Create venv
py -m venv IgBotEnv
Activate env (assuming you are still cd'd into the base directory of the project)

IgBotEnv/Scripts/Activate.ps1


Install Google Chrome. We need to install  it so we can use its binary. (google why do  we need to install it?)
Install dependencies

pip install django
pip install django-cors-headers
pip install psycopg2
pip install selenium
pip install requests
pip install djangorestframework-simplejwt


Cd to folder containing manage.py. If the name of the path has spaces in it, make sure to include quotation marks around it like so: cd "path" | not cd path
cd "IG Backend\IgBotPrj"
Take care of migrations (explain what migrations are)
python manage.py makemigrations
python manage.py migrate
Run server
python manage.py runserver
