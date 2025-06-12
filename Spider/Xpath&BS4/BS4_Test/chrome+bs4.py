import re

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# 配置 ChromeDriver 路径
service = Service("E:\\PythonProjects\\Tools\\chromedriver-win64\\chromedriver.exe")  # 替换为你的 chromedriver 路径
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 无头模式（隐藏浏览器窗口）

# 启动 WebDriver
driver = webdriver.Chrome(service=service, options=options)

# 打开目标网址
url = 'https://www.photos18.com/zh-hans/v/JjPpe'
driver.get(url)

# 等待 JavaScript 加载完成
time.sleep(5)  # 视页面复杂度调整时间，也可用显式等待

# 获取完整的 HTML 源代码
html_source = driver.page_source


# 关闭 WebDriver
driver.quit()

'''main_folder = './Xiuren'
os.makedirs(main_folder, exist_ok=True)
file_path = os.path.join(main_folder, 'index.html')
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html_source)'''

soup = BeautifulSoup(html_source, 'html.parser')
all_content = soup.find_all('img')
img_src = [img['src'] for img in all_content if 'src' in img.attrs and 'image/3037' in img['src']]
print('\n'.join(img_src))

