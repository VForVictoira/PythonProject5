import requests
from bs4 import BeautifulSoup
import os
from concurrent.futures import ThreadPoolExecutor


def get_each_page_seq(url):
    start_url = 'https://meirentu.cc'
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    href_link = [tag['href'] for tag in soup.find_all('a') if '/model/' in tag['href']]
    each_page_seq = [start_url + link for link in href_link]
    return each_page_seq


def get_each_page(url):
    start_url = 'https://meirentu.cc'
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    href_link= [tag['href'] for tag in soup.find_all('a', href=True) if '/pic/' in tag['href']]
    each_page = [start_url + link for link in href_link]
    return each_page

def get_each_pic_page(url):
    start_url = 'https://meirentu.cc'
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    href_link= [tag['href'] for tag in soup.find_all('a', href=True) if '/pic/' in tag['href']]
    each_pic_page = [start_url + link for link in href_link]
    return each_pic_page

def get_each_pic_link(url):
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    pic_link = [tag['src'] for tag in soup.find_all('img') if tag.get('src') and  'https://cdn8.mmdb.cc/file' in tag['src'] ]
    return pic_link



if __name__ == '__main__':
    url = 'https://meirentu.cc/model/%E5%AE%89%E7%84%B6.html'
    os.environ.pop("HTTP_PROXY", None)
    os.environ.pop("HTTPS_PROXY", None)
    each_page_seq = get_each_page_seq(url)
    each_model_page = []
    for url in each_page_seq:
        each_page = get_each_page(url)
        each_model_page.extend(each_page)
    each_pic_seq_link = []
    for url in each_model_page:
        each_pic_seq = get_each_pic_page(url)
        each_pic_seq_link.extend(each_pic_seq)
    pic_link = []
    for url2 in each_pic_seq_link:
        pic = get_each_pic_link(url2)
        pic_link.extend(pic)

    main_folder = './meirentu_cc'
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)
    file_path = os.path.join(main_folder, 'link4.txt')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(pic_link))







