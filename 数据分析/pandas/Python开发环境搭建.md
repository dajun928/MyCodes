# Python开发环境搭建

# 1.下载及安装

- ## 下载

  - [官方网站](https://link.jianshu.com/?t=http://www.python.org/)
  - [ftp官方下载地址](https://link.jianshu.com/?t=http://www.python.org/ftp/python)：在官方ftp下载地址中，可以选择下载任意一个需要的版本。

![img](https://upload-images.jianshu.io/upload_images/6078268-2c898567393554c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/857/format/webp)

- ## 安装过程

  - 双击安装包，出现如下的开始安装界面，选择自定义安装选项

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-5cb4e45fa65eff9d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/832/format/webp)

- 选项设置，默认全部勾选即可

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-c1dd82abb3b5174b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/832/format/webp)

- 高级配置选项，如图勾选即可

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-d0d7976287dd4215.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/832/format/webp)

- 安装过程中

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-d317a0e47d910130.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/832/format/webp)

- 安装完成，最后的结束界面中，一定点击disable path length limit，禁用系统的Path长度自动限制，能给我们避免很多的麻烦。

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-0ca1d2c1ff4df82b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/832/format/webp)

- 安装完成。
  开始菜单中，找到python3.6，然后点击IDLE就可以打开一个python 的界面工具啦。

# 2.一台PC安装多个python版本

- ## 安装Python2.7.9版本

现在python3是趋势，很多公司已经逐渐使用python3，但是对于爬虫来说，我们现在仍需用2.7，所以现在我们安装Python2.7.9版本

- [ftp官方下载地址](https://link.jianshu.com/?t=http://www.python.org/ftp/python)：在官方ftp下载地址中，可以选择下载Python2.7.9版本。双击安装包，出现安装界面如下

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-df574d9a3039f796.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/587/format/webp)

- 选择安装路径，如果不需要选择的话，安装到默认路径即可

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-25fe7f865d5c591c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/587/format/webp)

- 安装选项，默认即可，

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-bc1a7f74115e4962.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/587/format/webp)

- 安装完成，出现如下界面

![img](https://upload-images.jianshu.io/upload_images/6078268-d7d89691db5bc2c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/587/format/webp)

安装完成后，此时就会出现一个问题，我们已经在PC上同时安装了python2和python3的版本，如果此时打开命令行执行python命令，PC会直接使用默认安装的python进行处理，此时让python2和python3都能正常工作而不互相产生影响，成为我们急需要解决的问题。

# 3.python2和python3版本共存的配置

- 进入python2的安装路径如下

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-370119d1330066ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/898/format/webp)

- 修改python.exe，重命名为python2.exe

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-0230ec074ec27e89.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/919/format/webp)

- 进入python3的安装路径

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-8ff3b8ebd30c69b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/804/format/webp)

- 重命名文件python.exe为python3.exe，pythonw.exe为pythonw3.exe

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-b95bef8165616eed.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/864/format/webp)

- 配置环境变量，将python2和python3的路径都配置到path环境变量下

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-225b3ea2c2b3f12a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/678/format/webp)

- 此时，我们打开系统的命令行窗口，输入命令python2进入python2开发环境，输入命名python3进入python3开发环境

> 
>
> ![img](https://upload-images.jianshu.io/upload_images/6078268-a05a914a0b183d3f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/934/format/webp)

# 4. pip安装模块时执行的命令

正常情况下，我们还需要使用python的pip命令进行第三方模块的安装和配置，此时如果直接执行Pip会出现错误。

> 常规安装命令语法如下
>
> ```
> pip install 模块名称
> ```
>
> 但是，我们在PC上安装了两个版本的python并且修改了可执行文件python.exe的名称，所以直接执行pip会出现错误。

# 5.给python安装第三方模块

- 给python2安装第三方模块
  - 打开命令行工具，执行如下的命令进行安装python2需要的模块

```
python2 -m pip install 模块名称
```

- 给python3安装第三方模块
  - 打开命令行工具，执行如下的命令进行安装python3需要的模块

```
python3 -m pip install 模块名称
```

# 6.查看pip版本

![img](https://upload-images.jianshu.io/upload_images/6078268-4b7a628b247fd63e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/831/format/webp)

执行指定版本的python中的pip命令

© 著作权归作者所有
