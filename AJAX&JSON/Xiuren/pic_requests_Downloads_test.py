from tkinter.font import names

import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pickle
from selenium.webdriver.chrome.service import Service
import os
import re

from selenium.webdriver.support.wait import WebDriverWait

#chrome_driver_path = r'E:\PythonProjects\PythonProject5\AJAX&JSON\chromedriver-win64\chromedriver.exe'
#chrome_options = Options()
#chrome_options.add_argument("--headless")

#service = Service(chrome_driver_path)

#driver = webdriver.Chrome(service=service, options=chrome_options)
# 打开网页
url = input("Enter URL: ")
#driver.get('https://www.xsnvshen.co/girl/28144')
#driver.get(url)
#time.sleep(3)

#cookies = driver.get_cookies()
#with open('cookies.pkl', 'wb') as f:
#    pickle.dump(cookies, f)

#with open('cookies.pkl', 'rb') as file:
#    cookies = pickle.load(file)

#for cookie in cookies:
#    driver.add_cookie(cookie)
# 获取页面源代码

#driver.refresh()

#element = driver.find_element('tag name', 'img')
#pic_src = element.get_attribute('src')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": f"{url}",  # 根据情况设置来源
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}
pic_response = requests.get(url,headers=headers)

if pic_response.status_code == 200:
    with open('1.jpg', 'wb') as f:
        f.write(pic_response.content)
    print('图片成功下载到本地')
else:
    print(f'图片下载失败：{pic_response.status_code}')