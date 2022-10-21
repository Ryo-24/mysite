import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data_udemy():
    url_scraping = 'https://scraping-for-beginner.herokuapp.com/udemy'

    res_scraping = requests.get(url_scraping)
    soup_scraping = BeautifulSoup(res_scraping.text, 'html.parser')

    subscribers = soup_scraping.find('p', class_ = 'subscribers').text.split('：')[1]
    reviews = soup_scraping.find('p', class_ = 'reviews').text.split('：')[1]

    return {
        'subscribers': subscribers,
        'reviews': reviews
    }


def get_data_EC():
    url_EC = 'https://scraping.official.ec/'

    res_EC = requests.get(url_EC)
    soup_EC = BeautifulSoup(res_EC.text, 'html.parser')

    all_product = []
    for elem in soup_EC.find_all('li', class_ = 'items-grid_itemListLI_5a0255a1'):
        product_inf = {}
        product_inf['name'] = elem.find('p', class_ = 'items-grid_itemTitleText_5a0255a1').text
        product_inf['price'] = elem.find('p', class_ = 'items-grid_price_5a0255a1').text.replace('¥', '').replace(',', '')
        product_inf['url'] = elem.find('a', class_ = 'items-grid_anchor_5a0255a1 js-anchor').attrs['href']
        all_product.append(product_inf)

    df_EC = pd.DataFrame(all_product)

    return df_EC