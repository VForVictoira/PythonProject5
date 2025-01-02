import requests
import re
import os

ht='https://www.kanunu8.com/book6/guichuideng07/53062.html'
html = requests.get(ht).content.decode('GBK')
book_name = re.findall('<a href="./index.html" title="(.*?)"', html, re.S)[0]
chapter_pattern = rf'<h1>{re.escape(book_name)} 正文 (.*?)</h1>'
chapter_name = re.findall(chapter_pattern, html, re.S)[0]
text_block = re.findall('&nbsp;(.*?)</p>', html, re.S)[0]
text_block = text_block.replace('<br />', '')
text_block = text_block.replace('&nbsp;', '')
text_block = f'{chapter_name.center(100, ' ')}\n\n'.join(['\n', text_block])

print(text_block)