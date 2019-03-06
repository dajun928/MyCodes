# Linux命令-文件管理

# **1.目录方面命令：ls**

## 1.**查看文件信息：ls**

## 

Linux文件或者目录名称最长可以有265个字符，“.”代表当前目录，“..”代表上一级目录，以“.”开头的文件为隐藏文件，需要用-a参数才能显示。

ls显示指定目录的文件和目录

ls -a列出目录下的所有文件，包括以.开头的隐藏文件

![img](https://upload-images.jianshu.io/upload_images/6078268-801651b24cbce86b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

ls -l显示指定目录的详细列表

ls -R列出所有子目录下的文件

ls -F在每个文件名后附上一个字符以说明该文件的类型

/表示目录文件

*表示执行文件

|管道文件

![img](https://upload-images.jianshu.io/upload_images/6078268-fcf6c69f4ba0adda.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 2.显示方面命令

**1.cd切换目录**

![img](https://upload-images.jianshu.io/upload_images/6078268-8b49ab90d988574c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

注意：

如果路径是从根路径开始的，则路径的前面需要加上“ / ”，如“ /mnt ”，通常进入某个目录里的文件夹，前面不用加“ / ”。

**2.clear清屏**

clear作用为清除终端上的显示(类似于DOS的cls清屏功能)，也可使用快捷键：Ctrl + l ( “l”为字母)。

**3.pwd显示当前目录的绝对路径**

**4.mkdir创建目录**

mkdir a b c d在当前目录创建多个目录

mkdir -m 777 aa bb在当前目录创建aa,bb目录，且权限为所有权限。

mkdir -p a/b/c/d/e创建多级子目录

mkdir dir{1,2,3,4,5} ==== mkdir dir1 dir2 dir3 dir4 dir5

![img](https://upload-images.jianshu.io/upload_images/6078268-6bb7d66a96f2e40e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**5.删除目录：rmdir**

可使用rmdir命令删除一个目录。必须离开目录，并且目录必须为空目录，不然提示删除失败。

-p递归删除

**6.删除文件：rm**

可通过rm删除文件或目录。使用rm命令要小心，因为文件删除后不能恢复。为了防止文件误删，可以在rm后使用-i参数以逐个确认要删除的文件。

常用参数及含义如下表所示：

![img](https://upload-images.jianshu.io/upload_images/6078268-239cf703b475dc82.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**7.分屏显示：more**

查看内容时，在信息过长无法在一屏上显示时，会出现快速滚屏，使得用户无法看清文件的内容，此时可以使用more命令，每次只显示一页，按下空格键可以显示下一页，按下q键退出显示，按下h键可以获取帮助。

ctrl+b返回上一屏

ctrl+f下一屏

8.**查看或者合并文件内容：cat**

cat显示小文件的内容，以头到尾

tac显示小文件的内容，以尾到头

-n:显示行号

方法一:

cat /etc/group

方法二:

groupmod +三次tab键

**9.管道 |：**一个命令的输出可以通过管道做为另一个命令的输入。

管道我们可以理解现实生活中的管子，管子的一头塞东西进去，另一头取出来，这里“ | ”的左右分为两端，左端塞东西(写)，右端取东西(读)。

## 3.查找方面命令

**1.文本搜索：grep**

Linux系统中grep命令是一种强大的文本搜索工具，grep允许对文本文件进行模式查找。如果找到匹配模式，grep打印包含模式的所有行。

grep一般格式为：

grep [-选项] ‘搜索内容串’文件名

在grep命令中输入字符串参数时，最好引号或双引号括起来。例如：grep‘a ’1.txt。

常用选项说明：

![img](https://upload-images.jianshu.io/upload_images/6078268-72a4f8512eea6c92.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

grep搜索内容串可以是正则表达式。

正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

grep常用正则表达式：

![img](https://upload-images.jianshu.io/upload_images/6078268-2f7d7913e89a5918.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**2.find**

find命令功能非常强大，通常用来在特定的目录下搜索符合条件的文件，也可以用来搜索特定用户属主的文件。

![img](https://upload-images.jianshu.io/upload_images/6078268-23d1d615c1f27309.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 4.文件方面命令

**1.拷贝文件：cp**

cp命令的功能是将给出的文件或目录复制到另一个文件或目录中，相当于DOS下的copy命令。

常用选项说明：

![img](https://upload-images.jianshu.io/upload_images/6078268-c03b9214216d8770.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**2.移动文件：mv**

用户可以使用mv命令来移动文件或目录，也可以给文件或目录重命名。

常用选项说明：

![img](https://upload-images.jianshu.io/upload_images/6078268-754c7ac9f16db6ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img]()

![img]()

**3.归档管理：tar**

计算机中的数据经常需要备份，tar是Unix/Linux中最常用的备份工具，此命令可以把一系列文件归档到一个大文件中，也可以把档案文件解开以恢复数据。

tar使用格式tar [参数]打包文件名 文件

tar命令很特殊，其参数前面可以使用“-”，也可以不使用。

常用参数：

![img](https://upload-images.jianshu.io/upload_images/6078268-45a3661dd83daa53.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

注意：除了f需要放在参数的最后，其它参数的顺序任意。

**4.文件压缩解压：gzip**

tar与gzip命令结合使用实现文件打包、压缩。tar只负责打包文件，但不压缩，用gzip压缩tar打包后的文件，其扩展名一般用xxxx.tar.gz。

gzip使用格式如下：

gzip  [选项]被压缩文件

![img](https://upload-images.jianshu.io/upload_images/6078268-6faa830618bc9275.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-3145d02f625ccea4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

tar这个命令并没有压缩的功能，它只是一个打包的命令，但是在tar命令中增加一个选项(-z)可以调用gzip实现了一个压缩的功能，实行一个先打包后压缩的过程。

压缩用法：tar cvzf压缩包包名 文件1文件2 ...

-z：指定压缩包的格式为：file.tar.gz

![img](https://upload-images.jianshu.io/upload_images/6078268-acda930d01c7a390.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

解压用法：tar zxvf 压缩包包名

-z:指定压缩包的格式为：file.tar.gz

解压到指定目录：-C （大写字母“C”）

![img](https://upload-images.jianshu.io/upload_images/6078268-188a6a9480e8d164.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**5.文件压缩解压：bzip2**

tar与bzip2命令结合使用实现文件打包、压缩(用法和gzip一样)。

tar只负责打包文件，但不压缩，用bzip2压缩tar打包后的文件，其扩展名一般用xxxx.tar.gz2。

在tar命令中增加一个选项(-j)可以调用bzip2实现了一个压缩的功能，实行一个先打包后压缩的过程。

压缩用法：tar -jcvf 压缩包包名 文件...(tar jcvf bk.tar.bz2 *.c)

解压用法：tar -jxvf 压缩包包名 (tar jxvf bk.tar.bz2)

**6.文件压缩解压：zip、unzip**

通过zip压缩文件的目标文件不需要指定扩展名，默认扩展名为zip。

压缩文件：zip [-r] 目标文件(没有扩展名) 源文件

解压文件：unzip -d 解压后目录文件 压缩文件

![img](https://upload-images.jianshu.io/upload_images/6078268-b46fc22a7d29d45e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-59a191dd49e53885.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 5.权限方面命令

**1.查看命令位置：which**

![img](https://upload-images.jianshu.io/upload_images/6078268-23074bfaaf32fdda.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**2.查看当前用户：whoami**

whoami该命令用户查看当前系统当前账号的用户名。可通过cat /etc/passwd查看系统用户信息。

由于系统管理员通常需要使用多种身份登录系统，例如通常使用普通用户登录系统，然后再以su命令切换到root身份对传统进行管理。这时候就可以使用whoami来查看当前用户的身份。

**3.查看登录用户：who**

who命令用于查看当前所有登录系统的用户信息。

常用选项：

![img](https://upload-images.jianshu.io/upload_images/6078268-681fa05b2c5eaf3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**4.退出登录账户：exit**

如果是图形界面，退出当前终端；

如果是使用ssh远程登录，退出登陆账户；

如果是切换后的登陆用户，退出则返回上一个登陆账号。

**5.添加用户账号：useradd**

在Unix/Linux中添加用户账号可以使用adduser或useradd命令，因为adduser命令是指向useradd命令的一个链接，因此，这两个命令的使用格式完全一样。

useradd命令的使用格式如下：useradd [参数]新建用户账号

![img](https://upload-images.jianshu.io/upload_images/6078268-f8199bcd3393637c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

Linux每个用户都要有一个主目录，主目录就是第一次登陆系统，用户的默认当前目录(/home/用户)；

·每一个用户必须有一个主目录，所以用useradd创建用户的时候，一定给用户指定一个主目录；

·用户的主目录一般要放到根目录的home目录下，用户的主目录和用户名是相同的；

·如果创建用户的时候，不指定组名，那么系统会自动创建一个和用户名一样的组名。

能跨分区，不占用i节点。

![img](https://upload-images.jianshu.io/upload_images/6078268-29da082180509ef1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-fd1c5f248003bfe8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 6.用户方面命令

**1.设置用户密码：passwd**

在Unix/Linux中，超级用户可以使用passwd命令为普通用户设置或修改用户口令。用户也可以直接使用该命令来修改自己的口令，而无需在命令后面使用用户名。

**2.删除用户：userdel**

![img](https://upload-images.jianshu.io/upload_images/6078268-9497b79fa6078a86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**3.切换用户：su**

可以通过su命令切换用户，su后面可以加“-”。su和su –命令不同之处在于，su -切换到对应的用户时会将当前的工作目录自动转换到切换后的用户主目录。

注意：如果是ubuntu平台，需要在命令前加“sudo”，如果在某些操作需要管理员才能操作，ubuntu无需切换到root用户即可操作，只需加“sudo”即可。sudo是ubuntu平台下允许系统管理员让普通用户执行一些或者全部的root命令的一个工具，减少了root用户的登陆和管理时间，提高了安全性。

![img](https://upload-images.jianshu.io/upload_images/6078268-f4e6fc9a52583e31.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

Ubuntu下切换到root的简单命令:

![img](https://upload-images.jianshu.io/upload_images/6078268-367671139ff51302.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**4.添加、删除组账号：groupadd、groupdel**

groupadd新建组账号groupdel组账号cat /etc/group查看用户组

**5.修改用户所在组：usermod**

使用方法：usermod -g用户组 用户名

![img](https://upload-images.jianshu.io/upload_images/6078268-1f860ec7efbd28a7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-e7bf5a4ec68d919f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**6.查看用户在哪些组**

![img](https://upload-images.jianshu.io/upload_images/6078268-f77be2d06ddbb528.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**7.为创建的普通用户添加sudo权限**

新创建的用户，默认不能sudo，需要进行一下操作

sudo usermod -a -G adm用户名

sudo usermod -a -G sudo用户名

**8.usermod -g与-G的区别**

-g用来制定这个用户默认的用户组

-G一般配合'-a'来完成向其它组添加

**9.修改文件权限：chmod**

chmod修改文件权限有两种使用格式：字母法与数字法。

字母法：chmod u/g/o/a +/-/= rwx文件

![img](https://upload-images.jianshu.io/upload_images/6078268-6e2224cc977e1222.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-c65a0aa85e6ba5a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-731fdaefce57180a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-3aa665ca36593535.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-55ec89ae7eed60ed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-01056e26d23a2725.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

注意：如果想递归所有目录加上相同权限，需要加上参数“ -R ”。 如：chmod 777 test/ -R递归test目录下所有文件加777权限

**10.修改文件所有者：chown**

![img](https://upload-images.jianshu.io/upload_images/6078268-8f717295729731d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**11.修改文件所属组：chgrp**

![img](https://upload-images.jianshu.io/upload_images/6078268-2f024ee521fc96d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

© 著作权归作者所有