import requests
import re
import os
from concurrent.futures import ThreadPoolExecutor


def get_book_name(html):
    book_name = []
    site_url = 'https://www.kanunu8.com'
    toc_block = re.findall('天下霸唱作品集<(.*?)起源</a></', html, re.S)[0]
    book_name_list = re.findall('<h2><a href="(.*?)">鬼吹灯', toc_block, re.S)[0:9]
    for url in book_name_list:
        book_name.append(site_url + url)
    return book_name


def get_chapter_link(html, book_url):
    chapter_link = []
    toc_block = re.findall('<h2>正文</h2>(.*?)</ul>', html, re.S)[0]
    chapter_link_list = re.findall('href="(.*?)"', toc_block, re.S)
    for l in chapter_link_list:
        chapter_link.append(book_url + l)
    return chapter_link


def get_article(html_url):
    try:
        html = requests.get(html_url).content.decode('GBK')
        book_name = re.findall('<a href="./index.html" title="(.*?)"', html, re.S)[0]
        chapter_pattern = rf'<h1>{re.escape(book_name)} 正文 (.*?)</h1>'
        chapter_name = re.findall(chapter_pattern, html, re.S)[0]
        text_block = re.findall('<p>(.*?)</p>', html, re.S)[0]
        text_block = text_block.replace('<br />', '').replace('&nbsp;', '')
        return book_name, chapter_name, text_block
    except Exception as e:
        print(f"Error fetching article from {html_url}: {e}")
        return None, None, None


def save(sub_folder, chapter, article):
    if not chapter or not article:
        return
    main_folder = '鬼吹灯'
    os.makedirs(main_folder, exist_ok=True)
    folder_path = os.path.join(main_folder, sub_folder)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{chapter}.txt")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(article)


def fetch_and_save_chapter(html_url):
    sub_folder, chapter_name, text_block = get_article(html_url)
    if chapter_name and text_block:
        save(sub_folder, chapter_name, text_block)
        print(f"成功保存章节: {chapter_name}")


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

    # 使用多线程抓取和保存
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(fetch_and_save_chapter, chapter_list)
