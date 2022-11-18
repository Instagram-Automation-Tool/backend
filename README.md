# Setup
[Install Python](https://www.python.org/downloads/), then we will setup the [Python Django](https://www.djangoproject.com/) enviroment as instructed below. Django has [Selenium](https://www.selenium.dev/) integrated.

## Windows
1. Open powershell, CD to the directory where you want the enviroment to be created
```CD ".../IG Backend"```

2. Create the virtual enviroment required to run Python Django
```py -m venv IgBotEnv```

3. Activate the virtual enviroment so we can install Django trough [Pip](https://pip.pypa.io/en/stable/)
```IgBotEnv/Scripts/Activate.ps1```

If the enviroment was succesfully activated you should see this at the beginning of the line: ![Image alright](https://i.imgur.com/HVYNVTV.png)

4. Install Django
```pip install Django```



# Dependenices
pip install djangorestframework

pip install django-cors-headers

pip install djangorestframework-simplejwt


# Setup 

Clone  repository
Install Python. To make sure  it's installed, do:....
cd to directory root (explain this more)
Install virtualenv
pip install virtualenv
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
