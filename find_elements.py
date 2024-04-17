from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path: str = 'chromedriver-win64/chromedriver.exe'

# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Создание экземпляра браузера
browser = webdriver.Chrome(service=chrome_service)

URL: str = 'https://qa-test-selectors.netlify.app/'

try:
    # Открытие веб-ресурса
    browser.get(URL)

    # Неявное ожидание для загрузки элементов страницы
    browser.implicitly_wait(10)

    # Найдем кнопку со значением 15
    buttons = browser.find_elements(By.CSS_SELECTOR, ".variant__btn")

    # Нажать на кнопку
    buttons[14].click()

    # Элементы с тегом h1 (заголовки)
    elements_by_tag = browser.find_elements(By.TAG_NAME, 'h1')
    print(f'Количество элементов с тегом h1: {len(elements_by_tag)}')

    # Элемент с именем almond-nut (1 карточка)
    elements_by_name_1 = browser.find_elements(By.NAME, 'almond-nut')
    print(f'Количество элементов с именем almond-nut: {len(elements_by_name_1)}')

    # Элемент с ID cashew (2 карточка)
    elements_by_id_2 = browser.find_elements(By.ID, "cashew")
    print(f'Количество элементов с ID cashew: {len(elements_by_id_2)}')

    # Элементы с классом hazelnutNut (3 карточка)
    elements_by_class_3 = browser.find_elements(By.CLASS_NAME, 'hazelnutNut')
    print(f'Количество элементов с классом hazelnutNut: {len(elements_by_class_3)}')

    # Элемент с именем peanut-nut (4 карточка)
    elements_by_name_4 = browser.find_elements(By.NAME, 'peanut-nut')
    print(f'Количество элементов с именем peanut-nut: {len(elements_by_name_4)}')

    # Элемент с именем phistachios-nut (4 карточка)
    elements_by_name_5 = browser.find_elements(By.NAME, 'phistachios-nut')
    print(f'Количество элементов с именем phistachios-nut: {len(elements_by_name_5)}')

    # Элемент с ID walnut
    elements_by_id_6 = browser.find_elements(By.ID, "walnut")
    print(f'Количество элементов с ID walnut: {len(elements_by_id_6)}')

except Exception as e:
    print(f'Произошла ошибка: {e}')

finally:
    # Закрытие окна браузера
    browser.quit()

