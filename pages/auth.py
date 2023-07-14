import ast
import os
import time

from pages.base import BasePage
from pages.locators import *

'''Создаем класс страницы авторизации'''
class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv('MAIN_URL') or 'https://b2c.passport.rt.ru'
        driver.get(url)
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME_FORM)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.reg_in = driver.find_element(*AuthLocators.AUTH_REG_IN)
        self.VK_btn = driver.find_element(*AuthLocators.AUTH_VK_BTN)
        self.OD_btn = driver.find_element(*AuthLocators.AUTH_OD_BTN)
        self.MAIL_btn = driver.find_element(*AuthLocators.AUTH_MAIL_BTN)
        self.GOOGLE_btn = driver.find_element(*AuthLocators.AUTH_GOOGLE_BTN)
        self.YANDEX_btn = driver.find_element(*AuthLocators.AUTH_YANDEX_BTN)
        self.forgot_pass_btn = driver.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
        self.polz_sogl = driver.find_element(*AuthLocators.AUTH_POLZ_SOGL)
        self.politics = driver.find_element(*AuthLocators.AUTH_POLITICS)




    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def btn_click_enter(self):
        self.btn.click()
        time.sleep(10)

    def enter_reg_page(self):
        self.reg_in.click()
        time.sleep(10)

    def active_tab(self):
        self.active_tab()

    def enter_VK(self):
        self.VK_btn.click()
        time.sleep(2)

    def enter_OD(self):
        self.OD_btn.click()
        time.sleep(2)

    def enter_MAIL(self):
        self.MAIL_btn.click()
        time.sleep(2)

    def enter_GOOGLE(self):
        self.GOOGLE_btn.click()
        time.sleep(2)

    def enter_YANDEX(self):
        self.YANDEX_btn.click()
        time.sleep(2)

    def check_color(self, elem):
        rgba = elem.value_of_css_property('color')
        r, g, b, alpha = ast.literal_eval(rgba.strip('rgba'))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        return hex_value

    def enter_forgot_pass(self):
        self.forgot_pass_btn.click()
        time.sleep(2)

    def enter_back_from_forgot_pass(self):
        self.back_from_forgot_pass.click()
        time.sleep(2)

    def enter_polz_sogl(self):
        self.polz_sogl.click()
        time.sleep(2)

    def enter_politics(self):
        self.politics.click()
        time.sleep(2)

'''Создаем класс страниц регистрации'''
class RegPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.name = driver.find_element(*RegistrationLocators.REG_FIRSTNAME)
        self.last_name = driver.find_element(*RegistrationLocators.REG_LASTNAME)
        self.email = driver.find_element(*RegistrationLocators.REG_ADDRESS)
        self.password = driver.find_element(*RegistrationLocators.REG_PASSWORD)
        self.pass_conf = driver.find_element(*RegistrationLocators.REG_PASS_CONFIRM)
        self.btn = driver.find_element(*RegistrationLocators.REG_REGISTER)

    def enter_name(self, value):
        self.name.send_keys(value)

    def enter_lastname(self, value):
        self.last_name.send_keys(value)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_pass_again(self, value):
        self.pass_conf.send_keys(value)

    def btn_click(self):
        self.btn.click()