В файле results находятся allure отчёты, в requirements.txt находятся зависимости, используемые для работы, в pages методы, которые используются в тестировании(pages/tests). 
Структура proFinancy:
  Locators - класс с селекторами
  класс ProFinancy, где содержатся методы для тестирования. Для инициализации браузера используется пакет base_page, для которого настроена фикстура, возвращающая браузер с установленными параметрами(файл conftest.py)