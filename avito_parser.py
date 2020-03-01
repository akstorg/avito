import requests
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/newauto/marka-chevrolet/'
HEADERS = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) /Chrome/79.0.3945.130 Safari/537.36", 'accept': '*/*'}
HOST = 'https://auto.ria.com'
def get_html (url, params=None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_content (html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition_area')
    # print(items)

    cars = []
    for item in items:

            usd_price = item.find('span', class_='green bold size18')
            if usd_price:
                usd_price = item.find('span', class_='green bold size18').get_text()
            else:
                usd_price = 'Цену уточняйте'

            ua_price = item.find('span', class_='grey size13')
            if ua_price:
                ua_price = item.find('span', class_='grey size13').get_text()
            else:
                ua_price = 'Цену уточняйте'

            cars.append({
                'title': item.find('h3', class_='proposition_name').get_text(strip=True),
                'link': HOST + item.find('a').get('href'),
                'usd_price': usd_price,
                'ua_price': ua_price,
                'city': item.find ('div', class_='proposition_region grey size13').get_text(),
            })
    print(cars)
    print(len(cars))



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()