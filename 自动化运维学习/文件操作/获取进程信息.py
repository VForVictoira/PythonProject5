import psutil

for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
    if proc.info['name'].startswith('WeChat'):
        print(proc.info)
