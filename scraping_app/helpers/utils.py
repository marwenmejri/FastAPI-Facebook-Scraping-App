import time
from datetime import datetime, timedelta
from dateutil import parser

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def scroll_down(driver, pause_time):
    time.sleep(2)
    if driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div["
                                     "1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]"):
        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div["
                            "1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").click()
        time.sleep(2)
    body = driver.find_element(By.TAG_NAME, "body")
    for i in range(8):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(pause_time)


def transform_date_from_now(text):
    number, unit = int(text[:-1]), text[-1]
    now = datetime.now()
    if unit == 'h':
        new_date = now + timedelta(hours=number)
    elif unit in ['d', 'j']:
        new_date = now - timedelta(days=number)
    elif unit == 'm':
        new_date = now - timedelta(days=number * 30)
    elif unit in ['y', 'a']:
        new_date = now - timedelta(days=number * 365)
    else:
        try:
            return parser.parse(text)
        except ValueError as e:
            print(f"Date parsing error: {e}")
            new_date = now
    return new_date.strftime("%d-%m-%Y")
