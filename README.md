В проекте была произведена проверка требований, данных заказчиком, его исправление, составлены чек-лист и тест-кейсы для проверки соответсвия требованиям. При проверках использовались мануальные  и автоматизированные тесты, с помощью которых были найдены баги, составлены баг-реопрты. Автотесты написаны на языке программирования Python в среде Pycharm с использованием selenium  и pytest.

Чек-лист,тест-кейсы и баг-репорты находятся в в файле доступном по ссылке на гугл диске
https://drive.google.com/drive/folders/1rb3rZ-1RClw1fcNTFOgqTEF9ZbXg7Ix7?usp=sharing

Все тесты находятся в файле tests.

Для запуска всех тестов необходимо в консоль терминала ввести команду: python -m pytest -v --driver Chrome --driver-path chrDrive.exe tests/test.py

Тесты запускаются на компьютере с установленными Python3 и PyTest.

В процессе тестирования использовался браузер Google Chrome Версия 111.0.5563.65 (Официальная сборка), (64 бит), для применения автотестов необходимо иметь валидные имейл и пароль от лк Ростелекома и прописать путь к драйверу в файле conftest.py
