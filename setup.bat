@ECHO OFF

pip install virtualenv
py -m venv IgBotEnv
cd "IgBotEnv/Scripts"
call activate.bat
pip install django
pip install django-cors-headers
pip install psycopg2
pip install selenium
pip install requests
pip install djangorestframework-simplejwt
cd "../../IgBotPrj"
python manage.py makemigrations
python manage.py migrate --fake


echo AYOOOOOO 

PAUSE