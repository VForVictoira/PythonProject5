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

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#pic_link = all.xpath('.//div[@class="swi-hd"]//img/@data-original')

main_folder = './Xiuren'
os.makedirs(main_folder, exist_ok=True)
file_path = os.path.join(main_folder, 'index.html')
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()


selector = lxml.html.fromstring(html)

pic_link = selector.xpath('//img/@data-original')
final_links = ['https://' + link.lstrip('//') for link in pic_link]
'''
for idx, img_url in enumerate(final_links, start=1):
    file_name = f"image_{idx}.jpg"
    file_path2 = os.path.join(main_folder, file_name)
    try:
        response = requests.get(img_url, stream=True)
        if response.status_code == 200:
            with open(file_path2, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"已下载: {file_name}")
        else:
            print(f"无法下载 {img_url}，HTTP 状态码: {response.status_code}")
    except Exception as e:
        print(f"下载 {img_url} 时出错: {e}")

'''
file_path2 = os.path.join(main_folder, 'download4.txt')
# pic_link =[t for t in pic_link link.lstrip('//')]
with open(file_path2, 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_links))

