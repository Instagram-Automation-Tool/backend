import requests
from re import search
import re
import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib.parse
from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementNotSelectableException,
    StaleElementReferenceException,
)
from enum import Enum
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from . import dev_options
from lib2to3.pgen2 import driver
from lib2to3.pgen2.token import NEWLINE
from sys import platform
import datetime
from .thresholds import Thresholds
import pytz

# from msilib.schema import Environment
import os

from IgBotApp.models import InstagramAccount, Interaction, IGTarget

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR, "/gecko")

# index 0 = desktop
# index 1 = mobile
USER_AGENTS = [
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.11",
]

# todo: add identifiers to paramaters ex: def FUNC(input: String)

# todo: implement function: WaitForOption(), waits for multiple xpath possibilities


class WebdriverActions:
    # todo: implement detection if password is incorrect
    def StoreLoginCredentials(username, password):
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[0])
        driver.get("https://www.instagram.com/")

        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]",
        ).click()

        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
        ).send_keys(username)
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
        ).send_keys(password)
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button",
        ).click()

        time.sleep(4)

        driver.get("https://instagram.com/" + username)

        bio, followersCount, followingCount, postsCount, profilePictureURL = [
            "error",
            "error",
            "error",
            "error",
            "error",
        ]

        try:
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
                    "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a/div/span",
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
        except:
            try:
                bio = WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/span",
                ).text
                followersCount = int(
                    WebdriverActions.WaitForElement(
                        driver,
                        By.XPATH,
                        "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span",
                    ).text
                )
                followingCount = int(
                    WebdriverActions.WaitForElement(
                        driver,
                        By.XPATH,
                        "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/div/span",
                    ).text
                )
                postsCount = int(
                    WebdriverActions.WaitForElement(
                        driver,
                        By.XPATH,
                        "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[1]/div/span",
                    ).text
                )
                profilePictureURL = WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/div/div/span/img",
                ).get_attribute("src")
            except:
                bio = WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[3]/span",
                ).text
                followersCount = int(
                    WebdriverActions.WaitForElement(
                        driver,
                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span/span",
                    ).text
                )
                followingCount = int(
                    WebdriverActions.WaitForElement(
                        driver,
                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a/div/span/span",
                    ).text
                )
                postsCount = int(
                    WebdriverActions.WaitForElement(
                        driver,
                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[1]/div/span/span",
                    ).text
                )
                # make try get profilepicurl function and more
                profilePictureURL = WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/div/div/div/button/img",
                ).get_attribute("src")

        WebdriverActions.CreateAccount(
            driver=driver,
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
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
        driver.get("https://www.instagram.com/")

        WebdriverActions.LoadCookies(
            driver,
            username,
        )

        driver.get("https://instagram.com/" + username)

    def FetchNotifications(username):
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
        driver.get("https://www.instagram.com/accounts/activity")
        WebdriverActions.LoadCookies(driver, username)
        appId = ""
        for entry in driver.get_log("performance"):
            if "X-IG-App-ID" in entry["message"]:
                appId = re.findall(
                    'X-IG-App-ID":"(.*?)"',
                    "".join(entry["message"]),
                )[0]
                break

        session = requests.Session()
        cookies = (
            InstagramAccount.objects.all().values("cookies").get(username=username)
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

        session.headers.update({"x-ig-app-id": appId})
        response = session.get("https://www.instagram.com/api/v1/news/inbox/")
        responseJson = response.json()
        counts = responseJson["counts"]
        new_stories = responseJson["new_stories"]
        old_stories = responseJson["old_stories"]
        httpResponse = {
            "counts": counts,
            "new_stories": new_stories,
            "old_stories": old_stories,
        }
        return json.dumps(httpResponse)

    def FollowProfile(target, username):
        if not WebdriverActions.CheckThresholds(
            Interaction.InteractionType.FOLLOW, username, Thresholds.follow_limit
        ):
            return "Threshold reached"
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
        driver.get("https://www.instagram.com/" + target)

        WebdriverActions.LoadCookies(driver, username)
        try:
            if (
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div[1]",
                ).text
                == "Following"
            ):
                return WebdriverActions.LogInteraction(
                    Interaction.InteractionType.UNKNOWN,
                    target,
                    username,
                    "Tried to follow profile, already following.",
                )
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button",
            ).click()
        except:
            if (
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div/div",
                ).text
                == "Following"
            ):
                return WebdriverActions.LogInteraction(
                    Interaction.InteractionType.UNKNOWN,
                    target,
                    username,
                    "Tried to follow profile, already following.",
                )
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button",
            ).click()

        driver.quit
        return WebdriverActions.LogInteraction(
            Interaction.InteractionType.FOLLOW, target, username, "Followed profile"
        )

    def LikePost(link, username):
        if not WebdriverActions.CheckThresholds(
            Interaction.InteractionType.LIKE, username, Thresholds.like_limit
        ):
            return "Threshold reached"
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
        driver.get(urllib.parse.unquote(link))

        WebdriverActions.LoadCookies(driver, username)
        targetUsername = WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div[1]/a",
        ).text
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/section[1]/span[1]/button",
        ).click()

        return WebdriverActions.LogInteraction(
            Interaction.InteractionType.LIKE,
            targetUsername,
            username,
            "Liked post.",
            {"Link": link},
        )

    def CommentOnPost(link, comment, username):
        if not WebdriverActions.CheckThresholds(
            Interaction.InteractionType.COMMENT, username, Thresholds.comment_limit
        ):
            return "Threshold reached"
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
        driver.get(link)
        WebdriverActions.LoadCookies(driver, username)
        targetUsername = WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div[1]/a",
        ).text
        webElement = WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea",
        )
        webElement.click()
        webElement = WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea",
        )

        webElement.send_keys(comment + Keys.ENTER)
        return WebdriverActions.LogInteraction(
            Interaction.InteractionType.COMMENT,
            targetUsername,
            username,
            "Commented on post.",
            {"Link": link, "Comment": comment},
        )

    def CommentOnProfilePosts(targetUsername, comments, like, username):
        if not WebdriverActions.CheckThresholds(
            Interaction.InteractionType.COMMENT,
            username,
            Thresholds.comment_limit,
        ):
            return "Threshold reached"
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
        driver.get("https://instagram.com/" + targetUsername)
        interactions = []
        WebdriverActions.LoadCookies(driver, username)
        # First Post
        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a",
        ).click()
        if not WebdriverActions.CheckThresholds(
            Interaction.InteractionType.COMMENT, username, Thresholds.comment_limit
        ):
            return "Threshold reached"
        if len(comments) > 0:
            if like:
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button",
                ).click()
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea",
            ).click()
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea",
            ).send_keys(comments[0] + Keys.RETURN)
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button",
            ).click()
            interactions.append(
                WebdriverActions.LogInteraction(
                    Interaction.InteractionType.COMMENT,
                    targetUsername,
                    username,
                    "Commented on post.",
                    {"Comment": comments[0], "alsoLike": like},
                )
            )

        if len(comments) > 1:
            for comment in comments[1:]:
                if not WebdriverActions.CheckThresholds(
                    Interaction.InteractionType.COMMENT,
                    username,
                    Thresholds.comment_limit,
                ):
                    return "Threshold reached"
                if like:
                    WebdriverActions.WaitForElement(
                        driver,
                        By.XPATH,
                        "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button",
                    ).click()
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea",
                ).click()
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea",
                ).send_keys(comment + Keys.RETURN)
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button",
                ).click()
                interactions.append(
                    WebdriverActions.LogInteraction(
                        Interaction.InteractionType.COMMENT,
                        targetUsername,
                        username,
                        "Commented on post.",
                        {"Comment": comment, "alsoLike": like},
                    )
                )
        return interactions

    # paramaters, in order: array of target profile usernames, amount of posts to like (if 0, it will like all posts on profile), array of comments to be used on profiles, bool like posts or not, bool follow or not, messages array with messages to send to profiles, username param (login username)
    def FollowUsernames(targetUsernames, username):
        interactions = []
        for targetUsername in targetUsernames:
            interactions.append(
                WebdriverActions.FollowProfile(targetUsername, username)
            )
        return interactions

    def LikePostsOfUsernamesProfiles(targetUsernames, count, username):
        interactions = []
        for targetUsername in targetUsernames:
            if not WebdriverActions.CheckThresholds(
                Interaction.InteractionType.LIKE,
                username,
                Thresholds.like_limit,
            ):
                return "Threshold reached"
            driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
            driver.get("https://instagram.com/")
            WebdriverActions.LoadCookies(driver, username)
            driver.get("https://instagram.com/" + targetUsername)
            try:
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a",
                ).click()
            except:
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a",
                ).click()
            interactions.append(
                WebdriverActions.LogInteraction(
                    Interaction.InteractionType.LIKE,
                    targetUsername,
                    username,
                    "Liked post.",
                    {"Link": driver.current_url},
                )
            )
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button",
            ).click()
            WebdriverActions.WaitForElement(
                driver,
                By.XPATH,
                "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button",
            ).click()

            for _ in range(int(count) - 1):
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button",
                ).click()
                interactions.append(
                    WebdriverActions.LogInteraction(
                        Interaction.InteractionType.LIKE,
                        targetUsername,
                        username,
                        "Liked post.",
                        {"Link": driver.current_url},
                    )
                )
                WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button",
                ).click()

            driver.quit()
        return interactions

    class HashtagScrapingOptions(Enum):
        TOP_POSTS = 0  # only top posts
        RANDOM_POSTS = 1  # random posts
        ALL_POSTS = 2  # all posts

    def ScrapeHashtag(
        hashtag,
        username,
        noOfFollowersToScrape=100000,
        noOfPostsToScrape=100000,
        hashtagScrapingOption=2,
    ):
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
        driver.get("https://www.instagram.com/explore/tags/" + hashtag)
        appId = ""
        for entry in driver.get_log("performance"):
            if "X-IG-App-ID" in entry["message"]:
                appId = re.findall(
                    'X-IG-App-ID":"(.*?)"',
                    "".join(entry["message"]),
                )[0]
                break
        session = requests.Session()
        session.headers.update({"x-ig-app-id": appId})
        response = session.get(
            "https://www.instagram.com/api/v1/tags/logged_out_web_info/?tag_name="
            + hashtag
        )
        responseJson = response.json()
        shortCodes = []
        if hashtagScrapingOption == 0 or hashtagScrapingOption == 2:
            for post in responseJson["data"]["hashtag"]["edge_hashtag_to_top_posts"][
                "edges"
            ]:
                shortCodes.append(post["node"]["shortcode"])
        if hashtagScrapingOption > 0:
            for post in responseJson["data"]["hashtag"]["edge_hashtag_to_media"][
                "edges"
            ]:
                shortCodes.append(post["node"]["shortcode"])
        scrapedUsernames = []
        WebdriverActions.LoadCookies(
            driver,
            username,
        )
        noPostsScraped = 0
        for shortCode in shortCodes:
            if len(scrapedUsernames) >= noOfFollowersToScrape:
                return scrapedUsernames
            if noPostsScraped >= noOfPostsToScrape:
                return scrapedUsernames
            usernames = WebdriverActions.ScrapeComments(driver, shortCode, username)
            for username in usernames:
                scrapedUsernames.append(username)
            noPostsScraped += 1
        return scrapedUsernames

    def ScrapeComments(driver, shortCode, username):
        driver.get("https://www.instagram.com/p/" + shortCode)

        WebdriverActions.WaitForElement(
            driver,
            By.XPATH,
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div/article/div/div[2]/div/div[2]/div[1]/div/div[2]/a",
        ).click()
        howManyTimesToScrollAndLoad = 12
        try:
            while howManyTimesToScrollAndLoad > 0:
                time.sleep(2)
                driver.execute_script("window.scrollBy(0,2000)")
                el = WebdriverActions.WaitForElement(
                    driver,
                    By.XPATH,
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/ul/li/div/button",
                )
                if el != None:
                    el.click()
                else:
                    break
                howManyTimesToScrollAndLoad -= 1
        finally:
            ids = []
            for entry in driver.get_log("performance"):
                if search(
                    re.escape("/comments/?can_support_threading=true"), entry["message"]
                ):
                    if (
                        json.loads(entry["message"])["message"]["params"].get(
                            "response"
                        )
                        is not None
                    ):
                        for userField in json.loads(
                            driver.execute_cdp_cmd(
                                "Network.getResponseBody",
                                {
                                    "requestId": json.loads(entry["message"])[
                                        "message"
                                    ]["params"]["requestId"]
                                },
                            )["body"]
                        )["comments"]:
                            if userField["user"]["username"] in ids:
                                continue
                            ids.append(userField["user"]["username"])
        return ids

    def ScrapeFollowers(link, amount, username):
        driver = WebdriverActions.GetWebDriver(USER_AGENTS[1])
        driver.get(urllib.parse.unquote(link))
        driver.get("https://www.instagram.com/")

        WebdriverActions.LoadCookies(
            driver,
            username,
        )
        driver.get(link + "/followers/")
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
                for user in usersJson:
                    users.append(user["username"])

                return users
        driver.quit()
        print("\nScraped followers.\n\n")

    # helper functions

    def DetectOS():
        if platform == "darwin":
            return "/chromedriver"
        return "chromedrive"

    def LogInteraction(
        interactionType,
        targetUsername,
        loggedInAs,
        context,
        data=None,
    ):
        foundBy = InstagramAccount.objects.get(username=loggedInAs)
        target = IGTarget.objects.get_or_create(
            username=targetUsername, foundBy=foundBy
        )
        interaction = Interaction(
            reachedWhileLoggedInAs=foundBy,
            reachedAccount=target[0],
            context=context,
            interactionType=interactionType,
        )
        if data is not None:
            interaction.data = data
        interaction.save()
        return interaction

    def CheckThresholds(interactionType, username, limit):
        date_from = datetime.datetime.now().astimezone(pytz.utc) - datetime.timedelta(
            hours=1
        )
        interactionCount = Interaction.objects.filter(
            reachedWhileLoggedInAs=InstagramAccount.objects.get(username=username),
            interactionType=interactionType,
            reachedAt__range=(date_from, datetime.datetime.now()),
        ).count()
        if interactionCount < limit:
            return True
        return False

    def GetWebDriver(userAgent):
        chromeOptions = WebdriverActions.GetOptions(userAgent)
        caps = DesiredCapabilities.CHROME
        caps["goog:loggingPrefs"] = {"performance": "ALL"}
        return webdriver.Chrome(
            ChromeDriverManager().install(),
            desired_capabilities=caps,
            chrome_options=chromeOptions,
        )

    def GetOptions(userAgent):
        chromeOptions = Options()
        chromeOptions.add_argument("--window-size=1020,1020")
        if dev_options.Headless:
            chromeOptions.add_argument("--headless")
        if dev_options.Proxyless != True:
            chromeOptions.add_argument("--proxy-server=%s" % "hostname" + ":" + "port")
        if dev_options.KeepWindowOpenOnFinish == True:
            chromeOptions.add_experimental_option("detach", True)
        chromeOptions.add_argument(userAgent)
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

        try:
            element = None
            element = wait.until(
                EC.element_to_be_clickable(
                    (
                        by,
                        value,
                    )
                )
            )
        finally:
            return element

    def CreateAccount(
        driver,
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
        print("New account!")
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
