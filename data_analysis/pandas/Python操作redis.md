# Python操作redis

# 1.python操作redis

#### 1.安装

- **输入命令：**

```
pip  install redis
```

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-b2730cc9f6dac11a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/748/format/webp)

#### 2.使用

```
引入模块
import redis 连接

try: 
    r=redis.StrictRedis(host='localhost',port=6379) 
except Exception,e: 
    print e.message 

方式一：根据数据类型的不同，调用相应的方法，完成读写
更多方法同上边写的命令
r.set('name','hello') 
r.get('name’) 

方式二：pipline
缓冲多条命令，然后一次性执行，减少服务器-客户端之间TCP数据库包，从而提高效率
pipe = r.pipeline() 
pipe.set('name', 'world') 
pipe.get('name') 
pipe.execute() 
```

- **封装**

```
#连接redis服务器部分是一致的
#这里将string类型的读写进行封装
import redis 
class RedisHelper(): 
    def __init__(self,host='localhost',port=6379): 
        self.__redis = redis.StrictRedis(host, port) 
        
    def get(self,key):
        if self.__redis.exists(key): 
            return self.__redis.get(key) 
        else: 
            return "" 
    
    def set(self,key,value): 
        self.__redis.set(key,value)
```

# 2.实例

```
#coding=utf-8 
import redis 
class CRedis: 
  def __init__(self): 
    self.host = 'localhost'
    self.port = 6379
    self.db = 0
    self.r = redis.Redis(host = self.host, port = self.port, db = self.db) 
  
#1. strings 类型及操作 
  #设置 key 对应的值为 string 类型的 value 
  def set(self, key, value): 
    return self.r.set(key, value) 
  #设置 key 对应的值为 string 类型的 value。如果 key 已经存在,返回 0,nx 是 not exist 的意思 
  def setnx(self, key, value): 
    return self.r.setnx(key, value) 
  #设置 key 对应的值为 string 类型的 value,并指定此键值对应的有效期 
  def setex(self, key, time, value): 
    return self.r.setex(key, time, value) 
  #设置指定 key 的 value 值的子字符串 
  #setrange name 8 gmail.com 
  #其中的 8 是指从下标为 8(包含 8)的字符开始替换 
  def setrange(self, key, num, value): 
    return self.r.setrange(key, num, value) 
  #获取指定 key 的 value 值的子字符串 
  def getrange(self, key, start ,end): 
    return self.r.getrange(key, start, end) 
  #mget(list) 
  def get(self, key): 
    if isinstance(key, list): 
      return self.r.mget(key) 
    else: 
      return self.r.get(key) 
  #删除 
  def remove(self, key): 
    return self.r.delete(key) 
  #自增 
  def incr(self, key, default = 1): 
    if (1 == default): 
      return self.r.incr(key) 
    else: 
      return self.r.incr(key, default) 
  #自减 
  def decr(self, key, default = 1): 
    if (1 == default): 
      return self.r.decr(key) 
    else: 
      return self.r.decr(key, default) 
  
#2. hashes 类型及操作 
  #根据email获取session信息 
  def hget(self, email): 
    return self.r.hget('session', email) 
  #以email作为唯一标识，增加用户session 
  def hset(self, email, content): 
    return self.r.hset('session', email, content) 
  #获取session哈希表中的所有数据 
  def hgetall(self): 
    return self.r.hgetall('session') 
  #删除hashes 
  def hdel(self, name, key = None): 
    if(key): 
      return self.r.hdel(name, key) 
    return self.r.hdel(name) 
  #清空当前db 
  def clear(self): 
    return self.r.flushdb() 
 
#3、lists 类型及操作 
  #适合做邮件队列 
  #在 key 对应 list 的头部添加字符串元素 
  def lpush(self, key ,value): 
    return self.r.lpush(key, value) 
  #从 list 的尾部删除元素,并返回删除元素 
  def lpop(self, key): 
    return self.r.plush(key) 

if __name__ == '__main__': 
  r = CRedis()
```

# 3.Redis缓存Mysql模拟用户登录，Python实现实例

- **整体逻辑如下：**

> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-abccf1978d2ddddf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/588/format/webp)
>
> 
>
> 1 .
>
> 用户登录首先判断是否在redis缓存中，如果在redis缓存中，直接登录成功；
>
> 
>
> 2 .
>
> 若用户未在redis缓存，则访问Mysql，判断用户是否存在，如果不存在，则提示用户注册；如果存在，则登录成功；
>
> 
>
> 3 .
>
> 在Mysql存在并登录成功的同时，将改条数据用Redis Hash类型进行缓存，并设置过期时间为20分钟；
>
> 

```
import redis

pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
r = redis.Redis(connection_pool=pool)
class Redis_login():
    def __init__(self,user,pwd):
        # user = input('请输入用户名\n')
        # pwd = input('请输入密码\n')
        r.mset(user1='123',user2='1234',user3='12345')
    def login(self):
        ls = []
        for key in r.keys():
            ls.append(key.decode('utf-8'))
        if user not in ls:
            print('用户名错误请重新输入')
        elif r.get(user).decode('utf-8') == pwd:
            print('登录成功！！！')
        else:
            red.not_login()
    def not_login(self):
        print('输入错误请重新输入')

if __name__ == '__main__':
    while True:
        user = input('请输入用户名\n')
        pwd = input('请输入密码\n')
        red = Redis_login(user,pwd)
        red.login()
```

© 著作权归作者所有
