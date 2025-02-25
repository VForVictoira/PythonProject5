import configparser

config = configparser.ConfigParser()
config ["DEFAULT"] = {
    "ServerAliveInterval": "60",
    "ServerAliveCountMax": "1",
    "Compression": "none",
    "CompressionMethod": "lz4",
}

config["bitbucket.org"]={}
config["test.com"]={}
test = config["test.com"]

test["Port"] = "80"
test['IP']='192.168.1.1'


with open('config.ini', 'w') as configfile:
    config.write(configfile)
with open('config.ini', 'r') as configfile:
    print(configfile.read())