import requests
#d ='[XiuRen]高清写真图 2024.07.18 No.8880 陆萱萱 性感美腿'
#title = result = re.search(r"No\.\d+", d).group(0)
url = 'https://xx.knit.bid/static/images/2021/09/23/%E6%91%84%E5%BD%B1%E5%B8%88mix%E5%A4%9A%E4%BD%8D%E6%A8%A1%E7%89%B9%E5%A4%A7%E5%B0%BA%E5%BA%A6%E6%97%A0%E5%9C%A3%E5%85%89%E4%BD%9C%E5%93%81%5B156P%5D/3592b279d59c97615cac3.jpg'
pic =requests.get(url).content.decode('utf8')

print(pic)
