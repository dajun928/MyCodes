# Linux命令-系统管理

## 1.**查看当前日历：cal**

cal命令用于查看当前日历，-y显示整年日历：

## **2.显示或设置时间：date**

设置时间格式（需要管理员权限）：

date [MMDDhhmm[[CC]YY][.ss]] +format

CC为年前两位yy为年的后两位，前两位的mm为月，后两位的mm为分钟，dd为天，hh为小时，ss为秒。如：date 010203042016.55。

显示时间格式（date '+%y,%m,%d,%H,%M,%S'）：

![img](https://upload-images.jianshu.io/upload_images/6078268-3c4fad841573635c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-02584185bdaf4475.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 3.**查看进程信息：ps**

进程是一个具有一定独立功能的程序，它是操作系统动态执行的基本单元。

ps命令可以查看进程的详细状况，常用选项(选项可以不加“-”)如下：

![img](https://upload-images.jianshu.io/upload_images/6078268-5a79f15927f3f67d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## **4.动态显示进程：top**

top命令用来动态显示运行中的进程。top命令能够在运行后，在指定的时间间隔更新显示信息。可以在使用top命令时加上-d来指定显示信息更新的时间间隔。

在top命令执行后，可以按下按键得到对显示的结果进行排序：

![img](https://upload-images.jianshu.io/upload_images/6078268-d35dae34dede2315.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 5.**终止进程：kill**

kill命令指定进程号的进程，需要配合ps使用。

使用格式：

kill [-signal] pid

信号值从0到15，其中9为绝对终止，可以处理一般信号无法终止的进程。

kill 9133：9133为应用程序所对应的进程号

![img](https://upload-images.jianshu.io/upload_images/6078268-9f0bd31d97a853ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-6e2107fb487ad840.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

有些进程不能直接杀死，这时候我们需要加一个参数“ -9 ”，“ -9 ”代表强制结束。

## 6.关机重启：reboot、shutdown、init

![img](https://upload-images.jianshu.io/upload_images/6078268-152b231ecd1039c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 7.**检测磁盘空间：df**

df命令用于检测文件系统的磁盘空间占用和空余情况，可以显示所有文件系统对节点和磁盘块的使用情况。

![img](https://upload-images.jianshu.io/upload_images/6078268-be59fdc3974deb8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-8184bfe6e799b7e2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 8.**检测目录所占磁盘空间：du**

du命令用于统计目录或文件所占磁盘空间的大小，该命令的执行结果与df类似，du更侧重于磁盘的使用状况。

du命令的使用格式如下：du [选项]目录或文件名

![img](https://upload-images.jianshu.io/upload_images/6078268-eff543bc4a221ce1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-06660dd8fefb3bc4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/530/format/webp)

## **9.查看或配置网卡信息：ifconfig**

如果，我们只是敲：ifconfig，它会显示所有网卡的信息：

![img](https://upload-images.jianshu.io/upload_images/6078268-08e5722147959f21.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-c7fe9c8cb4ab35cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 10.测试远程主机连通性：ping

![img](https://upload-images.jianshu.io/upload_images/6078268-23734f7151478593.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 11.**apt-get**

在Ubuntu下，apt-get近乎是最常用的shell命令之一了，因为他是Ubuntu通过新立得安装软件的常用工具命令。

本文列举了常用的APT命令参数：

apt-cache search package搜索软件包

apt-cache show package获取包的相关信息，如说明、大小、版本等

sudo apt-get install package安装包

sudo apt-get install package --reinstall重新安装包

sudo apt-get -f install修复安装

sudo apt-get remove package删除包

sudo apt-get remove package --purge删除包，包括配置文件等

sudo apt-get update更新源

sudo apt-get upgrade更新已安装的包

sudo apt-get dist-upgrade升级系统

apt-cache depends package了解使用该包依赖那些包

apt-cache rdepends package查看该包被哪些包依赖

sudo apt-get build-dep package安装相关的编译环境

apt-get source package下载该包的源代码

sudo apt-get clean && sudo apt-get autoclean清理无用的包

sudo apt-get check检查是否有损坏的依赖

# 2.vim编辑器

## **1.vi简介**

vi是“Visual interface”的简称，它在Linux上的地位就仿佛Edit程序在DOS上一样。它可以执行输出、删除、查找、替换、块操作等众多文本操作，而且用户可以根据自己的需要对其进行定制。Vi不是一个排版程序，它不象Word或WPS那样可以对字体、格式、段落等其他属性进行编排，它只是一个文本编辑程序。vi没有菜单，只有命令，且命令繁多。

Vi有三种基本工作模式：

+命令模式

+文本输入模式

+末行模式。

![img](https://upload-images.jianshu.io/upload_images/6078268-643d303759e7d424.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 2.安装

![img](https://upload-images.jianshu.io/upload_images/6078268-875b745d241f9e07.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 3.命令行模式

任何时候，不管用户处于何种模式，只要按一下ESC键，即可使Vi进入命令模式；我们在shell环境(提示符为$)下输入启动Vi命令，进入编辑器时，也是处于该模式下。在该模式下，用户可以输入各种合法的Vi命令，用于管理自己的文档。此时从键盘上输入的任何字符都被当做编辑命令来解释，若输入的字符是合法的Vi命令，则Vi在接受用户命令之后完成相应的动作。但需注意的是，所输入的命令并不在屏幕上显示出来。若输入的字符不是Vi的合法命令，Vi会响铃报警。

## 4.**文本输入模式**

在命令模式下输入插入命令i、附加命令a、打开命令o、修改命令c、取代命令r或替换命令s都可以进入文本输入模式。在该模式下，用户输入的任何字符都被Vi当做文件内容保存起来，并将其显示在屏幕上。在文本输入过程中，若想回到命令模式下，按键ESC即可。

## 5.**末行模式**

末行模式也称ex转义模式。在命令模式下，用户按“:”键即可进入末行模式下，此时Vi会在显示窗口的最后一行(通常也是屏幕的最后一行)显示一个“:”作为末行模式的提示符，等待用户输入命令。多数文件管理命令都是在此模式下执行的(如把编辑缓冲区的内容写到文件中等)。末行命令执行完后，Vi自动回到命令模式。例如：

:sp newfile

则分出一个窗口编辑newfile文件。如果要从命令模式转换到编辑模式，可以键入命令a或者i；如果需要从文本模式返回，则按Esc键即可。在命令模式下输入“:”即可切换到末行模式，然后输入命令。

# 3.vim基础操作

vim是从vi发展出来的一个文本编辑器 。代码补完、编译及错误跳转等方便编程的功能特别丰富

进入插入模式:

i:插入光标前一个字符

I:插入行首

a:插入光标后一个字符

A:插入行末

o:向下新开一行,插入行首

O:向上新开一行,插入行首

进入命令模式:

ESC:从插入模式或末行模式进入命令模式

移动光标:

h:左移

j:下移

k:上移

l:右移

M:光标移动到中间行

L:光标移动到屏幕最后一行行首

G:移动到指定行,行号-G

w:向后一次移动一个字

b:向前一次移动一个字

{:按段移动,上移

}:按段移动,下移

Ctr-d:向下翻半屏

Ctr-u:向上翻半屏

Ctr-f:向下翻一屏

Ctr-b:向上翻一屏

gg:光标移动文件开头

G:光标移动到文件末尾

删除命令:

x:删除光标后一个字符,相当于Del

X:删除光标前一个字符,相当于Backspace

dd:删除光标所在行,n dd删除指定的行数D:删除光标后本行所有内容,包含光标所在字符

d0:删除光标前本行所有内容,不包含光标所在字符

dw:删除光标开始位置的字,包含光标所在字符

撤销命令:

u:一步一步撤销

Ctr-r:反撤销

重复命令:

.:重复上一次操作的命令

文本行移动:

\>>:文本行右移

<<:文本行左移

复制粘贴:

yy:复制当前行,n yy复制n行

p:在光标所在位置向下新开辟一行,粘贴

可视模式:

v:按字符移动,选中文本

V:按行移动,选中文本可视模式可以配合d, y, >>, <<实现对文本块的删除,复制,左右移动

替换操作:

r:替换当前字符

R:替换当前行光标后的字符

查找命令:

/查找

n:下一个

N：上一个

替换命令：

把abc全部替换成123

末行模式下，将光标所在行的abc替换成123

:%s/abc/123/g

末行模式下，将第一行至第10行之间的abc替换成123

:1, 10s/abc/123/g

vim里执行shell下命令:

末行模式里输入!,后面跟命令

放大缩写

ctrl -缩小

ctrl shift +放大

ubuntu vim tab 4个空格

编辑文件

sudo vim /etc/vim/vimrc

在最后加上

set ts=4

set expandtab

set autoindent

# 4.安装ssh

![img](https://upload-images.jianshu.io/upload_images/6078268-1d0ea78103bfda61.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img]()

![img](https://upload-images.jianshu.io/upload_images/6078268-b9594cd0f307c5cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

******A机器安装ssh******

1、更新apt-get

sudo apt-get update

2、使用apt-get从网络上下载并安装sshserver

sudo apt-get install openssh-server

3、查看ssh进程，如果能查到说明安装成功并启动了

ps -e|grep ssh

******B机器远程登录******

ssh用户名@IP

使用ssh访问，如访问出现错误。可查看是否有该文件 ～/.ssh/known_ssh尝试删除该文件解决。

# 5.**使用ssh连接服务器**

SSH告知用户，这个主机不能识别，这时键入"yes"，SSH就会将相关信息，写入" ~/.ssh/know_hosts"中，再次访问，就不会有这些信息了。然后输入完口令,就可以登录到主机了。

## 1.scp

使用crt在windows和linux之间传输文件:alt+p

![img](https://upload-images.jianshu.io/upload_images/6078268-52b5c9b011b27eff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 2.远程拷贝文件,scp -r的常用方法：

1.使用该命令的前提条件要求目标主机已经成功安装openssh-server

如没有安装使用sudo apt-get install openssh-server来安装

2.使用格式：

scp -r目标用户名@目标主机IP地址：/目标文件的绝对路径/保存到本机的绝对/相对路径

举例：

scp -r laowang@192.168.1.100:/home/laowang/QQ_dir/ ./mytest/lisi

在后续会提示输入“yes”此时，只能输“yes”而不能简单输入“Y”

拷贝单个文件可以不加-r参数，拷贝目录必须要加。

本地文件复制到远程：

scp FileName RemoteUserName@RemoteHostIp:RemoteFile

scp FileName RemoteHostIp:RemoteFolder

scp FileName RemoteHostIp:RemoteFile

远程文件复制到本地：

scp RemoteUserName@RemoteHostIp:RemoteFile FileName

scp RemoteHostIp:RemoteFolder FileName

scp RemoteHostIp:RemoteFile FileName

远程目录复制到本地：

scp -r RemoteUserName@RemoteHostIp:RemoteFolder FolderName

scp -r RemoteHostIp:RemoteFolder FolderName

## 3.强行踢除其他登录用户

![img](https://upload-images.jianshu.io/upload_images/6078268-c2113ac900b288db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/626/format/webp)

注意：

只有root用户才可以踢人，如果同时有两个人用root用户登录，其中任何一个人可以踢掉另一个，任何用户都可以踢掉自己。如： 

![img](https://upload-images.jianshu.io/upload_images/6078268-178d81e65518d85a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/422/format/webp)

© 著作权归作者所有
