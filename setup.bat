@ECHO OFF

pip install virtualenv
py -m venv IgBotEnv
cd "IgBotEnv/Scripts"
call activate.bat
pip install django django-cors-headers psycopg2 selenium requests djangorestframework-simplejwt
cd "../../IgBotPrj"
python manage.py makemigrations
python manage.py migrate --fake


echo AYOOOOOO 

PAUSE