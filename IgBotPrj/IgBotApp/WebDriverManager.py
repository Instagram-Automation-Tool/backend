from lib2to3.pgen2 import driver
from lib2to3.pgen2.token import NEWLINE
# from msilib.schema import Environment
import os

from pytz import common_timezones_set

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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import json
import re
from re import search
import requests

# todo: add identifiers to paramaters ex: def FUNC(input: String)


class WebdriverActions:
    # todo: implement detection if password is incorrect
    def StoreLoginCredentials(username, password):
        driver = WebdriverActions.GetWebDriver()
        driver.get("https://www.instagram.com/")

        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div[1]/div/button",
        ).click()

        WebdriverActions.WaitForElement(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div[2]/div[3]/button[1]").click()

        WebdriverActions.WaitForElement(
            driver, By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div[2]/form/div[1]/div[3]/div/label/input"
        ).send_keys(username)
        password_input = WebdriverActions.WaitForElement(
            driver, By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div[2]/form/div[1]/div[4]/div/label/input"
        ).send_keys(password + Keys.RETURN)

        time.sleep(3)
        driver.get("https://instagram.com/" + username)

        bio = WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]/div",
        ).text
        followersCount = int(
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div/span",
            ).text
        )
        followingCount = int(
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a/div/span"
            ).text
        )
        postsCount = int(
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[1]/div/span",
            ).text
        )
        profilePictureURL = WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/div/div/span/img",
        ).get_attribute("src")

        WebdriverActions.CreateAccount(
            driver=driver,
            expandiId=69,
            username=username,
            password=password,
            cookies=driver.get_cookies(),
            proxy="1231:1232",
            followerCount=followersCount,
            followingCount=followingCount,
            profilePictureURL=profilePictureURL,
            postsCount=postsCount,
            bio=bio,
        )

        print("\nCredentials saved.\n\n")


    def LoadSession(username):
        driver = WebdriverActions.GetWebDriver()
        driver.get("https://www.instagram.com/")

        WebdriverActions.LoadCookies(
            driver,
            username,
        )

        driver.get("https://instagram.com/" + username)
        print()

        print("\nLoaded session.\n\n")

    def FollowProfile(link, username):
        driver = WebdriverActions.GetWebDriver()
        driver.get(link)

        WebdriverActions.LoadCookies(driver, username)
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button/div"
        ).click()


        print("\nFollowed " + link.split("/")[3] + "\n\n")

    def LikePost(link, username):
        driver = WebdriverActions.GetWebDriver()
        driver.get(urllib.parse.unquote(link))

        WebdriverActions.LoadCookies(driver, username)
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button",
        ).click()
        print("\nLiked post.\n\n")

    def CommentOnPost(link, comment, username):
        driver = WebdriverActions.GetWebDriver()
        driver.get(link)
        WebdriverActions.LoadCookies(driver, username)

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

    def CommentOnProfilePosts(targetUsername, comments, like, username):
        driver = WebdriverActions.GetWebDriver()
        driver.get('https://instagram.com/'+targetUsername)
        WebdriverActions.LoadCookies(driver, username)
        # First Post
        WebdriverActions.WaitForElement(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div").click()

        if(len(comments)>0):
            for comment in comments:
                if(like):
                    WebdriverActions.WaitForElement(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
                WebdriverActions.WaitForElement(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").click()
                WebdriverActions.WaitForElement(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").send_keys(comment + Keys.RETURN)
                WebdriverActions.WaitForElement(driver, By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button").click()

        return comments       

    def ScrapeFollowers(link, amount, username):
        driver = WebdriverActions.GetWebDriver()
        driver.get(urllib.parse.unquote(link))
        driver.get("https://www.instagram.com/")

        WebdriverActions.LoadCookies(
            driver,
            username,
        )
        driver.get(link+"followers/")

        ids = []
        appIds = []
        for entry in driver.get_log("performance"):
            if search("target_id=", entry["message"]):
                id = re.findall(
                    'target_id=(.*?)\\"',
                    "".join(entry["message"]),
                )
                appId = re.findall(
                    'X-IG-App-ID":"(.*?)"',
                    "".join(entry["message"]),
                )

                if len(id) > 0:
                    if id not in ids:
                        ids.append(id)
                if len(appId) > 0:
                    if appId not in appIds:
                        appIds.append(appId)

        users = []

        for appId in appIds:
            for id in ids:
                session = requests.Session()

                cookies = (
                    InstagramAccount.objects.all()
                    .values("cookies")
                    .get(username=username)
                )

                jar = requests.cookies.RequestsCookieJar()
                for cookie in cookies["cookies"]:
                    jar.set(
                        cookie["name"],
                        cookie["value"],
                        domain=cookie["domain"],
                        path=cookie["path"],
                    )

                session.cookies = jar

                # look for next_max_id
                # look for string that looks like current id

                session.headers.update({"x-ig-app-id": appId[0]})
                response = session.get(
                    "https://www.instagram.com/api/v1/friendships/"
                    + id[0]
                    + "/followers/?count="
                    + amount
                    + "&search_surface=follow_list_page"
                )
                usersJson = response.json()["users"]
                print(usersJson[0])
                for user in usersJson:
                    users.append(user["username"])

                return json.dumps(users)
        driver.quit()
        print("\nScraped followers.\n\n")

    # helper functions
    def GetWebDriver():
        chrome_options = WebdriverActions.GetOptions()
        chrome_options.add_argument("--window-size=1020,1020")
        caps = DesiredCapabilities.CHROME
        # as per latest docs
        caps["goog:loggingPrefs"] = {"performance": "ALL"}

        return webdriver.Chrome(
            BASE_DIR + "/chromedriver.exe",
            desired_capabilities=caps,
            chrome_options=chrome_options,
        )

    def GetOptions():
        chromeOptions = Options()
        if dev_options.Headless:
            chromeOptions.add_argument("--headless")
        if dev_options.Proxyless != True:
            chromeOptions.add_argument("--proxy-server=%s" % "hostname" + ":" + "port")
        if dev_options.KeepWindowOpenOnFinish == True:
            chromeOptions.add_experimental_option("detach", True)
        chromeOptions.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.11")
        return chromeOptions

    def WaitForElement(driver, by, value):
        wait = WebDriverWait(
            driver,
            timeout=20,
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

    def CreateAccount(
        driver,
        expandiId,
        username,
        password,
        cookies,
        proxy,
        bio,
        followerCount,
        followingCount,
        postsCount,
        profilePictureURL,
    ):
        account = InstagramAccount(
            expandiId=69,
            username=username,
            password=password,
            cookies=cookies,
            proxy=proxy,
            bio=bio,
            followerCount=followerCount,
            followingCount=followingCount,
            postsCount=postsCount,
            profilePictureURL=profilePictureURL,
        )
        print("New account! ExpandiId:", expandiId)
        account.save()

    def LoadCookies(driver, username):
        cookies = (
            InstagramAccount.objects.all().values("cookies").get(username=username)
        )
        for cookie in cookies["cookies"]:
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
