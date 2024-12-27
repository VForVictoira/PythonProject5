import requests
import re
import os


def get_toc(html):
    toc_url_list = []
    toc_block = re.findall('正文(.*?)</tbody>', html, re.S)[0]
    toc_url = re.findall('href="(.*?)"', toc_block, re.S)
    for url in toc_url:
        toc_url_list.append(start_url + url)
    return toc_url_list

def get_article(html):
    html = requests.get(html).content.decode('GBK')
    chapter_name = re.search('size="4">(.*?)<', html, re.S).group(1)
    text_block = re.search('<p>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace('<br />', '')
    return chapter_name, text_block


def save(chapter, article):
    os.makedirs('动物农场', exist_ok = True)
    # 如果没有“动物农场”文件夹，就创建一个，如果有，则什么都不做
    with open(os.path.join('动物农场', chapter+'.txt'), 'w', encoding='utf-8') as f:
        f.write(article)

if __name__ == '__main__':
    start_url = 'http://www.kanunu8.com/book3/6879/'
    html = requests.get(start_url).content.decode('GBK')
    toc_list = get_toc(html)
    for toc_url in toc_list:
        chapter_name, text_block = get_article(toc_url)
        save(chapter_name, text_block)
        print(f"成功保存章节: {chapter_name}")