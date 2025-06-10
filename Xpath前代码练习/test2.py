import requests
import re
import os


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
    book_name = get_book_name(html)
    url_list=[]
    for name in book_name:
        html = requests.get(name).content.decode('GBK')
        chapter_link = get_chapter_link(html,name)
        url_list.extend(chapter_link)  # 使用了 url_list = url_list.append(...)，这是一个问题，因为 list.append() 方法会修改列表本身并返回 None，因此不能将其赋值回列表
    print(url_list)
