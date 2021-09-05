from scrapinsta.infra.entities.Scrapinsta import Scrapinsta
from getpass import getpass
import pytest


class TestScrapinsta:
    user = input("Enter your username: ")
    password = getpass("Enter your password: ")

    def test_get_credentials(self):
        scrapinsta = Scrapinsta()
        scrapinsta.get_credentials(user="scrapinsta", password="scrapinsta")

        assert scrapinsta.user is not None
        assert scrapinsta.password is not None

    def test_get_credentials_should_throw_an_error_with_invalid_params(self):
        scrapinsta = Scrapinsta()

        with pytest.raises(ValueError) as execinfo:
            scrapinsta.get_credentials(user=True, password=True)

        assert str(execinfo.value) == "Invalid user or password"

    def test_login(self):
        scrapinsta = Scrapinsta()

        scrapinsta.get_credentials(user=self.user, password=self.password)
        scrapinsta.login()

        assert scrapinsta.logged_in is True

    def test_login_should_throw_an_error_without_get_credentials_before(self):
        scrapinsta = Scrapinsta()

        with pytest.raises(ValueError) as execinfo:
            scrapinsta.login()

        assert str(execinfo.value) == "Invalid user or password"

    def test_get_followers(self):
        scrapinsta = Scrapinsta()

        scrapinsta.get_credentials(user=self.user, password=self.password)
        scrapinsta.login()
        followers = scrapinsta.get_followers(user="1matheus4", amount=10)

        assert followers is not None

    def test_get_followings(self):
        scrapinsta = Scrapinsta()

        scrapinsta.get_credentials(user=self.user, password=self.password)
        scrapinsta.login()
        followings = scrapinsta.get_following(user="1matheus4", amount=10)

        assert followings is not None
