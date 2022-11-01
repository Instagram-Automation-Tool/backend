from lib2to3.pgen2 import driver
import os

from IgBotApp.models import InstagramAccount


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR, "/gecko")

from . import dev_options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    StaleElementReferenceException,
)
import urllib.parse
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle


class WebdriverActions:
    def StoreLoginCredentials(username,password):
        driver = WebdriverActions.GetWebDriver()
        # driver.set_window_size(500, 695)
        driver.get("https://www.instagram.com/")
        # driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
        time.sleep(20)

        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]").click()
        except:
            print("NO COOKIES")

         
        username_input = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        password_input = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        

        username_input.send_keys(username)
        password_input.send_keys(password)

        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "//button[@type='submit']"
        ).click()

        print(
            "\nLogin to your Instagram account.\nAfter 20 seconds, your credentials will be stored for later automatic logins.\n\n"
        )
        time.sleep(20)
        # replace mock data with real acount data
        bruh = InstagramAccount(
            expandiId=3,
            username="test3123",
            cookies=driver.get_cookies(),
            proxy="1.1.1.1:1234",
        )
        bruh.save()
        WebdriverActions.SaveCookies(driver)
        print("\nCredentials saved.\n\n")

    def LoadSession():
        driver = WebdriverActions.GetWebDriver()
        driver.get("https://www.instagram.com/")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()

        WebdriverActions.LoadCookies(driver)
        print("\nLoaded session.\n\n")

    def FollowProfile(link):
        driver = WebdriverActions.GetWebDriver()
        driver.get(link)

        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]",
        ).click()
        WebdriverActions.LoadCookies(driver)
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button/div/div",
        ).click()

        print("\nFollowed " + link.split("/")[3] + "\n\n")

    def LikePost(link):
        driver = WebdriverActions.GetWebDriver()
        driver.get(urllib.parse.unquote(link))

        WebdriverActions.LoadCookies(driver)
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button",
        ).click()
        print("\nLiked post.\n\n")

    def CommentOnPost(link, comment):
        driver = WebdriverActions.GetWebDriver()
        driver.get(link)
        WebdriverActions.LoadCookies(driver)

        webElement = WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea",
        )
        webElement.click()
        webElement = WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea",
        )

        webElement.send_keys(comment + Keys.ENTER)

        print("\nCommented on post.\n\n")

    # helper functions
    def GetWebDriver():
        chrome_options = WebdriverActions.GetOptions()
        return webdriver.Chrome(
            BASE_DIR + "/chromedriver", chrome_options=chrome_options
        )

    def GetOptions():
        chromeOptions = Options()
        if dev_options.Headless:
            chromeOptions.add_argument("--headless")
        if dev_options.Proxyless != True:
            chromeOptions.add_argument("--proxy-server=%s" % "hostname" + ":" + "port")
        if dev_options.KeepWindowOpenOnFinish == True:
            chromeOptions.add_experimental_option("detach", True)
        return chromeOptions

    def WaitForElement(driver, by, value):
        wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                ElementNotVisibleException,
                ElementNotSelectableException,
                StaleElementReferenceException,
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
