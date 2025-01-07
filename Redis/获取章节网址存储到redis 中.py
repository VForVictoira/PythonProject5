import requests
import lxml.html
import redis


# 目标网页
url = 'https://www.kanunu8.com/book3/6879/'

# 使用 xpath 获取章节网址
html = requests.get(url).content.decode('GBK')
selector = lxml.html.fromstring(html)

content_url = selector.xpath('//td//a[starts-with(@href,"1317")]/@href')
url_head = 'https://www.kanunu8.com/book3/6879/'
chapter_url =[url_head+url for url in content_url]

# 将章节网页写入 Redis
client = redis.StrictRedis(host='192.168.0.109', port=6379, db=0)
for url in chapter_url:
    client.sadd('Chapter_URL', url)

