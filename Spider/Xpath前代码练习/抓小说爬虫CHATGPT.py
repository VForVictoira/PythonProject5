import requests
import re
import os


def get_toc(html, start_url):
    """
    获取每一章链接，储存到一个列表中并返回
    :param html: 目录页源代码
    :param start_url: 起始 URL，用于拼接完整链接
    :return: 每章链接列表
    """
    toc_url_list = []
    try:
        toc_block = re.search('正文.*?</tbody>', html, re.S)
        if not toc_block:
            raise ValueError("无法找到目录的内容块")
        toc_block = toc_block.group(0)
        toc_urls = re.findall('href="(.*?)"', toc_block, re.S)
        for url in toc_urls:
            toc_url_list.append(start_url + url)
    except Exception as e:
        print(f"获取目录时出现错误: {e}")
    return toc_url_list


def get_article(html):
    """
    获取每一章的正文并返回章节名和正文
    :param html: 正文源代码
    :return: 章节名，正文
    """
    try:
        chapter_name = re.search('size="4">(.*?)<', html, re.S)
        if not chapter_name:
            raise ValueError("无法找到章节名")
        chapter_name = chapter_name.group(1).strip()

        text_block = re.search('<p>(.*?)</p>', html, re.S)
        if not text_block:
            raise ValueError("无法找到正文内容")
        text_block = text_block.group(1)
        text_block = re.sub('<br\s*/?>', '\n', text_block).strip()  # 替换换行标签为换行符
    except Exception as e:
        print(f"获取章节时出现错误: {e}")
        chapter_name = "未知章节"
        text_block = "内容解析失败"
    return chapter_name, text_block


def save(chapter, article):
    """
    将每一章保存到本地。
    :param chapter: 章节名，第X章
    :param article: 正文内容
    :return: None
    """
    os.makedirs('动物农场', exist_ok=True)  # 如果没有“动物农场”文件夹，就创建一个
    safe_chapter_name = re.sub(r'[\\/:*?"<>|]', '_', chapter)  # 替换文件名中的非法字符
    file_path = os.path.join('动物农场', safe_chapter_name + '.txt')
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(article)
    except Exception as e:
        print(f"保存章节 {chapter} 时出现错误: {e}")


if __name__ == '__main__':
    start_url = "http://www.kanunu8.com/book3/6879/"  # 起始网址
    try:
        #response = requests.get(start_url)
        #response.encoding = 'GBK'  # 设置正确的编码
        html = requests.get(start_url).content.decode('GBK')
        toc_url_list = get_toc(html, start_url)
        for toc_url in toc_url_list:
            try:
                chapter_html = requests.get(toc_url).content.decode('GBK')
                chapter_name, text_block = get_article(chapter_html)
                save(chapter_name, text_block)
                print(f"成功保存章节: {chapter_name}")
            except Exception as e:
                print(f"处理章节 {toc_url} 时出现错误: {e}")
    except Exception as e:
        print(f"获取目录页时出现错误: {e}")
