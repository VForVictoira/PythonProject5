from bs4 import BeautifulSoup
import re
import requests
import os

url = 'https://www.kanunu8.com/book5/daomubiji/'
html = requests.get(url).content.decode('GBK')
#main = './BS4_Test'
#os.makedirs(main, exist_ok=True)
#file_path = main + '/index.txt'
#with open(file_path, 'w') as f:
#    f.write(html)

# 解析源代码生成 BS 对象
soup = BeautifulSoup(html, 'html.parser')
# 安装了 lxml 也可以使用 lxml
#soup2 = BeautifulSoup(html, 'lxml')
info1 = soup.find(href = '/files/youth/')
#print(info1)
#print(info1.string)

info2 = soup.find(class_ = 'ind')
print((info2.string))