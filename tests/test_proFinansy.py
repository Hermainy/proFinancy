import time

from pages.proFinansy import ProFinancy
import pytest
import allure


@allure.feature('UserStoryCase')
def test_proFinancy(browser):
    with allure.step('Open login page'):
        page = ProFinancy(browser)
        page.open_login_page()
        time.sleep(2)
    with allure.step('Authorization with email and password'):
        page.email_field_value('andreiermilov@bk.ru')
        page.password_field_value('TESTpassword123')
        page.button_submit_click()
        time.sleep(2)
    with allure.step('Create balance'):
        page.open_wallet_page()
        page.create_balance_click()
        page.balance_title_value('BALANCE')
        page.select_found_click()
        page.select_russian_rub()
        page.balance_value('0')
        page.balance_icon_select()
        page.icon_color_select()
        page.create_button_click()
    with allure.step('add income transaction'):
        page.add_operations_click()
        page.income_click()
        page.enter_sum()
        page.balance_name_select()
        page.transaction_type_select()
    with allure.step('add expense transaction'):
        page.create_transaction_click()
        time.sleep(2)
        page.add_operations_click()
        page.enter_sum()
        page.balance_name_select()
        page.transaction_type_select()
        page.create_transaction_click()
    with allure.step('check balance'):
        assert page.amount == "0 ₽"
