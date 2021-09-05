from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from scrapinsta.domain.providers.IWebdriver import IWebdriver


class Webdriver(IWebdriver):
    driver: WebDriver
    options = webdriver.ChromeOptions

    @property
    def client(self) -> Optional[webdriver.Chrome]:
        return self.driver

    def __init__(self):
        self.options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=self.options
        )
        self.clear_cache()

    def open_url(self, url: str) -> None:
        if self.driver is None:
            raise Exception("Webdriver is not opened, please get_driver first!")

        if not isinstance(url, str):
            raise TypeError("URL need to be a string!")

        self.driver.get(url)

    def quit_driver(self) -> Optional[bool]:
        if self.driver is None:
            return False

        self.driver.quit()
        return True

    def find_element(self, selector: str, type: str) -> WebElement:
        if self.driver is None:
            raise Exception("Webdriver is not opened, please get_driver first!")

        if type not in ("css", "xpath"):
            raise ValueError(
                "Type is not supported! Actually need to be 'css' or 'xpath'..."
            )

        if type == "css":
            element = self.driver.find_element_by_css_selector(selector)
            return element

        element = self.driver.find_element_by_xpath(selector)
        return element

    def send_keys(self, element: WebElement, value: str) -> None:
        if self.driver is None:
            raise Exception("Webdriver is not opened, please get_driver first!")

        if not isinstance(element, WebElement):
            raise TypeError(
                "Element need to be found before send_keys, please find element first!"
            )

        element.send_keys(value)

    def click(self, element: WebElement) -> None:
        if self.driver is None:
            raise Exception("Webdriver is not opened, please get_driver first!")

        if not isinstance(element, WebElement):
            raise TypeError(
                "Element need to be found before click, please find element first!"
            )

        element.click()

    def clear_cache(self) -> None:
        if self.driver is None:
            raise Exception("Webdriver is not opened, please get_driver first!")

        self.driver.delete_all_cookies()
