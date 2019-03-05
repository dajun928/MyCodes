# 数据库 - MySQL



# 1.MySQL内容简介

**MySQL数据库，是当前应用非常广泛的一款关系型数据库**
[MySQL官网](https://link.jianshu.com/?t=https://www.mysql.com/)
[数据库排名](https://link.jianshu.com/?t=https://db-engines.com/en/ranking)

计算机诞生后，数据开始在计算机中存储并计算，并设计出了数据库系统数据库系统解决的问题：持久化存储，优化读写，保证数据的有效性
当前使用的数据库，主要分为两类

1. 文档型，如`sqlite`，就是一个文件，通过对文件的复制完成数据库的复制
2. 服务型，如`mysql`、`postgre，数据存储在一个物理文件中，但是需要使用终端以tcp/ip协议连接，进行数据库的读写操作

### E-R模型

当前物理的数据库都是按照E-R模型进行设计的

- E表示entry，实体
- R表示relationship，关系

一个实体转换为数据库中的一个表
关系描述两个实体之间的对应规则，包括

1. 一对一
2. 一对多
3. 多对多

关系转换为数据库表中的一个列在关系型数据库中一行就是一个对象
三范式
经过研究和对使用中问题的总结，对于设计数据库提出了一些规范，这些规范被称为范式

1. 第一范式（1NF)：列不可拆分
2. 第二范式（2NF)：唯一标识
3. 第三范式（3NF)：引用主键

说明：后一个范式，都是在前一个范式的基础上建立的

**执行顺序为：**

- from 表名
- where ....
- group by ...
- having ...
- order by ...
- limit star,count

实际使用中，只是语句中某些部分的组合，而不是全部

# 2.安装管理(linux)

##### 安装

```
sudo apt-get install mysql-server mysql-client
然后按照提示输入
```

##### 管理服务

```
#启动
service mysql start

#停止
service mysql stop

#重启
service mysql restart

#查询服务是否启动
netstat -tap | grep mysql
```

##### 允许远程连接

```
#找到mysql配置文件并修改
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
将bind-address=127.0.0.1注释


#登录mysql，运行命令
grant all privileges on *.* to 'root'@'%' identified by '密码' with grant option;
*.*：第一个*代表数据库名；第二个*代表表名。这里的意思是所有数据库里的所有表都授权给用户。root：授予root账号。“%”：表示授权的用户IP可以指定，这里代表任意的IP地址都能访问MySQL数据库。“password”：分配账号对应的密码，这里密码自己替换成你的mysql root帐号密码。


flush privileges;
刷新权限信息，也即是让我们所作的设置马上生效。


#重启mysql
/etc/init.d/mysql restart
```

##### 卸载管理

```
删除mysql的数据文件
sudo rm /var/lib/mysql/ -R

删除mqsql的配置文件
sudo rm /etc/mysql/ -R

自动卸载mysql的程序
sudo apt-get autoremove mysql* --purge
sudo apt-get remove apparmor
```

# window下安装Mysql

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-592d39c3c37da0b0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/476/format/webp)
>
> 双击打开MySQL5.5的数据库安装程序，进到此页面。
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-d00eb51593dde4e6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/495/format/webp)
>
> 同意协议
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-a0ddc47d7662bcc4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/497/format/webp)
>
> 一般选择典型安装
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-42b3eb5c68d22684.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/498/format/webp)
>
> 安装执行
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-861a3766e0428007.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/498/format/webp)
>
> 正在进行安装
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-d0446d21b634df36.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/704/format/webp)
>
> 下一步
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-fdf62221add57744.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/502/format/webp)
>
> 下一步
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-a208e219df7ea696.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/500/format/webp)
>
> 进行数据库设置
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-d0e062b43e45b3d6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/480/format/webp)
>
> 一般选择开发配置
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-bec33126e8050c31.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/502/format/webp)
>
> 选择开发用途机器
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-6eeec57cab3b00e9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/502/format/webp)
>
> 选择多功能数据库
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-d48031db40d2eb6f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/502/format/webp)
>
> 选择安装路径：一般默项
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-28622bd2366c23b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/506/format/webp)
>
> 直接选择下一步
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-c3783539d97f8b91.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/504/format/webp)
>
> 点下一步 不启用标准模式
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-7169b44d8dccce9c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/502/format/webp)
>
> 选择编码方式：utf-8（一般）
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-5b4f1515bbce08d2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/502/format/webp)
>
> 选择服务名字：一般默认项
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-67f40b946413b5f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/502/format/webp)
>
> 设置数据库密码（进数据库时要用的）
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-7aac6dcbf68dfca7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/504/format/webp)
>
> 执行配置
>
> 
>
> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-1312c46ade8f8acf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/506/format/webp)
>
> 四个选项都执行完毕则安装mysql成功

**注意：**

![img](https://upload-images.jianshu.io/upload_images/6078268-d4c50a1965991589.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

如果是在windows中，有时候运行MySQL会报错可以在命令窗口输入services.msc,找到服务是否打开

附：
[解决mysql不允许远程连接](https://link.jianshu.com/?t=http://jingyan.baidu.com/article/b907e627b0e3b846e7891cc9.html)
[修改MySQL用户root密码](https://link.jianshu.com/?t=http://jingyan.baidu.com/article/495ba841ef412d38b30edeb2.html)

# 3.数据的完整性

一个数据库就是一个完整的业务单元，可以包含多张表，数据被存储在表中
在表中为了更加准确的存储数据，保证数据的正确有效，可以在创建表的时候，为表添加一些强制性的验证，包括数据字段的类型、约束

##### 字段类型

在mysql中包含的数据类型很多，这里主要列出来常用的几种

1. 数字：**int,decimal**
   decimal(5,2) 整数位最多是3位，小数位最多是2位
2. 字符串：**varchar,text**
   char(10) 10个字符长度，用不完，也是10个长度
   varchar(10) 10个字符长度，用多少，是多少长度
   字符 = 字节+编码
   char因为是定长，所以查询效率高，浪费空间
   varchar因为是边长，所以节省空间，查询效率相对低
3. 日期：datetime
4. 布尔：bit(0/1)

![img](https://upload-images.jianshu.io/upload_images/6078268-408b1452fd02b5d0.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/749/format/webp)

MySQL数据类型

##### 约束

1. 主键primary key
2. 非空not null
3. 惟一unique
4. 默认default
5. 外键foreign key

##### 图形窗口操作

使用图形窗口连接 可以用windows下的navicat连接

##### 逻辑删除

- 对于重要数据，并不希望物理删除，一旦删除，数据无法找回
- 一般对于重要数据，会设置一个isDelete的列，类型为bit，表示逻辑删除
- 大于大量增长的非重要数据，可以进行物理删除
- 数据的重要性，要根据实际开发决定

# 4.脚本命令操作

使用命令连接：mysql -uroot -p 回车后输入密码

![img](https://upload-images.jianshu.io/upload_images/6078268-d194767057bc15c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/749/format/webp)

连接成功如图所示

```
#退出登录
quit或exit

#登录成功后，输入如下命令查看效果
#查看版本
select version();

#显示当前时间
select now();
注意：在语句结尾要使用分号;
```

##### 数据库操作

```
#创建数据库
create database 数据库名 charset=utf8;

#删除数据库
drop database 数据库名;

#切换数据库
use 数据库名;

#查看当前选择的数据库
select database();
```

##### 表操作

```
#查看当前数据库中所有表
show tables;

#创建表
auto_increment表示自动增长
create table 表名(列及类型);
如：

#COMMENT '主键'  是注释
create table students(
    id int auto_increment primary key  COMMENT '主键',
    sname varchar(10) not null
);

#修改表
alter table 表名 add|change|drop 列名 类型;
如：
alter table students add birthday datetime;

#删除表
drop table 表名;

#查看表结构
desc 表名;

#更改表名称
rename table 原表名 to 新表名;

#查看表的创建语句
show create table '表名';
```

##### 数据操作

```
#查询
select * from 表名

#增加
全列插入：insert into 表名 values(...)
缺省插入：insert into 表名(列1,...) values(值1,...)
同时插入多条数据：insert into 表名 values(...),(...)...;
或insert into 表名(列1,...) values(值1,...),(值1,...)...;
#主键列是自动增长，但是在全列插入时需要占位，通常使用0，插入成功后以实际数据为准


#修改
update 表名 set 列1=值1,... where 条件

#删除
delete from 表名 where 条件

#逻辑删除，本质就是修改操作update
alter table students add isdelete bit default 0;

#如果需要删除则
update students isdelete=1 where ...;
```

##### 备份与恢复

```
#数据备份
#进入超级管理员
sudo -s

#进入mysql库目录
cd /var/lib/mysql

#运行mysqldump命令
mysqldump –uroot –p 数据库名 > ~/Desktop/备份文件.sql;
#按提示输入mysql的密码




#数据恢复
#连接mysqk，创建数据库
#退出连接，执行如下命令
mysql -uroot –p 数据库名 < ~/Desktop/备份文件.sql
根据提示输入mysql密码
```

**实例：**

```
SELECT
WHERE
/*查询所有的列的内容*/
select * from x_students;
insert into x_students(name,birthday) values('冷笑','2017-06-21')

/*增加*/
alter table x_students add sex bit;

/*删除表中列*/
alter table x_students drop column sex;
alter table x_students drop column birthday;

/*删除表中行*/
delete from x_students where id=4;

/*增加表中的行*/
insert into x_students(name,sex) values('可乐',1)

/*修改表中的内容*/
UPDATE x_students set sex=1 where id=1;
UPDATE x_students set sex=0 where id=2;
UPDATE x_students set birthday=NOW() where id=5;
UPDATE x_students set birthday='1994-08-22' where id=2;
UPDATE x_students set birthday='1995-10-23' where id=1;

/*查部分列*/
SELECT name,id from x_students;

/*描述表结构*/
desc x_students

/*查看建表语句*/
show create table x_students;

/*修改表*/
alter table x_students MODIFY birthday date;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-c2d29ae43916ad59.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/327/format/webp)

数据库如图所示

```
/*如果存在表就删除*/
drop table if EXISTS x_person;

/*创建表*/  COMMENT '主键'  是注释
create table x_person(
    id int auto_increment PRIMARY KEY  COMMENT '主键',
    name varchar(10) not null,
    sex bit not null DEFAULT 1,
    idcard char(18) UNIQUE not null
);

/*查询所有的列的内容*/
SELECT * from x_person;

/*增加表中的行*/
insert into x_person(name,sex,idcard) VALUES('刘邦','1','410188000101118888')
insert into x_person(name,sex,idcard) VALUES('狄仁杰','1','410188199607228888')
insert into x_person(name,sex,idcard) VALUES('千玺','1','410188200011288888')
insert into x_person(name,sex,idcard) VALUES('后羿','0','410188200022286666')

/*修改表中的内容*/
UPDATE x_person
    set sex=0
where id=1;

UPDATE x_person set name='荆轲',sex=1 where id=2;

-- 删除 (mysql中'-- '表示单行注释)
delete from x_person where id=3;

-- 增加表中内容
update x_person
set isvalid = 0
where id = 4;

update x_person set isvalid = 1 where id = 1;
update x_person set isvalid = 1 where id = 2;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-50c8368fd3107289.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/376/format/webp)

数据库如图

#### 数据库的备份与恢复

```
#数据库备份
mysqldump -uroot -p python01 > /home/xu/python01_20170622.sql
```

![img](https://upload-images.jianshu.io/upload_images/6078268-ed6cc43b87ca67a9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/804/format/webp)

数据库备份

```
#数据库恢复
mysql -uroot -p python02 < /home/xu/python01_20170622.sql
```

![img](https://upload-images.jianshu.io/upload_images/6078268-cf2652cd175a4814.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/806/format/webp)

数据库恢复

# 5.数据库查询

## 1.创建表

```
-- 创建表x_msg
drop table if exists  x_msg;
CREATE  TABLE  x_msg (
id  INT(10)  PRIMARY KEY  ,
name  VARCHAR(20)  NOT NULL ,
sex  VARCHAR(1)  ,
birth  YEAR,
department  VARCHAR(20) ,
address  VARCHAR(50) 
);

-- 创建表x_score
drop table if exists x_score;
CREATE  TABLE  x_score (
id  INT(10)  PRIMARY KEY  AUTO_INCREMENT ,
stu_id  INT(10)  NOT NULL ,
sub_name  VARCHAR(20) ,
grade  INT(10)
);

-- 向x_msg表插入记录的INSERT语句如下：
INSERT INTO x_msg VALUES( 901,'王明哲', '男',1985,'计算机系', '北京市海淀区');
INSERT INTO x_msg VALUES( 902,'张健雄', '男',1986,'中文系', '上海市青浦区');
INSERT INTO x_msg VALUES( 903,'张梦琪', '女',1990,'中文系', '湖南省永州市');
INSERT INTO x_msg VALUES( 904,'李瑞霖', '男',1990,'英语系', '广东省中山市');
INSERT INTO x_msg VALUES( 905,'王健辉', '男',1990,'英语系', '福建省厦门市');
INSERT INTO x_msg VALUES( 906,'张妙涵', '女',1988,'计算机系', '湖南省衡阳市');

-- 向x_score表插入记录的INSERT语句如下：
INSERT INTO x_score VALUES(NULL,901, '计算机',98);
INSERT INTO x_score VALUES(NULL,901, '英语', 80);
INSERT INTO x_score VALUES(NULL,902, '计算机',92);
INSERT INTO x_score VALUES(NULL,902, '中文',88);
INSERT INTO x_score VALUES(NULL,903, '中文',95);
INSERT INTO x_score VALUES(NULL,904, '计算机',59);
INSERT INTO x_score VALUES(NULL,904, '英语',92);
INSERT INTO x_score VALUES(NULL,905, '英语',94);
INSERT INTO x_score VALUES(NULL,906, '计算机',59);
INSERT INTO x_score VALUES(NULL,906, '英语',85);

-- 查询
select * from x_msg;
select * from x_score;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-fe1c026033d9d8a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/446/format/webp)

