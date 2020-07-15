#python 连接redis集群
from rediscluster import RedisCluster
#构建所有的节点
startup_nodes = [
    {"host":"192.168.160.131", "port":7000},  # 主
    {"host":"192.168.160.132", "port":7003},  # 7000的从数据库
    {"host":"192.168.160.131", "port":7001},  # 主
    {"host":"192.168.160.132", "port":7004},  # 7001的从数据库
    {"host":"192.168.160.131", "port":7002},  # 主
    {"host":"192.168.160.132", "port":7005}   # 7002的从数据库
]
#构建StrictRedisCluster对象
redis_store= RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
# 设置key键为name、money; value值为 '老鹰'、'10亿'
redis_store.set('name', '老鹰')
redis_store.set('money', '10亿')
# 获取键为name,money
print("My name is: ", redis_store.get('str5'))
print("I have money: ", redis_store.get('money'))