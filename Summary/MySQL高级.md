# MySQL高级





# 1.mysql高级

## 1.关系

![img](https://upload-images.jianshu.io/upload_images/6078268-7fbb067dbab173de.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

创建学生成绩关系表

```
drop table if exists scores;
drop table if exists students;
drop table if exists subjects;

create table students(
    id int auto_increment primary key,
    sname varchar(20)
);

create table subjects(
    id int auto_increment primary key,
    stitle varchar(20)
);

/*
create table scores(
    id int auto_increment primary key,
    stuid int,
    subid int,
    score decimal(5,2),
    foreign key(stuid) references students(id),   #引用的第一种写法
    foreign key(subid) references subjects(id)
);
*/
create table scores(
    id int auto_increment primary key,
    stuid int,
    subid int,
    score decimal(5,2)
);

#引用的第二种写法
alter table scores
add constraint fk_scores_stuid foreign key(stuid)
references students(id) on delete cascade;  #外键的级联操作

alter table scores
add constraint fk_scores_subid foreign key(subid)
references subjects(id) on delete cascade;


insert into students(sname) values('小茗');
insert into students(sname) values('可乐');
insert into students(sname) values('小伊');
insert into subjects(stitle) values('语文');
insert into subjects(stitle) values('数学');
insert into subjects(stitle) values('英语');

select * from students;
select * from subjects;
select * from scores;

insert into scores(stuid,subid,score) values(1,1,88);
insert into scores(stuid,subid,score) values(1,2,90);
insert into scores(stuid,subid,score) values(2,3,99);
insert into scores(stuid,subid,score) values(2,1,70);

-- 查询一个学生各科的成绩
select t1.id,t1.sname,t2.score
from students t1,scores t2
where t1.id = t2.stuid;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-d64569751e3d787e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/347/format/webp)

三张表如图

![img](https://upload-images.jianshu.io/upload_images/6078268-8b77f1f52a1c2383.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/187/format/webp)

查询一个学生各科成绩的结果

**级联操作的类型包括：**

- restrict（限制）：默认值，抛异常
- cascade（级联）：如果主表的记录删掉，则从表中相关联的记录都将被删除
- set null：将外键设置为空
- no action：什么都不做

## 2.连接查询

- 当需要对有关系的多张表进行查询时，需要使用连接 **join**

**连接查询分类如下：**

- `表A inner join 表B`：表A与表B匹配的行会出现在结果中
- `表A left join 表B`：表A与表B匹配的行会出现在结果中，外加表A中独有的数据，未对应的数据使用null填充
- `表A right join 表B`：表A与表B匹配的行会出现在结果中，外加表B中独有的数据，未对应的数据使用null填充


- 在查询或条件中推荐使用“表名.列名”的语法
- 如果多个表中列名不重复可以省略“表名.”部分
- 如果表的名称太长，可以在表名后面使用' as 简写名'或' 简写名'，为表起个临时的简写名称

**实例一**

```
-- 先建立关系表
drop table if exists x_emp;
drop table if exists x_dept;
create table x_dept(
     id int auto_increment primary key,
     dname varchar(20)
);
create table x_emp(
     id int auto_increment primary key,
     ename varchar(20),
     did int not null,
     mgr int, 
     foreign key(did) references x_dept(id),
     foreign key(mgr) references x_emp(id)
);
insert into x_dept(dname) values('研发部');
insert into x_dept(dname) values('人事部');
insert into x_dept(dname) values('财务部');

insert into x_emp(ename,did,mgr) values('老王',1,null);
insert into x_emp(ename,did,mgr) values('老张',1,1);
insert into x_emp(ename,did,mgr) values('老赵',1,1);
insert into x_emp(ename,did,mgr) values('小茗',2,3);
insert into x_emp(ename,did,mgr) values('小伊',2,3);

select * from x_dept;
select * from x_emp;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-41a9124deff23372.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/383/format/webp)

创建的两个表

