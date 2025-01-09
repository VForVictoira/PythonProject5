import redis

#client = redis.StrictRedis()
client2  = redis.StrictRedis(host='192.168.0.109', port=6379, db=0)

#client2.sadd('URL_LIST','https://www.baidu.com')
if client2.sadd('URL_LIST','https://www.baidu.com') == 1:
    print('success')
else:
    print('fail')