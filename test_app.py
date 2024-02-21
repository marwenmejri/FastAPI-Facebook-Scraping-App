from fastapi.testclient import TestClient
from scraping_app.main import app
from bs4 import BeautifulSoup


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, 'lxml')
    home_page_title = soup.title.text
    assert home_page_title == 'Scraping Service'
