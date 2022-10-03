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

