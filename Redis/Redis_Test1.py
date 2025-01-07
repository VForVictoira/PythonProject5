import redis

#client = redis.StrictRedis()
client2  = redis.StrictRedis(host='192.168.0.109', port=6379, db=0)

client2.sadd('set2','https://www.baidu.com')