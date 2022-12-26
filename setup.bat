@ECHO OFF

pip install virtualenv
py -m venv IgBotEnv
cd "IgBotEnv/Scripts"
call activate.bat
pip install django asgiref async-generator attrs black certifi cffi charset-normalizer click colorama distlib django-cors-headers django-selenium djangorestframework djangorestframework-simplejwt filelock h11 idna mypy-extensions mysqlclient outcome pathspec platformdirs psycopg2 psycopg2-binary pycparser PyJWT PyMySQL PySocks python-dotenv pytz requests selenium six sniffio sortedcontainers sqlparse tomli tqdm trio trio-websocket typing_extensions tzdata urllib3 virtualenv webdriver-manager wsproto
cd "../../IgBotPrj"
python manage.py makemigrations
python manage.py migrate --fake


echo AYOOOOOO 

PAUSE