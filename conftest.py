from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import pytest


@pytest.fixture
def browser():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser

