import pytest

from pages.auth import *
from pages.locators import *
from pages.settings import *
from conftest import *
'''1. Перед началом проведения тестов необходимо в файле settings.py указать 
своии валидный имейл, телефон и пароль от личного кабинета
   3. В файле conftest.py указать путь к дврайверу хром
   2. При появлении ошибок с капчой вводить код с картинки вручную'''

'''Тест авторизации с валидным имейлом и паролем'''
def test_auth_page_valid_email_valid_pass_authorization(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    time.sleep(15)
    page.btn_click_enter()
    assert page.get_relative_link() == '/account_b2c/page'  # проверка входа в личный кабинет


'''Тест авторизации с невалидными данными'''
@pytest.mark.parametrize('username_form', [invalid_phone, invalid_email, invalid_login, invalid_LS],
                         ids=['invalid_phone & invalid_password',
                              'invalid_email & invalid_password',
                              'invalid_login & invalid_password',
                              'invalid_LS & invalid_password'])
def test_auth_page_invalid_data(browser, username_form):
    page = AuthPage(browser)
    page.enter_username(username_form)
    page.enter_password(password)
    time.sleep(15)
    page.btn_click_enter()

    browser.implicitly_wait(5)
    error_message = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_message.text == 'Неверный логин или пароль' and page.check_color(forgot_pass) == '#ff4f12'  # Проверяем появление сообщения об ошибке и измениние цвета надписи "Забыл пароль"


'''Тест авторизации с валидной почтой и невалидным паролем'''
def test_auth_page_valid_email_invalid_pass_authorization(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(invalid_password)
    time.sleep(15)
    page.btn_click_enter()
    browser.implicitly_wait(2)

    error_message = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_message.text == 'Неверный логин или пароль' and page.check_color(forgot_pass) == '#ff4f12' # Проверяем появление сообщения об ошибке и измениние цвета надписи "Забыл пароль"


'''Тест авторизации с невалидной почтой и валидным паролем'''
def test_auth_page_invalid_email_valid_pass_authorization(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(invalid_password)
    time.sleep(15)
    page.btn_click_enter()
    browser.implicitly_wait(5)
    error_message = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    forgot_pass = browser.find_element(*AuthLocators.AUTH_FORGOT_PASSWORD)
    assert error_message.text == 'Неверный логин или пароль' and page.check_color(forgot_pass) == '#ff4f12'  # Проверяем появление сообщения об ошибке и измениние цвета надписи "Забыл пароль"


'''Тест авторизации с пустыми полями ввода'''
def test_auth_page_empty_phone_empty_pass_authorization(browser):
    page = AuthPage(browser)
    page.enter_username('')
    page.enter_password('')
    page.btn_click_enter()
    error_message = browser.find_element(*AuthLocators.AUTH_MESS_EMPTY_PHONE)
    assert error_message.text == 'Введите номер телефона'  # Сообщение при пустом поле "Телефон" (при пустом пароле сообщения нет)


'''Тест кнопки перехода на страницу регистрации'''
def test_reg_page_button(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration' #переход на страницу регистрации


'''Тест кнопки авторизации через ВК'''
def test_VK_button(browser):
    page = AuthPage(browser)
    page.enter_VK()
    assert page.get_relative_link() == '/authorize' #переход на страницу авторизации через соцесть
    page.driver.save_screenshot('test_VK_button.png')


'''Тест кнопки авторизации через Одноклассники'''
def test_OD_button(browser):
    page = AuthPage(browser)
    page.enter_OD()
    assert page.get_relative_link() == '/dk' #переход на страницу авторизации через соцесть
    page.driver.save_screenshot('test_OD_button.png')


'''Тест кнопки авторизации через Мэйл.ру'''
def test_MAIL_button(browser):
    page = AuthPage(browser)
    page.enter_MAIL()
    assert page.get_relative_link() == '/oauth/authorize' #переход на страницу авторизации через сервис
    page.driver.save_screenshot('test_MAIL_button.png')


'''Тест кнопки авторизации через гугл аккаунт'''
def test_GOOGLE_button(browser):
    page = AuthPage(browser)
    page.enter_GOOGLE()
    assert page.get_relative_link() == '/o/oauth2/auth/identifier' #переход на страницу авторизации через гугл аккаунт
    page.driver.save_screenshot('test_GOOGLE_button.png')


'''Тест кнопки авторизации через яндекс аккаунт'''
def test_YANDEX_button(browser):
    page = AuthPage(browser)
    browser.implicitly_wait(10)
    page.enter_YANDEX()
    browser.implicitly_wait(10)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/authenticate' #переход на страницу авторизации через яндекс аккаунт
    page.driver.save_screenshot('test_YANDEX_button.png')


'''Тест кнопки "Забыл пароль"'''
def test_to_forgot_pass_page(browser):
    page = AuthPage(browser)
    page.enter_forgot_pass()
    browser.implicitly_wait(3)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials' #переход на страницу восстановления пароля
    page.driver.save_screenshot('test_forgot_pass.png')


'''Тест регистрации нового пользователя с невалидным имейлом(негативный сценарий)'''
@pytest.mark.parametrize('email', ['', invalid_email, no_eng_email],
                         ids=['EMPTY_EMAIL', 'INVALID_EMAIL', 'NO_ENG_EMAIL'])
def test_registration_invalid_email(browser, email):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_name(name)
    browser.implicitly_wait(5)
    page.enter_lastname(lastname)
    browser.implicitly_wait(5)
    page.enter_email(email)
    browser.implicitly_wait(5)
    page.enter_password(valid_password)
    browser.implicitly_wait(5)
    page.enter_pass_again(valid_password)
    browser.implicitly_wait(5)
    page.btn_click()

    error_message = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'#Сообщение об ошибке
    page.driver.save_screenshot('test_registration_invalid_email.png')


'''Тест регистрации нового пользователя с невалидным паролем(негативный сценарий)'''
@pytest.mark.parametrize('password', ['', password20, short_pass, long_pass, incorrect_pass1,
                                      incorrect_pass2, incorrect_pass3],
                         ids=['EMPTY_PASS',
                              'password20',
                              'SHORT_PASS',
                              'LONG_PASS',
                              'incorrect_pass1',
                              'incorrect_pass2',
                              'incorrect_pass3'])
def test_registration_invalid_pass(browser, password):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(5)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_name(name)
    browser.implicitly_wait(5)
    page.enter_lastname(lastname)
    browser.implicitly_wait(5)
    page.enter_email(valid_email)
    browser.implicitly_wait(5)
    page.enter_password(password)
    browser.implicitly_wait(5)
    page.enter_pass_again(password)
    browser.implicitly_wait(5)
    page.btn_click()

    error_message = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_message.text == 'Длина пароля должна быть не менее 8 символов' or 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or 'Длина' \
    ' пароля должна быть не более 20 символов' or 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' or 'Пароль' \
    ' должен содержать хотя бы одну заглавную букву' or 'Пароль должен содержать хотя бы одну заглавную букву' #Тест считается пройденным в случае получения одной из ошибок
    page.driver.save_screenshot('test_registration_invalid_pass.png')


'''Тест регистрации нового пользователя с невалидным именем(негативный сценарий)'''
@pytest.mark.parametrize('name', ['', short_name, long_name, no_rus_name, invalid_name, name31],
                         ids=['EMPTY_NAME', 'SHORT_NAME', 'LONG_NAME', 'NO_RUS_NAME', 'INVALID_NAME', 'NAME31'])
def test_registration_invalid_name(browser, name):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_name(name)
    browser.implicitly_wait(2)
    page.enter_lastname(lastname)
    browser.implicitly_wait(2)
    page.enter_email(valid_email)
    browser.implicitly_wait(2)
    page.enter_password(valid_password)
    browser.implicitly_wait(2)
    page.enter_pass_again(valid_password)
    browser.implicitly_wait(2)
    page.btn_click()

    error_message = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' #Тест считается пройденным в случае получения ошибки
    page.driver.save_screenshot('test_registration_invalid_name.png')


#ТЕСТ регистрация с невалидной фамилией
@pytest.mark.parametrize('secondname', ['', short_name, long_name, no_rus_name, invalid_name, name31],
                         ids=['EMPTY_SECONDNAME', 'SHORT_SECONDNAME', 'LONG_SECONDNAME', 'NO_RUS_SECONDNAME', 'INVALID_SECONDNAME', 'SECONDNAMENAME31'])
def test_registration_invalid_secondname(browser, secondname):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(1)

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_name(name)
    browser.implicitly_wait(1)
    page.enter_lastname(secondname)
    browser.implicitly_wait(1)
    page.enter_email(valid_email)
    browser.implicitly_wait(1)
    page.enter_password(valid_password)
    browser.implicitly_wait(1)
    page.enter_pass_again(valid_password)
    browser.implicitly_wait(1)
    page.btn_click()

    error_message = browser.find_element(*AuthLocators.AUTH_MESS_ERROR)
    assert error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' ##Тест считается пройденным в случае получения ошибки


'''Тест кнопки "Пользвательское соглашение"'''
def test_to_polz_sogl_page(browser):
    page = AuthPage(browser)
    page.enter_polz_sogl()
    assert page.get_relative_link() == '/auth/realms/b2c/protocol/openid-connect/auth' #переход на страницу пользовательского соглашения
    browser.implicitly_wait(3)


''' Тест кнопки "Политика конфиденциальности"'''
def test_to_politics_page(browser):
    page = AuthPage(browser)
    page.enter_politics()
    page.driver.save_screenshot('test_pol_conf.png')
    browser.implicitly_wait(3)
    assert page.get_relative_link() == '/auth/realms/b2c/protocol/openid-connect/auth' #переход на страницу пользовательского соглашения
