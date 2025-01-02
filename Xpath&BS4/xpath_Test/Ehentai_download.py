import requests
import lxml.html
import os
import csv
from concurrent.futures import ThreadPoolExecutor




url = 'https://e-hentai.org/g/3175785/3ffc77a984/'
html = requests.get(url).content.decode('utf-8')
selector = lxml.html.fromstring(html)

all_content= selector.xpath('//div[@class="gt200"]')
download_urls = all_content[0].xpath('.//a/@href')

with ThreadPoolExecutor(max_workers=5) as executor:
    download_link_list = []
    for url in download_urls:
        html2 = requests.get(url).content.decode('utf-8')
        selector2 = lxml.html.fromstring(html)
        Pic_link = selector2.xpath('//dive[@id="i3"]//a//img/@src')
        download_link_list.append(Pic_link)

print(download_link_list)