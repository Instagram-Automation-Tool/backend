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
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.instagram.com/")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
        print(
            "\nLogin to your Instagram account.\nAfter logging in, your credentials will be stored for later automatic logins.\n\n"
        )
        time.sleep(2)
        # cookies = ",".join(str(v) for v in driver.get_cookies())
        # print(cookies)
        # print(SaveCredentials.ParseCookies(cookies))
        print(driver.get_cookies())

        time.sleep(14)
        f = open("file.pkl", "wb")
        pickle.dump(dict, f)
        f.close()
        print("\nCredentials saved!\n\n")

    def LoadSession(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://www.instagram.com/")

        with open("file.pkl", "wb") as handle:
            data = handle.read()

        print("Data type before reconstruction : ", type(data))

        # reconstructing the data as dictionary
        d = pickle.loads(data)

        print("Data type after reconstruction : ", type(d))
        print(d)

    # def ParseCookies(cookiesString):
    #     parsed = Json.loads(cookiesString)
    #     for x in parsed:
    #         print("This is a cookie: " + x)


# make the app save cookies when logging in
# use saved cookies next time


# driver.add_cookie(
#     {
#         "name": "shbid",
#         "value": '"8430\\05454206727848\\0541695814142:01f738b4a76684cac34e7cc7d7cf272f2270735dc3cfd7bf63d414152a0262a99e25ee27"',
#     }
# )
# driver.add_cookie(
#     {
#         "name": "shbts",
#         "value": '"1664278142\\05454206727848\\0541695814142:01f7f20c3e0e611124988ab3bf8f37ea1ca3d03b4d124219042facdaacf1b5f24c933f71"',
#     }
# )
# {"name": "ig_did", "value": "E0DCE5DB-81E7-482B-A11F-338C4785FFFE"},
# driver.add_cookie(
#     {
#         "name": "sessionid",
#         "value": "54206727848:TYTyOfprsXOho4:14:AYf_tohhKEG7P9mNPUCQuqmDDR2WcyEf4C9EaGO44w",
#     }
# )
# driver.add_cookie(
#     {
#         "name": "rur",
#         "value": '"CLN\\05454206727848\\0541695815104:01f7554abb97e39faafc0ab425f97d65fc3ad7b64959c58e78f964b953ef90a448a93be6"',
#     }
# )