x_msg表

![img](https://upload-images.jianshu.io/upload_images/6078268-0948a6a7c56be41e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/278/format/webp)

x_score表

## 2.查询

### 1.条件查询

```
-- 查询部分列
select id,name,sex,birth,department,address from x_msg;

-- 查询列，改别名
select id,name,sex,birth,department,address from x_msg;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-f5c4a3401cfe04bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/424/format/webp)

改过别名后的x_msg表

```
-- 去重复，根据sex
select distinct sex from x_msg;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-332a9ada6ae99b8a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/63/format/webp)

根据sex去重复

##### 去重复 select distinct

```
-- 根据性别和出生的年份去重复
select distinct sex,birth from x_msg;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-eae26a287e67e73b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/123/format/webp)

根据性别和出生的年份去重复

```
-- 条件,筛选id>900的男生
select * from x_msg
where id > 900 and sex = '男';
```

![img](https://upload-images.jianshu.io/upload_images/6078268-cc166e740d0aa21a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/443/format/webp)

筛选id>900的男生

```
-- 筛选id>900或者性别是男的学生
select * from x_msg
where id > 900 or sex = '男';
```

![img](https://upload-images.jianshu.io/upload_images/6078268-9131b6d8164976e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/444/format/webp)

筛选id>900或者性别是男的学生

```
-- 筛选成绩在70到80的学生
select * from x_score
where grade>=70 and grade <=80;

