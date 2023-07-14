from selenium.webdriver.common.by import By

'''Базовый url страницы авторизации'''
MAIN_URL = 'https://b2c.passport.rt.ru'

'''Создаем класс со всеми используемыми локаторами на странице авторизации'''
class AuthLocators:
    AUTH_USERNAME_FORM = (By.ID, 'username')
    AUTH_PASS = (By.ID, 'password')
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_FORM_ERROR = (By.XPATH, "//span[@id='form-error-message']")
    AUTH_MESS_ERROR = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    AUTH_REG_IN = (By.XPATH, "//a[@id='kc-register']")
    AUTH_REG_IN_TEMP_CODE = (By.ID, 'back_to_otp_btn')
    AUTH_ACTIVE_TAB = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')
    AUTH_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    AUTH_BACK_FROM_FORGOT_PASSWORD = (By.XPATH, '//*[@id="reset-back"]')  # (By.NAME, 'back_to_login')
    AUTH_TEXT_IMAGE = (By.ID, 'captcha')
    AUTH_MESS_EMPTY_PHONE = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    AUTH_VK_BTN = (By.ID, 'oidc_vk')
    AUTH_OD_BTN = (By.ID, 'oidc_ok')
    AUTH_MAIL_BTN = (By.ID, 'oidc_mail')
    AUTH_GOOGLE_BTN = (By.ID, 'oidc_google')
    AUTH_YANDEX_BTN = (By.ID, 'oidc_ya')
    AUTH_POLZ_SOGL = (By.LINK_TEXT, 'пользовательского соглашения')
    AUTH_POLITICS = (By.XPATH, '//*[@id="rt-footer-agreement-link"]/span[1]')

'''Создаем класс со всеми используемыми локаторами на странице регистрации'''
class RegistrationLocators:
    REG_FIRSTNAME = (By.XPATH, "//input[@name='firstName']")
    REG_LASTNAME = (By.XPATH, "//input[@name='lastName']")
    REG_REGION = (By.XPATH, "//input[@autocomplete='new-password']"[0])
    REG_ADDRESS = (By.ID, 'address')
    REG_PASSWORD = (By.ID, 'password')
    REG_PASS_CONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    REG_REGISTER = (By.XPATH, "//button[@name='register']")
    REG_CARD_MODAL = (By.XPATH, "//h2[@class='card-modal__title']")