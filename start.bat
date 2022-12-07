@ECHO OFF

ECHO Press CTRL + C to stop server.

cd "IgBotEnv\Scripts"
call activate.bat
cd "..\..\IgBotPrj"
python.exe manage.py runserver

PAUSE