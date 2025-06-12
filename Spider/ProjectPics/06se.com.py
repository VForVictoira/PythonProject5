import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.06se.com/97058.html'
response = requests.get(url).content.decode('utf-8')

soup = BeautifulSoup(response, 'html.parser')
#all_img_content = soup.find_all('img')
#data_src = [img['data-src'] for img in all_img_content if 'data-src' in img.attrs]
pic_links = [tag['data-src'].split('&url=')[-1] for tag in soup.find_all('img')
    if 'data-src' in tag.attrs and 'https://imgsa.baidu.com/forum/pic/item/' in tag['data-src']]



main_folder = './06s_com'
if not os.path.exists(main_folder):
    os.makedirs(main_folder)
file_path = os.path.join(main_folder, 'link2.txt')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(pic_links))
