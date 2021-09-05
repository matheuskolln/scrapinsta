from abc import ABC, abstractmethod
from typing import Optional

from selenium.webdriver.remote.webelement import WebElement


class IWebdriver(ABC):
    """Abstract class for webdriver."""

    @property
    @abstractmethod
    def client(self) -> Optional[object]:
        pass

    @abstractmethod
    def __init__(self, config) -> None:
        pass

    @abstractmethod
    def quit_driver(self) -> Optional[bool]:
        pass

    @abstractmethod
    def open_url(self, url: str) -> None:
        pass

    @abstractmethod
    def find_element(self, selector: str, type: str) -> WebElement:
        pass

    @abstractmethod
    def send_keys(self, element: WebElement, value: str) -> None:
        pass

    @abstractmethod
    def click(self, element: WebElement) -> None:
        pass
