from selenium import webdriver
import time
from bs4 import BeautifulSoup

id = 'ryo1209hei@gmail.com'
psw = 'Nissy241209'

url = 'https://moneyforward.com'
url_signup = '/sign_up'
url_login = 'https://id.moneyforward.com/sign_in/new?client_id=2WND7CAYV1NsJDBzk13JRtjuk5g9Jtz-4gkAoVzuS_k&nonce=d0d4779253451b6b73f10ff0cd263415&redirect_uri=https%3A%2F%2Fmoneyforward.com%2Fauth%2Fmfid%2Fcallback&response_type=code&scope=openid+email+profile+address&state=c564d3048fd1e07da03dc541a593b080'
url_adress_login = 'https://id.moneyforward.com/sign_in/email?client_id=2WND7CAYV1NsJDBzk13JRtjuk5g9Jtz-4gkAoVzuS_k&nonce=d0d4779253451b6b73f10ff0cd263415&redirect_uri=https%3A%2F%2Fmoneyforward.com%2Fauth%2Fmfid%2Fcallback&response_type=code&scope=openid+email+profile+address&state=c564d3048fd1e07da03dc541a593b080'

driver = webdriver.Chrome('C:/Users/ryohei/Desktop/python/money_forward/chromedriver')
# driver.get(url+url_signup)
# time.sleep(1)

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# login = soup.find('a', class_ = '_y_7FIGn')
# url_login = login.attrs['href']
# print(url_login)
# driver.get(url+url_login)
# time.sleep(1)

driver.get(url_adress_login)
time.sleep(1)

email = driver.find_element_by_name('mfid_user[email]')
email.send_keys(id)
time.sleep(1)
email_button = driver.find_element_by_class_name('submitBtn')
email_button.click()
time.sleep(1)
passward = driver.find_element_by_name('mfid_user[password]')
passward.send_keys(psw)
time.sleep(1)
# passward_button = driver.find_element_by_class_name('submitBtn')
# passward_button.click()



