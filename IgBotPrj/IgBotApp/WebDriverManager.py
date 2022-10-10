from lib2to3.pgen2 import driver
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR, "/gecko")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
)
from selenium.webdriver.support import expected_conditions as EC
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
        WebdriverActions.SaveCookies(driver)
        print("\nCredentials saved.\n\n")

    def LoadSession():
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.instagram.com/")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()

        WebdriverActions.LoadCookies(driver)

        print("\nLoaded session.\n\n")

    def FollowProfile(username):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.instagram.com/" + username)

        WebdriverActions.WaitForElement(
            driver, By.XPATH, "/html/body/div[4]/div/div/button[1]"
        ).click()
        WebdriverActions.LoadCookies(driver)
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]/div/div[1]/button/div",
        ).click()

        print("\Followed " + username + "\n\n")

    def LikePost(link):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.instagram.com/" + link)

        WebdriverActions.LoadCookies(driver)

        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button",
        ).click()

        print("\nLiked post.\n\n")

    # helper functions
    def WaitForElement(driver, by, value):
        wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
            ],
        )

        element = wait.until(
            EC.element_to_be_clickable(
                (
                    by,
                    value,
                )
            )
        )
        return element

    def SaveCookies(driver):
        dict = driver.get_cookies()
        with open("saved_dictionary.pkl", "wb") as f:
            pickle.dump(dict, f)

    def LoadCookies(driver):
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

        driver.refresh()
