from typing import Optional, Type
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from scrapinsta.domain.providers.IWebdriver import IWebdriver

OPTIONS = {
    "arguments": [
        "--ignore-certificate-errors",
        '--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"',
    ]
}


class Webdriver(IWebdriver):
    driver: webdriver
    options = webdriver.ChromeOptions

    @property
    def client(self) -> Optional[webdriver.Chrome]:
        return self.driver

    def __init__(self):
        self.options = webdriver.ChromeOptions()

        for option in OPTIONS["arguments"]:
            self.options.add_argument(option)

        self.driver = None

    def open_url(self, url: str) -> None:
        if self.driver is None:
            raise Exception("Webdriver is not opened, please get_driver first!")

        if not isinstance(url, str):
            raise TypeError("URL need to be a string!")

        self.driver.get(url)

    def get_driver(self) -> bool:
        if self.driver is None:
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=self.options
            )
            return True

        return False

    def quit_driver(self) -> Optional[bool]:
        if self.driver is None:
            return False

        self.driver.quit()
        self.driver = None
        return True

    def find_element(self, selector: str, type: str) -> Optional[object]:
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
