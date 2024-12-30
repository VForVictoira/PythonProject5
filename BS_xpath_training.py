import requests
import os
import lxml.html
import csv
from concurrent.futures import ThreadPoolExecutor

def get_sub_url(sul):
    sub_link=[]
    origin_url = 'https://xunlei8.cc'
    sub_link_list = sul.xpath('.//div//a//@href')
    for url in sub_link_list:
        sub_link.append(origin_url+url)
    return sub_link




url = 'https://xunlei8.cc/list-0-2024-0-rating-1-30.html'
html = requests.get(url).content.decode('utf-8')

selector = lxml.html.fromstring(html)

item_list = selector.xpath('//div[@class="bd6d40 b351186d6b114"]')
name_list = item_list[0].xpath('//div//span[@class="b355d4cd397"]/text()')
time_list = item_list[0].xpath('//div//span[@class="span-year span-year-2020"]/text()')
classify_list = item_list[0].xpath('//div//span[@class="span-high"]/text()')
description_list_all = item_list[0].xpath('//div//span/text()')
sub_link = get_sub_url(item_list[0])
'''
url2='https://xunlei8.cc/movie/05987884.html'
html2 = requests.get(url2).content.decode('utf-8')
selector1 = lxml.html.fromstring(html2)

#all_content = selector1.xpath('//div[@class="b59a2b64df1 bb4fa"]')
download_link=selector1.xpath('//div//a[@class="baf6e960dd"]//@href')
print(download_link)
'''
with ThreadPoolExecutor(max_workers=10) as executor:
    download_link_list = []
    for i in sub_link:
        html2 = requests.get(i).content.decode('utf-8')
        selector1 = lxml.html.fromstring(html2)
        download_link = selector1.xpath('(//div//a[@class="baf6e960dd"])[1]/@href')
        download_link_list.extend(download_link)



filter = [text for text in description_list_all if ' ' in text][3::]
description_list = [t for t in filter if t.strip() != '/']
item_dict_list=[]
for i in range (len(description_list)):
    item_dict = {'电影名称': name_list[i],
                 '上映时间': time_list[i],
                 '评分': classify_list[i],
                 '描述': description_list[i],
                 '下载链接':download_link_list[i],
    }
    item_dict_list.append(item_dict)

main_folder = './Moives'
os.makedirs(main_folder, exist_ok=True)
file_path = os.path.join(main_folder, 'BS_xpath_training.csv')
with open(file_path, 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['电影名称','上映时间','评分','描述','下载链接'])
    writer.writeheader()
    writer.writerows(item_dict_list)
print(f'数据已经保存到{file_path}')

