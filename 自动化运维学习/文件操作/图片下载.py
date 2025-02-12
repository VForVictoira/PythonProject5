import requests

url = "http://pic.jdtaotu.com/photo/xwebp/2028329/202832904242468.jpg"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=10)  # 设置超时，避免长时间无响应
    response.raise_for_status()  # 检查 HTTP 状态码，非 200 时抛出异常

    with open('1.jpg', 'wb') as f:
        f.write(response.content)
    print("图片下载成功！")

except requests.exceptions.RequestException as e:
    print(f"下载失败: {e}")
