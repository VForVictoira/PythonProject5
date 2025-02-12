import configparser

config = configparser.ConfigParser()

config.read(r'.\pip.ini')
print("遍历配置信息：")
for section in config.sections():
    print(f"section is {section}")
    for key in config[section]:
        print(f"key is {key}, value is {config[section][key]}")