```
/*查询员工的编号，姓名，上级的姓名*/
select * from x_emp 员工表,x_emp 上级表
where 员工表.mgr = 上级表.id;

-- 第一种写法
select t1.id,t1.ename,t2.ename
from x_emp t1,x_emp t2
where t1.mgr = t2.id;

-- 第二种写法
select t1.id,t1.ename,t2.ename
from x_emp t1
inner join x_emp t2
on t1.mgr = t2.id;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-5e2c90d4285bd5bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/190/format/webp)

查询员工额编号，姓名，上级的姓名

```
-- 'left',表x_emp与表x_dept匹配的行会出现在结果中，外加表x_emp中独有的数据，未对应的数据使用null填充
select * 
from x_emp left outer join x_dept
on x_emp.did = x_dept.id;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-19faab48052e3d1e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/339/format/webp)

left

```
-- 'right',表x_emp与表x_dept匹配的行会出现在结果中，外加表x_dept中独有的数据，未对应的数据使用null填充
select * 
from x_emp right outer join x_dept
on x_emp.did = x_dept.id;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-0193681e148bcee3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/340/format/webp)

right

```
/*x_emp中，查询是经理的人的名字
    1、哪些是经理啊？
    2、再找名字
*/
select ename 
from x_emp 
where id in(
    select mgr from x_emp
);
```

![img](https://upload-images.jianshu.io/upload_images/6078268-2191de912dc96942.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/72/format/webp)

查询哪些是经理

**实例二**

```
drop table if exists scores;
drop table if exists students;
drop table if exists subjects;

create table students(
    id int auto_increment primary key,
    sname varchar(20)
);

create table subjects(
    id int auto_increment primary key,
    stitle varchar(20)
);


create table scores(
    id int auto_increment primary key,
    stuid int,
    subid int,
    score decimal(5,2),
    foreign key(stuid) references students(id),
    foreign key(subid) references subjects(id)
);

insert into students(sname) values('小茗');
insert into students(sname) values('可乐');
insert into students(sname) values('小伊');
insert into subjects(stitle) values('语文');
insert into subjects(stitle) values('数学');
insert into subjects(stitle) values('英语');

insert into scores(stuid,subid,score) values(1,1,88);
insert into scores(stuid,subid,score) values(1,2,90);
insert into scores(stuid,subid,score) values(2,3,99);
insert into scores(stuid,subid,score) values(3,1,70);

select * from students;
select * from subjects;
select * from scores;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-b52a7624b3c4e477.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/549/format/webp)

创建的三个表

```
/*查询学生的编号，姓名，科目的名称，成绩*/
-- 三种方法都可以

select t1.id,t1.sname,t2.stitle,t3.score
from students t1,subjects t2,scores t3
where t3.stuid = t1.id and t3.subid = t2.id;

select t1.id,t1.sname,t2.stitle,t3.score
from scores t3
inner join students t1
on t3.stuid = t1.id 
inner join subjects t2
on t3.subid = t2.id;


select t1.id,t1.sname,t2.stitle,t3.score
from  students t1
inner join scores t3
on t3.stuid = t1.id 
inner join subjects t2
on t3.subid = t2.id;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-cef7b7eaa0a7de74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/235/format/webp)

查询学生的编号，姓名，科目的名称，成绩

**实例三**

```
drop table if exists emp1;
drop table if exists salgrade;
create table emp1(
     id int auto_increment primary key,
   name VARCHAR(20),
     sal int
);
create table salgrade(
     id int auto_increment primary key,
     low int,
     high int
);
insert into emp1(name,sal) values('小茗',4000);
insert into emp1(name,sal) values('可乐',5000);
insert into emp1(name,sal) values('小伊',8800);

insert into salgrade(low,high) values(1000,3999);
insert into salgrade(low,high) values(4000,7999);
insert into salgrade(low,high) values(8000,10000);

select * from emp1;
select * from salgrade;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-8347dc03385d91f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/389/format/webp)

创建的两个表

```
-- 查询员工的编号，工资和等级
select t1.id,t1.name,t1.sal,t2.id
from emp1 t1 inner join salgrade t2
on t1.sal between t2.low and t2.high;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-1abafd6bfa5a58eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/216/format/webp)

查询员工的编号，工资和等级

```
create view myView2
as
select * from emp1;

