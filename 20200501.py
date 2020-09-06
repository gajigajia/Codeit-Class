from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver')


customer_num ='0135162726'
date =['2019-12-31']

url = 'https://admin.enernoc.kr/payment/ajaxPaymentFinal/?meter_id='+customer_num+'&payment_month='+date
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
#body > div > div > div > div > div.contents > div.data_area.ep_data > div.tbl_payment > table > tbody > tr > td


title = driver.find_element_by_xpath("/html/head/title")


final_payment =soup.select_one('#body > div > div > div > div > div.contents > div.data_area.ep_data > div.tbl_payment > table > tbody > tr > td')


print(final_payment)