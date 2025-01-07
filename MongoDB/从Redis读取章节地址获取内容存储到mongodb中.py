import requests
from bs4 import BeautifulSoup
import redis
from pymongo import MongoClient
from charset_normalizer.md import CjkInvalidStopPlugin

# 从 Redis 中读取章节地址
client = redis.StrictRedis(host='192.168.0.109', port=6379, db=0)

Chapter_URL = []
while True:
    URL = client.spop('Chapter_URL')
    if URL is None:
        break
    Chapter_URL.append(URL)
# 抓取章节
def get_article(url):
    html = requests.get(url).content.decode('GBK')
    soup = BeautifulSoup(html, 'html.parser')
    chapter_name = soup.find('font', attrs={'color': '#dc143c'}).text
    text= soup.find('p').text.replace('\r', '').replace('\n', '')
    return chapter_name, text

if __name__ == '__main__':
    client2 = MongoClient('localhost', 27017)
    database = client2.Project1
    collection = database.Animal_Farm

    for url in Chapter_URL:
        result = get_article(url)
        data = {'Chapter':result[0],'Text':result[1]}
        collection.insert_one(data)