delete from emp1;
select * from myView2;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-6316d76ff9911d2e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/154/format/webp)

delete from emp1后，表emp1数据为空

**实例四**

```
/*查询各学生的语文、数学、英语的成绩*/
select sname,
(select sco.score from scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='语文' and stuid=stu.id) as 语文,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='数学' and stuid=stu.id) as 数学,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='英语' and stuid=stu.id) as 英语
from students stu;

-- 这里我们可以用视图来查询，视图的用途就是查询

/*视图*/
create view myView 
as
select sname,
(select sco.score from scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='语文' and stuid=stu.id) as 语文,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='数学' and stuid=stu.id) as 数学,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='英语' and stuid=stu.id) as 英语
from students stu;


select * from myView;
select sname from myView;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-5ae191d756422518.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/234/format/webp)

查询各学生的语文、数学、英语的成绩

![img](https://upload-images.jianshu.io/upload_images/6078268-425624ec15f270f5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/459/format/webp)

用视图以后查询的结果如图

## 事务

- 当一个业务逻辑需要多个sql完成时，如果其中某条sql语句出错，则希望整个操作都退回，保证数据的正确性。
- 使用事务可以完成退回的功能，保证业务逻辑的正确性
- 两个功能：有一个出问题，回滚。都没有问题，提交。(同生共死)

##### 事务四大特性(简称ACID)

- 原子性(Atomicity)：事务中的全部操作在数据库中是不可分割的，要么全部完成，要么均不执行
- 一致性(Consistency)：几个并行执行的事务，其执行结果必须与按某一顺序串行执行的结果相一致
- 隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须是透明的
- 持久性(Durability)：对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障

要求：表的类型必须是innodb或bdb类型(表的默认类型就是innodb)，才可以对此表使用事务

**查看表的创建语句**
show create table students;

**修改表的类型**
alter table '表名' engine=innodb;

**事务语句**

- 开启`begin`;
- 提交`commit`;
- 回滚`rollback`;

**示例**

```
drop table if exists bank;
create table bank(
    id int primary key,
    name varchar(20),
    money int 
);
insert into bank values(1,'王明哲',100);
insert into bank values(2,'张妙涵',1);
select * from bank;
update bank set money = money-10 where id=1;
update bank set money = money+10 where id=2;
select * from bank;
```

```
-- 查看建表语句
show create table students;

CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8
-- 从建表语句中我们可以看出默认的是InnoDB类型
```

```
/*事务，一般用来做测试*/
begin;
delete from bank; 
rollback;
commit;
```

![img](https://upload-images.jianshu.io/upload_images/6078268-1f57627b580f432e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/613/format/webp)

用事务来进行测试

# 3.内置函数

### 1.字符串函数

```
/*字符串函数,sql里函数都是有返回值的*/
-- 查看字符的ascii码值ascii(str)，str是空串时返回0
select ascii('a');
97

-- 查看ascii码值对应的字符char(数字)
select char(97);
a

-- 拼接字符串concat(str1,str2...)
select concat(12,34,'ab','小茗');
1234ab小茗

-- 包含字符个数length(str)
select length('中a')
4
select length(ename),ename from x_emp;


/*截取字符串
left(str,len)返回字符串str的左端len个字符
right(str,len)返回字符串str的右端len个字符
substring(str,pos,len)返回字符串str的位置pos起len个字符*/

select substring('abc123',2,3);
bc1


/*去除空格
ltrim(str)返回删除了左空格的字符串str
rtrim(str)返回删除了右空格的字符串str
trim([方向 remstr from str)返回从某侧删除remstr后的字符串str，方向词包括both、leading、trailing，表示两侧、左、右*/
select trim('  bar   ');
bar

select trim(leading 'x' FROM 'xxxbarxxx');
barxxx

select trim(both 'x' FROM 'xxxbarxxx');
bar

select trim(trailing 'x' FROM 'xxxbarxxx');
xxxbar

--返回由n个空格字符组成的一个字符串space(n)
select space(10);

