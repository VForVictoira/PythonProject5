import requests
import lxml.html
import os
import asyncio
from pyppeteer import launch
# 设置 Chrome 驱动程序路径
async def fetch_html(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url)
    content = await page.content()  # 获取渲染后的 HTML
    await browser.close()
    return content

url = 'https://www.xsnvshen.co/album/44090'
html = asyncio.run(fetch_html(url))



#pic_link = all.xpath('.//div[@class="swi-hd"]//img/@data-original')
'''
main_folder = './Xiuren'
os.makedirs(main_folder, exist_ok=True)
file_path = os.path.join(main_folder, 'index.html')
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()'''


selector = lxml.html.fromstring(html)

pic_link = selector.xpath('//img/@data-original')
final_links = ['https://' + link.lstrip('//') for link in pic_link]
file_path2 = os.path.join(main_folder, 'download3.txt')
# pic_link =[t for t in pic_link link.lstrip('//')]
with open(file_path2, 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_links))