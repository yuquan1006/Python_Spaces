import redis

'''连接redis'''

class RedisCmd(object):

    def connect_to_redis(self,host,port,password,db=0):
        '''
        Arguments:
            - redis_host: hostname or IP address of the Redis server.
            - redis_port: Redis port number (default=6379)
            - db: Redis keyspace number (default=0)
            - redis_password:

        Return redis connection object

        Examples:
        | ${redis_conn}=   | Connect To Redis |  redis-dev.com | 6379 |  0 |  XXxxXXxxXX |
        '''
        try:
            redis_conn = redis.Redis(host=host,port=port,db=db,password=password)
        except BaseException as e:
            print("Redis 连接异常:%s"%str(e))
            raise BaseException(str(e))
        return redis_conn

    def set_to_redis(self,redis_conn,key,data):
        """ Set data to Redis

        Arguments:
            - redis_conn: Redis connection object
            - key: String keyword to find.
            - data: String data

        Examples:
        | ${data}=   | Set To Redis |  ${redis_conn} | BARCODE|1234567890 | ${data}  |
        """
        return redis_conn.set(key, data)

    def append_to_redis(self,redis_conn,key,value):
        '''
        向Redis添加数据。如果key不存在，则使用value创建它。返回键值的新长度。
        :param redis_conn:redis连接对象
        :param key:key
        :param value:key对应的值
        :return:返回键值的新长度
        Examples:
        | ${data}=   | Append To Redis |  ${redis_conn} | 1234567890 | ${data} |

        '''
        return redis_conn.append(key,value)

    def get_from_redis(self,redis_conn,key):
        '''
        从Redis获取缓存数据
          Examples:
        | ${data}=   | Get From Redis |  ${redis_conn} |1234567890 |
        '''
        return redis_conn.get(key)

    def flush_all(self,redis_conn):
        '''
          Delete all keys from Redis
        '''
        return redis_conn.flushall()

    def delete_from_redis(self,redis_conn,key):
        '''
        Delete data from Redis
        :param redis_conn:
        :param key:
        :return:
        '''
        return redis_conn.delete(key)

    def redis_key_should_be_exist(self,redis_conn,key):
        if redis_conn.exists(key) is False:
            print("Key: " + key +" doesn't exist in Redis.")
            raise AssertionError

    def redis_key_should_not_be_exist(self,redis_conn,key):
        if redis_conn.exists(key) is True:
            print("Key: " + key +" exist in Redis.")
            raise AssertionError


    