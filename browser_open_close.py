import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path: str = 'chromedriver-win64/chromedriver.exe'

# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)

# Создание экземпляра браузера
driver = webdriver.Chrome(service=chrome_service)

try:
    # Открытие веб-страницы
    driver.get('https://habr.com/ru/articles/')

    # Ждём некоторое время
    time.sleep(5)

except Exception as e:
    print(f'Произошла ошибка: {e}')

finally:
    # Закроем браузер
    driver.quit()
