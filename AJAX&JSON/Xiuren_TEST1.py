import requests


url = 'https://www.xsnvshen.co/girl/28036'
header= {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'Accept-Encoding':'gzip, deflate, br,zstd',
           'Accept-Language':'zh-CN,zh;q=0.9',
           'cache-control':'max-age=0',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
           }
response = requests.get(url,headers=header,verify=False).content.decode('utf-8')
print(response)