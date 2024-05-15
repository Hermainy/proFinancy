from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from datetime import date


class Locators:
    EMAIL_FIELD_SELECTOR = (By.NAME, 'email')
    PASSWORD_FIELD_SELECTOR = (By.NAME, 'password')
    BUTTON_SUBMIT_SELECTOR = (By.CSS_SELECTOR, "form button[type='submit']")
    CREATE_BALANCE_SELECTOR = (By.CSS_SELECTOR, ".sc-jlZhRR[mode='secondary']")
    BALANCE_TITLE_SELECTOR = (By.NAME, 'title')
    SELECT_FOUND_SELECTOR = (By.CSS_SELECTOR, "input[placeholder='Выберите валюту']")
    RUSSIAN_RUB_SELECTOR = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[1]')
    BALANCE_SELECTOR = (By.CSS_SELECTOR, "input[name='amount']")
    BALANCE_ICON_SELECTOR = (By.XPATH, "//*[@id='root']/div[1]/div[4]/div[2]/div/div[4]/button")
    COLOR_ICON_SELECTOR = (By.XPATH, "//*[@id='root']/div[1]/div[4]/div[2]/div/div[5]/button")
    BALANCE_ICON_SELECT_SELECTOR = (
        By.XPATH, "//*[@id='root']/div[1]/div[4]/div[2]/div/div[4]/div/div[2]/div[1]")
    COLOR_ICON_SELECT_SELECTOR = (By.CSS_SELECTOR, ".style_colorItem__N2vK5[style='background: rgb(137, 137, 137);'")
    SUBMIT_CREATE_BALANCE_SELECTOR = (By.XPATH, '//*[@id="root"]/div[1]/div[4]/div[2]/div/div[7]/button')
    ADD_OPERATIONS_SELECTOR = (By.XPATH, "//*[@id='root']/div[1]/div[2]/div/main/div[2]/div[1]/div[1]/div[2]/button[2]")
    SUM_FIELD_LOCATOR = (By.CLASS_NAME, "style_inputWithIconInput__PitpE")
    INCOME_BUTTON_SELECTOR = (By.XPATH, "//*[@id='root']/div[1]/div[4]/div[2]/aside/div/div[1]/div[1]/div/div[2]")
    EXPENSE_BUTTON_SELECTOR = (By.XPATH, "//*[@id='root']/div[1]/div[4]/div[2]/aside/div/div[1]/div[1]/div/div[1]")
    BALANCE_NAME_SELECTOR = (By.CSS_SELECTOR, "input[placeholder='Название счета']")
    TRANSACTION_TYPE_SELECTOR = (By.CSS_SELECTOR, "input[placeholder='Начните ввод']")
    BALANCE_NAME_SELECT_SELECTOR = (By.XPATH, "//*[@id='root']/div[1]/div[4]/div[2]/aside/div/div[1]/div[2]/div["
                                              "3]/div[1]/div/div[2]/ul/li")
    TRANSACTION_TYPE_SELECT_SELECTOR = (
        By.XPATH, "//*[@id='root']/div[1]/div[4]/div[2]/aside/div/div[1]/div[2]/div[3]/div[2]/div/div[2]/ul/li[1]")
    CREATE_TRANSACTION_SELECTOR = (By.XPATH, "//*[@id='root']/div[1]/div[4]/div[2]/aside/div/div[1]/div[2]/div["
                                             "7]/button")
    BALANCE_PARAGRAPH_SELECTOR = (
    By.XPATH, "//*[@id='root']/div[1]/div[2]/div/main/div[2]/div[1]/div[1]/div[1]/span/span")


class ProFinancy(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_login_page(self):
        return self.browser.get('https://profinansy.ru/login/')

    def open_wallet_page(self):
        return self.browser.get('https://profinansy.ru/wallet/')

    @property
    def email_field(self):
        return self.find(Locators.EMAIL_FIELD_SELECTOR)

    @property
    def password_field(self):
        return self.find(Locators.PASSWORD_FIELD_SELECTOR)

    @property
    def balance_title_field(self):
        return self.find(Locators.BALANCE_TITLE_SELECTOR)

    @property
    def balance_field(self):
        return self.find(Locators.BALANCE_SELECTOR)

    @property
    def balance(self):
        return self.find(Locators.BALANCE_SELECTOR)

    def balance_value(self, amount):
        self.balance.send_keys(amount)

    def select_russian_rub(self):
        self.find(Locators.RUSSIAN_RUB_SELECTOR).click()

    def balance_field_selector(self, number):
        self.balance_field(number)

    def balance_title_value(self, word):
        self.balance_title_field.send_keys(word)

    def button_submit_click(self):
        self.find(Locators.BUTTON_SUBMIT_SELECTOR).click()

    def create_balance_click(self):
        self.find(Locators.CREATE_BALANCE_SELECTOR).click()

    def select_found_click(self):
        self.find(Locators.SELECT_FOUND_SELECTOR).click()

    def email_field_value(self, word):
        self.email_field.send_keys(word)

    def password_field_value(self, word):
        self.password_field.send_keys(word)

    def balance_icon_click(self):
        self.find(Locators.BALANCE_ICON_SELECTOR).click()

    def balance_icon_select(self):
        self.balance_icon_click()
        self.find(Locators.BALANCE_ICON_SELECT_SELECTOR).click()

    def icon_color_click(self):
        self.find(Locators.COLOR_ICON_SELECTOR).click()

    def icon_color_select(self):
        self.icon_color_click()
        self.find(Locators.COLOR_ICON_SELECT_SELECTOR).click()

    def create_button_click(self):
        self.find(Locators.SUBMIT_CREATE_BALANCE_SELECTOR).click()

    def add_operations_click(self):
        self.find(Locators.ADD_OPERATIONS_SELECTOR).click()

    def enter_sum(self):
        fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
        day_now = date.today().day
        self.find(Locators.SUM_FIELD_LOCATOR).send_keys(fib(day_now))

    def income_click(self):
        self.find(Locators.INCOME_BUTTON_SELECTOR).click()

    def balance_name_select(self):
        self.find(Locators.BALANCE_NAME_SELECTOR).click()
        self.find(Locators.BALANCE_NAME_SELECT_SELECTOR).click()

    def transaction_type_select(self):
        self.find(Locators.TRANSACTION_TYPE_SELECTOR).click()
        self.find(Locators.TRANSACTION_TYPE_SELECT_SELECTOR).click()

    def create_transaction_click(self):
        self.find(Locators.CREATE_TRANSACTION_SELECTOR).click()

    @property
    def amount(self):
        return self.find(Locators.BALANCE_PARAGRAPH_SELECTOR).text