select * from x_score
where grade between 70 and 80;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-116f30bac0c16c8a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/282/format/webp)

筛选成绩在70到80的学生

```
-- 筛选成绩不等于70的学生
select * from x_score
where grade <> 70;

select * from x_score
where grade != 70;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-750aa1fac9c4bd6c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/285/format/webp)

筛选成绩不等于70的学生

### 2.模糊查询

```
-- 查询姓王的学生
select * from x_msg where name like '王%';
select * from x_msg where name like '王__';
```

![img](https://upload-images.jianshu.io/upload_images/6078268-537facc8c0e5c7b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/442/format/webp)

查询姓王的学生

```
-- 查询名字中有健的学生
select * from x_msg where name like '%健%';
```

### 3.范围查询

```
/*in表示在一个非连续的范围内*/
-- 查询编号是901或903或905的学生
select * from x_msg where id in(901,903,905);

/*between ... and ...表示在一个连续的范围内*/
-- 查询学生是902至905的学生
select * from x_msg where id between 902 and 905;

-- 查询学生是902至905的男生
select * from x_msg where id between 902 and 905 and sex='男';
```

![img](https://upload-images.jianshu.io/upload_images/6078268-0c82e16d47bbd8f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/444/format/webp)

查询编号是901或903或905的学生

### 4.空判断

```
/*空判断，注意：null与''是不同的，判空is null*/
-- 查询没有填写地址的学生
select * from x_msg where address is null;

