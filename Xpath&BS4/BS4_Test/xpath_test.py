import re
import selectors

import requests
import lxml.html
import os

html = requests.get('https://www.kanunu8.com/zt/zt_11227.html').content.decode('GBK')


selector = lxml.html.fromstring(html)
info = selector.xpath('//meta[@name="description"]//@content')[0]
#print(info)

#info2 = selector.xpath('//div[@class="nav-top"]//a[target="_parent"]//text()')
info2 = selector.xpath('//div[@class="nav-top"]//a[@target="_parent"]/text()')

#print(info2)
# 获取章节下载地址
info3 = selector.xpath('//div[@class="mulu-list"]//ul//li//a//@href')
info3 = '\n'.join(info3)


info4 = selector.xpath('//div[@class="mulu-list"]//ul//li//a//text()')

html2 = re.findall('精绝古城(.*?)</ul',html,re.S)[0]
selector2 = lxml.html.fromstring(html2)
info5 = selector2.xpath('//li//a//@href')
info6 = selector2.xpath('//li//a/text()')

file_path = os.path.join('../xpath_Test', 'info5.txt')
file_path2 = os.path.join('../xpath_Test', 'info6.txt')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str('\n'.join(info5)))
with open(file_path2, 'w', encoding='utf-8') as f:
    f.write(str('\n'.join(info6)))

# 属性值的开头部分相同
info7 = selector.xpath('//ul//li//a[starts-with(@href, "/book6/guichuideng01")]/text()')
#print(str('\n'.join(info7)))

# 属性值包含相同字符串
info8 = selector.xpath('//ul//li//a[contains(@href, "guichuideng02")]/text()')
#print(str('\n'.join(info8)))

# xpath 先抓大再抓小
html = requests.get('https://www.kanunu8.com/book6/guichuideng01/').content.decode('GBK')

info9_block = selector.xpath('//div[@class="top-right"]')
info10 = info9_block[0].xpath('//div[@class="nav-top"]//a/text()')
#print('\n'.join(info10))

# 不同标签下的文字
string1 = '''    <! DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <div id="test3">
          我左青龙，
          <span id="tiger">
              右白虎，
              <ul>上朱雀，
                  <li>下玄武。</li>
              </ul>
              老牛在当中，
          </span>
          龙头在胸口。
        </div>
    </body>
    </html>'''

selector3 = lxml.html.fromstring(string1)
info11 = selector3.xpath('//div[@id="test3"]')[0]
info12 = info11.xpath('string(.)')
print(info12)