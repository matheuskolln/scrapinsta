from time import sleep
from typing import List, Optional

from cryptography.fernet import Fernet
from scrapinsta.infra.providers.Webdriver import Webdriver
from scrapinsta.domain.providers.IWebdriver import IWebdriver
from scrapinsta.domain.entities.IScrapinsta import IScrapinsta


class Scrapinsta(IScrapinsta):
    driver: IWebdriver
    user: str
    password: Optional[bytes]
    crypto: Fernet
    logged_in: bool

    def __init__(self) -> None:
        self.driver = Webdriver()
        self.user = ""
        self.password = None
        self.logged_in = False

        key = Fernet.generate_key()
        self.crypto = Fernet(key)

    def get_credentials(self, user: str, password: str) -> None:
        if (
            not user
            or not password
            or not isinstance(user, str)
            or not isinstance(password, str)
        ):
            raise ValueError("Invalid user or password")

        self.user = user

        bpass = bytes(password, "utf-8")

        self.password = self.crypto.encrypt(bpass)

    def login(self) -> None:
        if not self.user or not self.password:
            raise ValueError("Invalid user or password")

        self.driver.open_url("https://www.instagram.com/accounts/login")
        sleep(5)
        user_input = self.driver.find_element(
            selector='//*[@id="loginForm"]/div/div[1]/div/label/input', type="xpath"
        )
        self.driver.send_keys(user_input, self.user)

        password_input = self.driver.find_element(
            selector='//*[@id="loginForm"]/div/div[2]/div/label/input', type="xpath"
        )
        password = str(self.crypto.decrypt(self.password), "utf-8")
        self.driver.send_keys(password_input, password)

        button = self.driver.find_element(
            selector="//button[@type='submit']", type="xpath"
        )
        self.driver.click(button)
        sleep(8)
        self.driver.open_url("https://www.instagram.com/")
        try:
            user_input = self.driver.find_element(
                selector='//*[@id="loginForm"]/div/div[1]/div/label/input', type="xpath"
            )
            self.logged_in = False
        except:
            self.logged_in = True

    def get_followers(self, user: str, amount: int) -> List[str]:
        if not self.logged_in:
            raise ValueError("Not logged in, please call login() before.")

        self.driver.open_url(f"https://www.instagram.com/{user}/")
        sleep(5)
        followers_button = self.driver.find_element(
            selector='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a',
            type="xpath",
        )
        self.driver.click(followers_button)
        sleep(5)
        followers = []
        for index in range(1, amount):
            follower = self.driver.find_element(
                selector=f"/html/body/div[6]/div/div/div[2]/ul/div/li[{index}]/div/div[2]/div[1]/div/div/span/a",
                type="xpath",
            )
            if follower:
                followers.append(follower.text)

        return followers

    def get_following(self, user: str, amount: int) -> List[str]:
        if not self.logged_in:
            raise ValueError("Not logged in, please call login() before.")

        self.driver.open_url(f"https://www.instagram.com/{user}/")
        sleep(10)
        following_button = self.driver.find_element(
            selector='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a',
            type="xpath",
        )
        self.driver.click(following_button)
        sleep(5)
        following = []
        for index in range(1, amount):
            account = self.driver.find_element(
                selector=f"/html/body/div[6]/div/div/div[2]/ul/div/li[{index}]/div/div[2]/div[1]/div/div/span/a",
                type="xpath",
            )
            if account:
                following.append(account.text)

        return following
