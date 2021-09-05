from abc import ABC, abstractmethod
from typing import List


class IScrapinsta(ABC):
    @abstractmethod
    def login(self) -> None:
        pass

    @abstractmethod
    def get_followers(self, user: str, amount: int) -> List[str]:
        pass

    @abstractmethod
    def get_following(self, user: str, amount: int) -> List[str]:
        pass