/*判非空is not null*/
-- 查询填写了地址的学生
select * from x_msg where address is not null;

/*优先级*/
-- 小括号，not，比较运算符，逻辑运算符
-- and比or先运算，如果同时出现并希望先算or，需要结合()使用
```

![img](https://upload-images.jianshu.io/upload_images/6078268-e35bb929a94704a8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/445/format/webp)

查询填写了地址的学生

## 5.聚合

```
/*聚合*/
/*count(*)表示计算总行数，括号中写*与列名，结果是相同的*/
-- 查询学生总数
select count(*) from x_msg;

-- 查询女生的编号最大值(max，min,agv)
select max(id) from x_msg where sex='女';
```

![img](https://upload-images.jianshu.io/upload_images/6078268-15543b95e5d5842c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/87/format/webp)

查询女生编号的最大值

```
--  sum(列)表示求此列的和
select sum(grade) from x_score;

-- avg(列)表示求此列的平均值
select sub_name,avg(grade) from x_score where sub_name='计算机';
```

![img](https://upload-images.jianshu.io/upload_images/6078268-5398a096a996aab3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/194/format/webp)

求计算机学科成绩的平均值

## 6.分组

```
/*分组按照字段分组，表示此字段相同的数据会被放到一个组中
分组后，只能查询出相同的数据列，对于有差异的数据列无法出现在结果集中
可以对分组后的数据进行统计，做聚合运算*/

