import requests
import json

url = 'https://exercise.kingname.info/exercise_headers_backend'
header1= {
    'Accept': '*./*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Host': 'exercise.kingname.info',
    'anhao':'kingname',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection-Type': 'keep-alive',
    'referer': 'https://exercise.kingname.info/exercise_headers.html',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'

    }
response = requests.get(url,headers= header1).content.decode()
html = json.loads(response)
print(html)
