# 文件的打开与关闭-IO

# 1.文件的目的

就是把一些存储存放起来，可以让程序下一次执行的时候直接使用，而不必重新制作一份，省时省力

# 2.**文件的打开与关闭**

如果想用word编写一份简历，应该有哪些流程呢？

1.打开word软件，新建一个word文件

2.写入个人简历信息

3.保存文件

4.关闭word软件

同样，在操作文件的整体过程与使用word编写一份简历的过程是很相似的

1.打开文件，或者新建立一个文件

2.读/写数据

3.关闭文件

## �2.1**打开文件**

在python，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件

open(文件名，访问模式)

示例如下： f = open('test.txt','w')

说明:

![img](https://upload-images.jianshu.io/upload_images/6078268-d8ad701be13333c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

### 2.2关闭文件

lose( )

示例如下：

\#新建一个文件，文件名为:test.txt

f = open('test.txt','w')

\#关闭这个文件

f.close()

### 2.3**路径**

**1.linux**

![img](https://upload-images.jianshu.io/upload_images/6078268-93ae64d0a3cd03be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/520/format/webp)

**2.windows**

![img](https://upload-images.jianshu.io/upload_images/6078268-74071473609092c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

# 3.**文件的读写**

### 1.写数据(write)

使用write()可以完成向文件写入数据

demo:

f = open('test.txt','w')

f.write('hello world, i am here!')

f.close()

注意：

如果文件不存在那么创建，如果存在那么就先清空，然后写入数据

### 2.读数据(read)

使用read(num)可以从文件中读取数据，num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据

demo:

f = open('test.txt','r')

content = f.read(5)

print(content)

print("-"*30)

content = f.read()

print(content)

f.close()

注意：

·如果open是打开一个文件，那么可以不用写打开的模式，即只写open('test.txt')

如果使用读了多次，那么后面读取的数据是从上次读完后的位置开始的

![img](https://upload-images.jianshu.io/upload_images/6078268-f94ee1e9cf494931.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/543/format/webp)

### 3.读数据（readlines）

就像read没有参数时一样，readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素

f = open('test.txt','r')

content = f.readlines()

print(type(content))

i=1

fortempincontent:

print("%d:%s"%(i, temp))

i+=1

f.close()

## 4.读数据（readline）

f = open('test.txt','r')

content = f.readline()

print("1:%s"%content)

content = f.readline()

print("2:%s"%content)

f.close()

# 4.应用

## 1:制作文件的备份

**任务描述:**

输入文件的名字，然后程序自动完成对文件进行备份

**参考代码****：**

oldFileName = input("请输入要拷贝的文件名字:")

oldFile = open(oldFileName,'r')

\#如果打开文件

ifoldFile:

\#提取文件的后缀

fileFlagNum = oldFileName.rfind('.')

iffileFlagNum >0:

fileFlag = oldFileName[fileFlagNum:]

\#组织新的文件名字

newFileName = oldFileName[:fileFlagNum] +'[复件]'+ fileFlag

\#创建新文件

newFile = open(newFileName,'w')

\#把旧文件中的数据，一行一行的进行复制到新文件中

forlineContentinoldFile.readlines():

newFile.write(lineContent)

\#关闭文件

oldFile.close()

newFile.close()

## 2.**获取当前读写的位置**

在读写文件的过程中，如果想知道当前的位置，可以使用tell()来获取

从0开始到字符的个数

\#打开一个已经存在的文件

![img](https://upload-images.jianshu.io/upload_images/6078268-886240e68f1662fc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/705/format/webp)

## 3.**定位到某个位置**

如果在读写文件的过程中，需要从另外一个位置进行操作的话，可以使用seek()

seek(offset, from)有2个参数

1.offset:偏移量

2.from:方向

a)0:表示文件开头（python3）

b)1:表示当前位置（python2）

c)2:表示文件末尾（python2）

demo:把位置设置为：从文件开头，偏移5个字节

![img](https://upload-images.jianshu.io/upload_images/6078268-4cb7a5c708411cb4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/704/format/webp)

demo:把位置设置为：离文件末尾，3字节处

![img](https://upload-images.jianshu.io/upload_images/6078268-c75e3b248bebe20a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/548/format/webp)

## 4.**文件重命名**

os模块中的rename()可以完成对文件的重命名操作

rename(需要修改的文件名,新的文件名)

![img](https://upload-images.jianshu.io/upload_images/6078268-e12ff4bdfc48ad40.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/713/format/webp)

## 5.**删除文件**

os模块中的remove()可以完成对文件的删除操作

remove(待删除的文件名)

![img](https://upload-images.jianshu.io/upload_images/6078268-f39585db10e1d5e7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/675/format/webp)

© 著作权归作者所有

人生几何，何不Python当歌？学习Python之路，始于爬虫，限于文本，忠于数据分析。目前文本和爬虫刚刚入门，数据分析还未真正开始。 公众号：Python攻城狮 博客地址：https://ask.hellobi.com/blog/zhiji 掘金：https://juejin.im/user/5a30fe44f265da4324807186 Github：https://github.com/ReainL 大人不华，君子务实。 转载请保留原文链接及作者。

