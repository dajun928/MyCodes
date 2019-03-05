# MySQL与Python的交互

# 1.交互类型

## 1.安装引入模块

- 安装`mysql`模块，在`windows`和`ubuntu`中

![img](https://upload-images.jianshu.io/upload_images/6078268-4c407d7a91966bb4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

windows里安装mysql模块

![img](https://upload-images.jianshu.io/upload_images/6078268-e3ddbeda314d79bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/518/format/webp)

Linux里安装mysql模块

- 在文件中引入模块
  `import pymysql`

#### 1.Connection对象

- 用于建立与数据库的连接
- 创建对象：调用`connect()`方法
  `conn=connect`(参数列表)
- 参数host：连接的mysql主机，如果本机是'localhost'
- 参数port：连接的mysql主机的端口，默认是3306
- 参数db：数据库的名称
- 参数user：连接的用户名
- 参数password：连接的密码
- 参数charset：通信采用的编码方式，默认是'gb2312'，要求与数据库创建时指定的编码一致，否则中文会乱码

#### 2.对象的方法

- `close()`关闭连接
- `commit()`事务，所以需要提交才会生效
- `rollback()`事务，放弃之前的操作
- `cursor()`返回Cursor对象，用于执行sql语句并获得结果

**Cursor对象**

- 执行sql语句
- 创建对象：调用Connection对象的`cursor()`方法
  `cursor1=conn.cursor()`

**对象的方法**

- `close()`关闭
- `execute(operation [, parameters ])`执行语句，返回受影响的行数
- `fetchone()`执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
- `next()`执行查询语句时，获取当前行的下一行
- `fetchall()`执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
- `scroll(value[,mode])`将行指针移动到某个位置
- `mode`表示移动的方式
- mode的默认值为relative，表示基于当前行移动到value，value为正则向下移动，value为负则向上移动。相对的
- mode的值为absolute，表示基于第一条数据的位置，第一条数据的位置为0，绝对的。

**举个例子便于理解**

```
# 导入python操作mysql的模块
import pymysql

# 获取连接对象
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='python01', port=3306, charset='utf8')
# 获取执行工具
cur = conn.cursor()
# sql语句,增删改
#sql = 'select birthday from t_user'
sql = 'select id,name,pwd,birthday from t_user'
# 执行,返回值。如果是增删改，返回受影响的行数，如果是查询，返回查询的行数
count = cur.execute(sql)
print('查询的结果有%s条数据'%count)

#获取第一行
dateOne = cur.fetchone()
print(dateOne)

#向上移动一行
cur.scroll(-1)

#向下移动一行
cur.scroll(1)

cur.scroll(1,mode='absolute')   绝对的，这里指的是第一行
cur.scroll(1,mode='relative')   相对的

#获取所有行的数据
dataAll = cur.fetchall()
print(dataAll)

for temp in dataAll:
     print(temp)
     print(dataAll[-1][2])      #dataAll[-1]得到的是一个用户所有的信息，dataAll[-1][2]获取最后一个人的密码


for temp in cur:
     print(temp)


s = 'id:%s,name:%s,pwd:%s,birthday:%s'
for temp in dataAll:
    print(s%(temp[0],temp[1],temp[2],temp[3]))

# 关闭
cur.close()
conn.close()
```

#### 3.对象的属性

- rowcount只读属性，表示最近一次`execute()`执行后受影响的行数
- connection获得当前连接对象

# 2.增删改查(CRUD)

## 1.增

- 创建testInsert.py文件，向学生表中插入一条数据

```
#encoding=utf-8
import pymysql
try:
    conn=pymysql.connect(host='localhost',port=3306,db='test1',user='root',passwd='mysql',charset='utf8')
    cs1=conn.cursor()
    count=cs1.execute("insert into students(sname) values('张良')")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception,e:
    print(e)
```

## 2.修改

- 创建testUpdate.py文件，修改学生表的一条数据

```
#encoding=utf-8
import pymysql
try:
    conn=pymysql.connect(host='localhost',port=3306,db='test1',user='root',passwd='mysql',charset='utf8')
    cs1=conn.cursor()
    count=cs1.execute("update students set sname='刘邦' where id=6")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception,e:
    print(e)
```

## 3.删除

- 创建testDelete.py文件，删除学生表的一条数据

```
#encoding=utf-8
import pymysql
try:
    conn=pymysql.connect(host='localhost',port=3306,db='test1',user='root',passwd='mysql',charset='utf8')
    cs1=conn.cursor()
    count=cs1.execute("delete from students where id=6")
    print(count)
    conn.commit()
    cs1.close()
    conn.close()
except Exception as e:
    print(e)
```

## 4.查

- 创建testSelectOne.py文件，查询一条学生信息

```
import Pymysql
try:
    conn=Pymysql.connect(host='localhost',port=3306,db='test1',user='root',passwd='mysql',charset='utf8')
    cur=conn.cursor()
    cur.execute('select * from students where id=7')
    result=cur.fetchone()
    print result
    cur.close()
    conn.close()
except Exception as e:
    print(e)
```

- 创建testSelectMany.py文件，查询全部学生信息

```
#encoding=utf8
import Pymysql
try:
    conn=Pymysql.connect(host='localhost',port=3306,db='test1',user='root',passwd='mysql',charset='utf8')
    cur=conn.cursor()
    cur.execute('select * from students')
    result=cur.fetchall()
    print result
    cur.close()
    conn.close()
except Exception as e:
    print(e)
```

**实例一：参数**

```
# 导入python操作mysql的模块
import pymysql
import time

# 获取连接对象
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='python01', port=3306, charset='utf8')
# 获取执行工具
cur = conn.cursor()
# sql语句,增删改，sql注入
sql = 'insert into t_user(name,pwd,birthday) values(%s,%s,%s)'
# 参数列表
name = input('输入姓名:')
pwd = input('输入密码:')
birthday = input('输入生日:')     # 2017年10月01日-->日期struct_time(--->2017-10-01)
birthday = time.strptime(birthday,'%Y年%m月%d日')      #这里我们就用到了时间与字符串的相互转换(详情见MySQL高级)

params = [name,pwd,birthday]
# 执行,返回值。如果是增删改，返回受影响的行数，如果是查询，返回查询的行数
count = cur.execute(sql,params)
#提交
conn.commit()
print('受影响的行数:%s'%count)
# 关闭
cur.close()
conn.close()
```

**实例二：抛出异常**

```
# 导入python操作mysql的模块
import pymysql

try:
    conn = None
    cur = None
    # 获取连接对象
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='123456',
                           database='python01',
                           port=3306,
                           charset='utf8')
    # 模拟异常
    # a = 1 / 0
    # 获取执行工具
    cur = conn.cursor()
    # sql语句,增删改
    sql = 'insert into t_user(name,pwd,birthday) values("小伊","123456",str_to_date("2017年10月20日","%Y年%m月%d日"))'
    # 执行,返回值。如果是增删改，返回受影响的行数，如果是查询，返回查询的行数
    count = cur.execute(sql)
    # 提交
    conn.commit()
    print('受影响的行数:%s' % count)
except Exception as ex:
    # 打印异常信息，测试时候使用，项目上线，去掉
    print(str(ex))
    # 将异常继续抛出
    # raise
finally:
    if cur != None:
        cur.close()
    if conn != None:
        conn.close()
```

**实例三：**

```
# 导入python操作mysql的模块
import pymysql

# 获取连接对象
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='python01', port=3306, charset='utf8')
# 获取执行工具
cur = conn.cursor()
# sql语句,增删改
#sql = 'select birthday from t_user'
sql = 'select id,name,pwd,birthday from t_user'
# 执行,返回值。如果是增删改，返回受影响的行数，如果是查询，返回查询的行数
count = cur.execute(sql)
print('查询的结果有%s条数据'%count)

#获取第一行
# dateOne = cur.fetchone()
# print(dateOne)


# for temp in cur:
#     print(temp)


s = 'id:%s,name:%s,pwd:%s,birthday:%s'
for temp in dataAll:
    print(s%(temp[0],temp[1],temp[2],temp[3]))

# 关闭
cur.close()
conn.close()
```

# 3.封装

这个库的名字：mySqlHelper

```
    python操作mysql进行增删改查的封装

    1、增删改，代码类似
    2、查询

    代码分析
    1、获取连接对象
    2、sql语句不同，参数不同
    3、获取执行对象
        增删改
        查询
            1、fetchone
            2、fetchall
    4、处理结果
    5、关闭

    面向对象  建立类，封装属性和函数 '''

import pymysql
class MysqlHelper:
    '''python操作mysql的增删改查的封装'''

    def __init__(self, host, user, password, database, port=3306, charset='utf8'):
        '''
        初始化参数
        :param host:        主机
        :param user:        用户名
        :param password:    密码
        :param database:    数据库
        :param port:        端口号，默认是3306
        :param charset:     编码，默认是utf8
        '''
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset

    def connect(self):
        '''
        获取连接对象和执行对象
        :return:
        '''
        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    database=self.database,
                                    port=self.port,
                                    charset=self.charset)

        self.cur = self.conn.cursor()

    def fetchone(self, sql, params=None):
        '''
         根据sql和参数获取一行数据
       :param sql:          sql语句
       :param params:       sql语句对象的参数元组，默认值为None
       :return:             查询的一行数据
       '''
        dataOne = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                dataOne = self.cur.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataOne

    def fetchall(self, sql, params=None):
        '''
         根据sql和参数获取一行数据
       :param sql:          sql语句
       :param params:       sql语句对象的参数列表，默认值为None
       :return:             查询的一行数据
       '''
        dataall = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                dataall = self.cur.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataall

    def __item(self, sql, params=None):
        '''
        执行增删改
        :param sql:           sql语句
        :param params:        sql语句对象的参数列表，默认值为None
        :return:              受影响的行数
        '''
        count = 0
        try:
            count = self.cur.execute(sql, params)
            self.conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return count

    def update(self, sql, params=None):
        '''
        执行修改
        :param sql:     sql语句
        :param params:  sql语句对象的参数列表，默认值为None
        :return:        受影响的行数
        '''
        return self.__item(sql, params)

    def insert(self, sql, params=None):
        '''
        执行新增
        :param sql:     sql语句
        :param params:  sql语句对象的参数列表，默认值为None
        :return:        受影响的行数
        '''
        return self.__item(sql, params)

    def delete(self, sql, params=None):
        '''
        执行删除
        :param sql:     sql语句
        :param params:  sql语句对象的参数列表，默认值为None
        :return:        受影响的行数
        '''
        return self.__item(sql, params)

    def close(self):
        '''
        关闭执行工具和连接对象
        '''
        if self.cur != None:
            self.cur.close()
        if self.conn != None:
            self.conn.close()
```

### 1.测试查询多条数据

```
import mysqlHelper

# 初始化对象
helper = mysqlHelper.MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
# 连接
helper.connect()
# sql
sql = 'select * from t_user where name = %s and id > %s'
# params
params = ['小茗',1]
# 执行
data = helper.fetchall(sql, params)
# 判断
if data:
    for temp in data:
        print(temp)
else:  # None,False,0
    print('没有数据.')

helper.close()
```

### 2.测试查询一条数据

```
import mysqlHelper

# 初始化对象
helper = mysqlHelper.MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
# 连接
helper.connect()
# sql
sql = 'select * from t_user where id = %s'
#sql = 'select * from t_user where id = 1'
# params
params = [2]
# 执行
data = helper.fetchone(sql, params)
#data = helper.fetchone(sql)
# 判断
if data:
    print(data)
else:  # None,False,0
    print('没有数据.')
```

### 3.测试增删改

```
import mysqlHelper
import time

# 初始化对象
helper = mysqlHelper.MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
# 连接
helper.connect()
# sql
sql = 'update t_user set name =%s,pwd=%s,birthday=%s where id=%s'
# params
id = input('输入编号:')
name = input('输入姓名:')
pwd = input('输入密码:')
birthday = time.strptime(input('输入生日:'), '%Y年%m月%d日')
params = [name, pwd, birthday,id]
# 执行
count = helper.update(sql, params)
# 判断
if count:
    print('操作成功.')
else:  # None,False,0
    print('操作失败.')
```

### 4.登录和注册

登录和注册的时候需要对密码进行加密

注意：

- 需要对密码进行加密
- 如果使用md5加密，则密码包含32个字符
- 如果使用sha1加密，则密码包含40个字符，这里使用这种方式

```
create table userinfos(
    id int primary key auto_increment,
    uname varchar(20),
    upwd char(40),
    isdelete bit default 0
);

/*
ret = doPwd('123')
print(ret)
结果：40bd001563085fc35165329ea1ff5c5ecbdbbeef
              */

-- 插入如下数据，用户名为123,密码为123,这是sha1加密后的值
insert into userinfos 
values(1,'123','40bd001563085fc35165329ea1ff5c5ecbdbbeef',0);
```

**登录与注册**

```
from mysqlHelper import MysqlHelper
import hashlib


def login():
    '''登录'''
    name = input('输入用户名:')
    pwd = input('输入密码:')
    #加密
    pwd = doPwd(pwd)

    helper = MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
    helper.connect()
    sql = 'select * from t_user where name=%s and pwd=%s'
    params = [name, pwd]
    data = helper.fetchone(sql, params)
    if data:
        print('登录成功.')
    else:  # None,False,0
        print('登录失败.')


def doPwd(pwd):
    '''sha1编码'''
    mysha1 = hashlib.sha1()
    mysha1.update(pwd.encode('utf-8'))
    pwd = mysha1.hexdigest()
    return pwd


def register():
    '''注册'''
    name = input('输入用户名:')
    pwd = input('输入密码:')
    # 加密
    pwd = doPwd(pwd)


    helper = MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
    helper.connect()
    sql = 'insert into t_user(name,pwd) values(%s,%s)'
    params = [name, pwd]
    count = helper.insert(sql, params)
    if count:
        print('操作成功.')
    else:  # None,False,0
        print('操作失败.')


if __name__ == '__main__':
    #register()
    login()
```

© 著作权归作者所有
