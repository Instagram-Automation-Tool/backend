import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR, "/gecko")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pickle


class WebdriverActions:
    def StoreLoginCredentials():
        chrome_options = Options()
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.instagram.com/")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
        print(
            "\nLogin to your Instagram account.\nAfter 20 seconds, your credentials will be stored for later automatic logins.\n\n"
        )

        time.sleep(20)
        dict = driver.get_cookies()
        with open("saved_dictionary.pkl", "wb") as f:
            pickle.dump(dict, f)
        print("\nCredentials saved.\n\n")

    def LoadSession():
        chrome_options = Options()
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.instagram.com/")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()

        with open("saved_dictionary.pkl", "rb") as f:
            loaded_dict = pickle.load(f)

        for cookie in loaded_dict:
            driver.add_cookie(
                {
                    "name": cookie["name"],
                    "value": cookie["value"],
                    "path": cookie["path"],
                    "domain": cookie["domain"],
                    "secure": cookie["secure"],
                }
            )

        print("\nLoaded session.\n\n")
