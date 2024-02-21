from scraping_app.helpers.utils import scroll_down, transform_date_from_now

import json
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Scrap:
    def __init__(self, url):
        self.url = url

    def scrap_data(self):
        posts = []
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(self.url)
        print(driver.title)
        scroll_down(driver, 3)
        page_source = driver.page_source
        driver.quit()
        soup = BeautifulSoup(page_source, 'lxml')
        sections = soup.find_all(class_='x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z')
        print(len(sections))
        for section in sections:
            try:
                post_text = section.find(class_='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a').text
                post_info = section.find(
                    class_='x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 '
                           'xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu '
                           'x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xt0b8zv '
                           'xo1l8bm')
                post_url = post_info['href'].split('?')[0]
                post_emojis = section.find(class_='xrbpyxo x6ikm8r x10wlt62 xlyipyv x1exxlbk').find(class_='x1e558r4').text
                try:
                    post_comments = section.find_all(class_='x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso '
                                                            'x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen '
                                                            'xo1l8bm xi81zsa')[1].text
                except Exception as e:
                    # print(e)
                    post_comments = '0'
                post_date = transform_date_from_now(post_info.span.text.strip())
                posts.append({
                    'page': self.url.split('/')[-1],
                    'url': post_url,
                    'text': post_text,
                    'date': datetime.strptime(post_date, "%d-%m-%Y"),
                    'nbr_emojis': post_emojis.replace('\u00a0', ' '),
                    'nbr_comments': post_comments.replace('\u00a0', ' ')
                })
            except Exception as e:
                print(e)
        return posts


if __name__ == '__main__':
    sp = Scrap(url='https://www.facebook.com/Cristiano')
    results = sp.scrap_data()
    with open('posts.json', 'w') as f:
        json.dump(results, f)
