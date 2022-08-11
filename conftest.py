import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose user_language: en, ru ...")
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    browser_name = request.config.getoption("browser_name")
    if browser_name is None:
        browser_name = "chrome"

    if user_language is None:
        user_language = "en"

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_argument("-disable-features=RendererCodeIntegrity")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

    # pytest -s -v --browser_name=chrome test_parser.py
    # pytest --language=es test_items.py

