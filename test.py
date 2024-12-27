import requests
import re

html = requests.get("https://www.kanunu8.com/book6/guichuideng01/").content.decode("GBK")
chapter_link = []
book_url = 'https://www.kanunu8.com/book6/guichuideng01/'
toc_block = re.findall('<h2>正文</h2>(.*?)</ul>', html, re.S)[0]
chapter_link_list = re.findall('href="(.*?)"', toc_block, re.S)
for l in chapter_link_list:
    chapter_link.append(book_url + l)
print(chapter_link)