-- 查询男女生总数
select sex as sex, count(*)
from x_msg
group by sex;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-153a56670c01718f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/139/format/webp)

查询男女生总数

```
/*分组后的数据筛选*/
/*语法*/
select 列1,列2,聚合... from 表名
group by 列1,列2,列3...
having 列1,...聚合...

/*having后面的条件运算符与where的相同*/

-- 查询男生总人数
-- 方案一
select count(*)
from x_msg
where sex='男';

-- 方案二
select sex as '性别',count(*)
from x_msg
group by sex
having sex='男';

/*where与having的区别*/
-- where是对from后面指定的表进行数据筛选，属于对原始数据的筛选
-- having是对group by的结果进行筛选
```

![img](https://upload-images.jianshu.io/upload_images/6078268-c3020e8416bdd7f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/144/format/webp)

查询男生总人数

## 7.排序

```
/*语法：
select * from 表名
order by 列1 asc|desc,列2 asc|desc,...
将行数据按照列1进行排序，如果某些行列1的值相同时，则按照列2排序，以此类推
默认按照列值从小到大排列
asc从小到大排列，即升序
desc从大到小排序，即降序*/

-- 查询男生且生日在1990年的信息，按学号降序
select * from x_msg
where sex='男' and birth=1990
order by id desc;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-1797a69d9c32a171.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/444/format/webp)

查询男生且生日在190年的信息，按学号降序

## 8.分页

```
/*分页*/
/*语法
select * from 表名
limit start,count
从start开始，获取count条数据
start索引从0开始*/

/*
示例：分页
已知：每页显示m(pageSize)条数据，当前显示第n(pageNow)页  
求总页数：
o  查询总条数p1
o  使用p1除以m得到p2
o  如果整除则p2为总数页
o  如果不整除则p2+1为总页数
求第n页的数据
select * from students
limit (n-1)*m,m      */ 

-- 每页显示3条数据，当前显示第4页
select * from x_score
limit 9,4

-- 每页显示2条数据，当前显示第3页
select * from x_msg
limit 4,3
```

![img](https://upload-images.jianshu.io/upload_images/6078268-bf09abfda3493ae8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/283/format/webp)

将x_score表按每页两条数据分页，显示第四页的内容

![img](https://upload-images.jianshu.io/upload_images/6078268-79c8bc9c28c0ea01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/442/format/webp)

将x_msg表按每页两条数据分页，显示第三页的内容

© 著作权归作者所有

