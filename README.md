# Requirements
[Install Python](https://www.python.org/downloads/). Make sure to tick the `Add Python to enviroment variables` box. If you didn't do it on install, you can rerun the installer, hit `Modify`, then tick the option. 

![image](https://user-images.githubusercontent.com/35419029/202734746-7ab53320-a430-4984-a3d2-fe5000d5f577.png)

Next, we will setup the [Python Django](https://www.djangoproject.com/) virtual enviroment as instructed below.
## Windows installation
### .bat files
1. Clone repository
2. Run ```setup.bat``` to create the Django virtual enviroment and install all dependencies
3. Run ```start.bat``` to start the server

### Manual setup and execution trough Command Prompt
1. Clone repository
2. Open Command Prompt
3. CD to desired directory
```cd C:/{your path}```
4. Install the virtualenv package
```pip install virtualenv```
5. Create a virtualenv named IgBotEnv
```py -m venv IgBotEnv```
6. CD to the Scripts folder
```cd "IgBotEnv/Scripts"```
7. Activate the virtual enviroment to install required packages
```call activate.bat```
8. Install dependencies
```pip install django django-cors-headers psycopg2 selenium requests djangorestframework-simplejwt```
9. CD to the Project's folder
```cd "../../IgBotPrj"```
10. Create local migrations
```python manage.py makemigrations```
```python manage.py migrate --fake```
11. Start the server
```python manage.py runserver```
