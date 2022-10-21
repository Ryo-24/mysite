from fileinput import filename
from importlib.resources import path
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
# import csv
import datetime

url_amazon = 'https://www.amazon.co.jp'

res = requests.get(url_amazon)
print(res)
soup = BeautifulSoup(res.text, 'html.parser')
url_order = soup.find('a', id = 'nav-orders').attrs['href']

driver = webdriver.Chrome('chromedriver')
driver.get(url_amazon + url_order)
time.sleep(1)

id = 'ryo1209hei@gmail.com'
psw = 'Nissy241209'

input_id = driver.find_element_by_id('ap_email')
input_id.send_keys(id)
time.sleep(1)
button_id = driver.find_element_by_xpath("//input[@aria-labelledby='continue-announce']")
button_id.click()
time.sleep(1)
input_psw = driver.find_element_by_id('ap_password')
input_psw.send_keys(psw)
time.sleep(1)
button_psw = driver.find_element_by_id('signInSubmit')
button_psw.click()
time.sleep(1)

ordered_soup = BeautifulSoup(driver.page_source, 'html.parser')

ordered_items = []
for ordered_elem in ordered_soup.find_all('div', class_ = 'a-box-group a-spacing-base order js-order-card'):
    ordered_item = {}
    order_day = ordered_elem.select(
        'div.a-box.a-color-offset-background.order-info > div > div > div > div.a-fixed-right-grid-col.a-col-left > div > div.a-column.a-span3 > div.a-row.a-size-base > span'
        )
    ordered_item['order_day'] = order_day[0].text.replace(' ', '').replace('\n', '')
    price = ordered_elem.select(
        'div.a-box.a-color-offset-background.order-info > div > div > div > div.a-fixed-right-grid-col.a-col-left > div > div.a-column.a-span2 > div.a-row.a-size-base > span'
    )
    ordered_item['price'] = price[0].text.replace('￥', '').replace(' ', '').replace('\n', '')
    name_url = ordered_elem.select(
        'div.a-box.shipment.shipment-is-delivered > div > div.a-fixed-right-grid.a-spacing-top-medium > div > div.a-fixed-right-grid-col.a-col-left > div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(1) > a'
    )
    ordered_item['name'] = name_url[0].text.replace(' ', '').replace('\n', '')
    ordered_item['url'] = url_amazon + name_url[0].attrs['href']
    ordered_items.append(ordered_item)

df_order = pd.DataFrame(
    ordered_items,
    columns=ordered_items[0].keys()
    )

df_order = df_order.set_index('order_day')

filename = f"ordered_history_{datetime.datetime.today().strftime('%Y%m%d')}.csv"
path = "C:/Users/ryohei/Desktop/python/amazon_ranking/"
open_path = path + filename

df_order.to_csv(open_path,encoding='utf_8_sig')

# with open(open_path,'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(df_order)




