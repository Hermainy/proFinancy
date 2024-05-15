from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args, time=20):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(args),
                                                       message=f"Can't find element by locator {args}")

    def finds(self, args, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(args),
                                                       message=f"Can't find elements by locator {args}")