-- 替换字符串replace(str,from_str,to_str)
select replace('abc123','123','def');

-- 大小写转换，函数如下
lower(str)
upper(str)
select lower('aBcD');
```

### 2.数学函数

```
-- 求绝对值abs(n)
select abs(-32);
32

-- 求m除以n的余数mod(m,n)，同运算符%
select mod(10,3);
1
select 10%3;
1

-- 地板floor(n)，表示不大于n的最大整数
select floor(2.3);
2

-- 天花板ceiling(n)，表示不小于n的最大整数
select ceiling(2.3);
3

-- 求四舍五入值round(n,d)，n表示原数，d表示小数位置，默认为0
select round(1.6);
2

-- 求x的y次幂pow(x,y)
select pow(2,3);
8

-- 获取圆周率PI()
select PI();
3.141593

-- 随机数rand()，值为0-1.0的浮点数
select rand();
0.7000933091157053

select floor(2.3),ceil(2.3),round(2.3456,2);
2          3          2.35
```

### 3.日期函数

**获取子值，语法如下:**

- `year(date)`返回date的年份(范围在1000到9999)
- `month(date)`返回date中的月份数值
- `day(date)`返回date中的日期数值
- `hour(time)`返回time的小时数(范围是0到23)
- `minute(time)`返回time的分钟数(范围是0到59)
- `second(time)`返回time的秒数(范围是0到59)
- 日期计算，使用+-运算符，数字后面的关键字为year、month、day、
  hour、minute、second
- 日期格式化date_format(date,format)，format参数可用的值如下
- 获取年%Y，返回4位的整数
- 获取年%y，返回2位的整数
- 获取月%m，值为1-12的整数
- 获取日%d，返回整数
- 获取时%H，值为0-23的整数
- 获取时%h，值为1-12的整数
- 获取分%i，值为0-59的整数
- 获取秒%s，值为0-59的整数

```
/*日期-->字符串*/
select date_format('2017-10-20','%Y年%m月%d日')
2017年10月20日

/*字符串-->日期*/
select str_to_date('2017年10月20日','%Y年%m月%d日')
2017-10-20

-- 当前日期current_date()
select current_date();
2017-06-23

-- 当前时间current_time()
select current_time();
21:21:55

-- 当前日期时间now()
select now();
2017-06-23 21:21:41
```

```
create table t1(
    id int,
    birthday date
);
insert into t1 values(1,'2017-10-20');
insert into t1 values(2,'2017/10/20');
insert into t1 values(3,str_to_date('2017年10月21日','%Y年%m月%d日'));
insert into t1 values('4','2017/10/20');
select * from t1;

/*日期-->字符串*/
select date_format('2017-10-20','%Y年%m月%d日')
/*字符串-->日期*/
select str_to_date('2017年10月20日','%Y年%m月%d日')

select current_date(),now();
```

# 4.时间与字符串的相互转换

```
import time
import  datetime

stime1 = '2015年10月20日'
#字符串--->时间time.struct_time
time1 = time.strptime(stime1,'%Y年%m月%d日')
print(time1)
结果：
time.struct_time(tm_year=2015, tm_mon=10, tm_mday=20, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=293, tm_isdst=-1)


#时间time.struct_time--->字符串
stime1 = time.strftime('%Y-%m-%d',time1)
print(stime1)
结果：
2015-10-20
```

```
dt = datetime.datetime.now()
print(dt)
结果：
2017-06-24 14:59:09.948008
```

```
dt = datetime.date(2017,6,24)
print(str(dt))
print(type(dt))
结果：
2017-06-24
<class 'datetime.date'>


dt = datetime.datetime(2017,6,24,14,23,45)
print(dt)
结果：
2017-06-24 14:23:45

dt = datetime.date(2017,6,24)
print(dt.timetuple())
结果：
time.struct_time(tm_year=2017, tm_mon=6, tm_mday=24, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=175, tm_isdst=-1)

dt = datetime.date(2017,6,24)
s = time.strftime('%Y/%m/%d',dt.timetuple())
print(s)
结果：
2017/06/24
```

© 著作权归作者所有

