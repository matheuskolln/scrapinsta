from scrapinsta.infra.providers.Webdriver import Webdriver
import pytest


class TestWebdriver:
    def test_quit_webdriver(self):
        webdriver = Webdriver()
        response = webdriver.quit_driver()

        assert response is True

    def test_open_url(self):
        webdriver = Webdriver()
        webdriver.open_url("https://www.github.com/matheuskolln/scrapinsta")
        webdriver.quit_driver()

    def test_open_url_should_throw_error_when_url_is_not_valid(self):
        webdriver = Webdriver()

        with pytest.raises(TypeError) as execinfo:
            webdriver.open_url(1234)

        webdriver.quit_driver()

        assert str(execinfo.value) == "URL need to be a string!"

    def test_find_element_with_css(self):
        webdriver = Webdriver()
        webdriver.open_url("https://www.github.com/matheuskolln/scrapinsta")
        element = webdriver.find_element(selector="a.url.fn", type="css")

        assert element is not None
        assert element.text == "matheuskolln"

        webdriver.quit_driver()

    def test_find_element_with_xpath(self):
        webdriver = Webdriver()
        webdriver.open_url("https://www.github.com/matheuskolln/scrapinsta")
        element = webdriver.find_element(
            selector='//*[@id="repository-container-header"]/div[1]/div/h1/span[1]/a',
            type="xpath",
        )

        assert element is not None
        assert element.text == "matheuskolln"

        webdriver.quit_driver()

    def test_find_element_should_throw_an_error_with_invalid_type(self):
        webdriver = Webdriver()
        webdriver.open_url("https://www.github.com/matheuskolln/scrapinsta")

        with pytest.raises(ValueError) as execinfo:
            element = webdriver.find_element(selector="a.url.fn", type="invalid")
            assert element is None

        assert (
            str(execinfo.value)
            == "Type is not supported! Actually need to be 'css' or 'xpath'..."
        )

        webdriver.quit_driver()

    def test_send_keys(self):
        webdriver = Webdriver()
        webdriver.open_url("https://github.com/search")
        input = webdriver.find_element(
            selector='//*[@id="search_form"]/div/div/input[1]', type="xpath"
        )
        webdriver.send_keys(element=input, value="Scrapinsta")
        webdriver.quit_driver()

    def test_send_keys_should_throw_an_error_with_invalid_element(self):
        webdriver = Webdriver()
        webdriver.open_url("https://github.com/search")

        with pytest.raises(TypeError) as execinfo:
            webdriver.send_keys(element="invalid", value="Scrapinsta")

        assert (
            str(execinfo.value)
            == "Element need to be found before send_keys, please find element first!"
        )

        webdriver.quit_driver()

    def test_click(self):
        webdriver = Webdriver()
        webdriver.open_url("https://github.com/search")

        input = webdriver.find_element(
            selector='//*[@id="search_form"]/div/div/input[1]', type="xpath"
        )
        webdriver.send_keys(element=input, value="Scrapinsta")

        button = webdriver.find_element(
            selector='//*[@id="search_form"]/div/button', type="xpath"
        )
        webdriver.click(element=button)

        webdriver.quit_driver()

    def test_click_should_throw_an_error_with_invalid_element(self):
        webdriver = Webdriver()
        webdriver.open_url("https://github.com/search")

        with pytest.raises(TypeError) as execinfo:
            webdriver.click(element="invalid")

        assert (
            str(execinfo.value)
            == "Element need to be found before click, please find element first!"
        )

        webdriver.quit_driver()
