import re
import requests
import os
from concurrent.futures import ThreadPoolExecutor

from urllib3.filepost import writer


def get_book_name(html):
    book_name = []
    site_url = 'https://www.kanunu8.com'
    toc_block = re.findall('天下霸唱作品集<(.*?)起源</a></', html, re.S)[0]
    book_name_list = re.findall('<h2><a href="(.*?)">鬼吹灯', toc_block, re.S)[0:9]
    for url in book_name_list:
        book_name.append(site_url + url)
    return book_name

def get_chapter_link(html,book_url):
    chapter_link= []
    toc_block = re.findall('<h2>正文</h2>(.*?)</ul>', html, re.S)[0]
    chapter_link_list = re.findall('href="(.*?)"', toc_block, re.S)
    for l in chapter_link_list:
        chapter_link.append(book_url + l)
    return chapter_link


if __name__ == '__main__':
    start_url = 'https://www.kanunu8.com/zt/zt_11227.html'
    html = requests.get(start_url).content.decode('GBK')

    # 获取所有书籍的链接
    book_name = get_book_name(html)
    chapter_list = []

    # 获取所有章节的链接
    for book in book_name:
        html = requests.get(book).content.decode('GBK')
        chapter = get_chapter_link(html, book)
        chapter_list.extend(chapter)
        #chapter_list.extend
        test = 'C:\\Users\\SawyerWang\\Desktop\\test'
        os.makedirs(test, exist_ok=True)
        file_path = os.path.join(test,  'chapter_list2.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(chapter_list))
