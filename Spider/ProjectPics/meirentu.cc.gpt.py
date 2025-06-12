import requests
from bs4 import BeautifulSoup
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm  # 用于显示进度条
import urllib3
# 获取每个模特页面的链接
def get_each_page_seq(url):
    start_url = 'https://meirentu.cc'
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    # 筛选出模特页面的链接
    href_link = [tag['href'] for tag in soup.find_all('a') if '/model/' in tag['href']]
    each_page_seq = [start_url + link for link in href_link]
    return each_page_seq

# 获取每个模特页面中的图片集页面链接
def get_each_page(url):
    start_url = 'https://meirentu.cc'
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    # 筛选出图片集页面的链接
    href_link = [tag['href'] for tag in soup.find_all('a', href=True) if '/pic/' in tag['href']]
    each_page = [start_url + link for link in href_link]
    return each_page

# 获取每个图片集页面中的单个图片页面链接
def get_each_pic_page(url):
    start_url = 'https://meirentu.cc'
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    # 筛选出具体图片页面的链接
    href_link = [tag['href'] for tag in soup.find_all('a', href=True) if '/pic/' in tag['href']]
    each_pic_page = [start_url + link for link in href_link]
    return each_pic_page

# 获取单个图片页面中的图片链接
def get_each_pic_link(url):
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    # 筛选出图片链接
    pic_link = [tag['src'] for tag in soup.find_all('img') if tag.get('src') and 'https://cdn8.mmdb.cc/file' in tag['src']]
    return pic_link

def get_each_pic_title(url):
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    pic_link_title = [h1.get_text() for h1 in soup.find_all('h1') ]
    return pic_link_title

# 多线程处理的辅助函数，带有进度条显示
def fetch_links(function, urls, description="Processing"):
    results = []
    with ThreadPoolExecutor() as executor:
        # 提交多个任务
        futures = {executor.submit(function, url): url for url in urls}
        for future in tqdm(as_completed(futures), total=len(futures), desc=description):
            try:
                results.extend(future.result())
            except Exception as e:
                print(f"错误: {e}")
    return results

if __name__ == '__main__':
    # 起始页面URL
    url = 'https://meirentu.cc/model/%E6%9D%8F%E5%AD%90.html'
    # 删除代理配置（如有）
    os.environ.pop("HTTP_PROXY", None)
    os.environ.pop("HTTPS_PROXY", None)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # 获取模特页面链接
    print("获取模特页面链接...")
    each_page_seq = get_each_page_seq(url)

    # 获取每个模特页面中的图片集页面链接（多线程加速 + 进度提示）
    print("获取图片集页面链接...")
    each_model_page = fetch_links(get_each_page, each_page_seq, description="图片集页面")

    # 获取每个图片集页面中的图片页面链接（多线程加速 + 进度提示）
    print("获取图片页面链接...")
    each_pic_seq_link = fetch_links(get_each_pic_page, each_model_page, description="图片页面")

    # 获取所有图片链接（多线程加速 + 进度提示）
    print("获取图片链接...")
    pic_link = fetch_links(get_each_pic_link, each_pic_seq_link, description="图片链接")

    # 保存结果到本地
    print("保存结果到文件...")
    main_folder = './meirentu_cc'
    if not os.path.exists(main_folder):
        os.makedirs(main_folder)
    file_path = os.path.join(main_folder, 'link5.txt')

    with open(file_path, 'w', encoding='utf-8') as f:

        f.write('\n'.join(pic_link)+'\n')

    print(f"完成！共保存 {len(pic_link)} 个图片链接。")
