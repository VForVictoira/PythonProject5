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
soup2 = BeautifulSoup(html, 'lxml')
info1 = soup.find(href = '/files/youth/')
#print(info1)
#print(info1.string)

info2 = soup.find(class_ = 'ind')
#print((info2.string))

# 先抓大再抓小
info3 = soup.find(class_ = 'mulu-list')
# soup.find() 方法只会返回匹配的第一个元素。
# find()返回的是一个BeautifulSoup Tag对象
# 它不会继续查找或返回其他同类元素
# 如果有多个同类的元素，find() 会忽略后面的元素，只获取第一个
#all_content = info3.find_all('li')
# find_all()返回的是BeautifulSoup Tag对象组成的列表
# 如果没有找到任何满足要求的标签，就会返回空列表
#for li in all_content:
#    print(li.string)

info4 = soup.find(class_='mulu-list')
# text 可以是一个字符串或正则，用于检索标签里的文本信息
#ll_content = info4.find_all(text=re.compile('章'))
#for li in all_content:
#    print(li)

info5 = soup.find(class_='nav-top')
all_content = info5.find_all(href=re.compile('youth'))
print(all_content)
for content in all_content:
    print(content.string)