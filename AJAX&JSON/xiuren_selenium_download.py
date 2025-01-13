
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pickle
from selenium.webdriver.chrome.service import Service
import os
import re


chrome_driver_path = r'E:\PythonProjects\PythonProject5\AJAX&JSON\chromedriver-win64\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
# 打开网页
url = input("Enter URL: ")
#driver.get('https://www.xsnvshen.co/girl/28144')
driver.get(url)
time.sleep(2)

#cookies = driver.get_cookies()
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)

for cookie in cookies:
    driver.add_cookie(cookie)
# 获取页面源代码

driver.refresh()

# 获取图片下载链接
element1 = driver.find_elements(By.XPATH,'//img[@data-original]')
data_original_values1 = [element.get_attribute('data-original') for element in element1]
final_links = ['https://' + link.lstrip('//') for link in data_original_values1]

# 获取套图名称
element2 = driver.find_element(By.XPATH,"//h1//a[contains(text(), 'No.')]")
data_original_values2 = element2.text
title  = re.search(r"No\.\d+", data_original_values2).group(0)

# 获取模特名称
#value1  = re.search(r"\d+", url).group(0)
# 模特的 /girl/值是主页的值，每个图片页面是固定数值
xpath_expression = f'//a[@href="/girl/28202"]'
element3 = driver.find_element(By.XPATH,xpath_expression)
model_name= element3.text

main_folder = f'./Xiuren/{model_name}'
os.makedirs(main_folder, exist_ok=True)
file_path2 = os.path.join(main_folder, f'{title}.txt')
# pic_link =[t for t in pic_link link.lstrip('//')]
with open(file_path2, 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_links))

