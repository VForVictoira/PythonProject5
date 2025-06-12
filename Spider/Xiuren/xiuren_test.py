import requests
import os
html = requests.get('https://m.xsnvshen.com/album/44090').content.decode('utf-8')

main_folder = './Xiuren'
os.makedirs(main_folder, exist_ok=True)
file_path = os.path.join(main_folder, 'index3.html')
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)