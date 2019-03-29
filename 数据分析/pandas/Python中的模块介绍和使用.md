# Python中的模块介绍和使用

在Python中有一个概念叫做模块（module），这个和C语言中的头文件以及Java中的包很类似，比如在Python中要调用sqrt函数，必须用import关键字引入math这个模块，下面就来了解一下Python中的模块。

说的通俗点：模块就好比是工具包，要想使用这个工具包中的工具(就好比函数)，就需要导入这个模块

# **1.import**

**在Python中用关键字import来引入某个模块，比如要引用模块math，就可以在文件最开始的地方用import math来引入。**

形如:

importmodule1,mudule2...

当解释器遇到import语句，如果模块在当前的搜索路径就会被导入。

在调用math模块中的函数时，必须这样引用：

模块名.函数名

这种方式必须加上模块名调用，因为可能存在这样一种情况：在多个模块中含有相同名称的函数，此时如果只是通过函数名来调用，解释器无法知道到底要调用哪个函数。所以如果像上述这样引入模块的时候，调用函数必须加上模块名。

![img](https://upload-images.jianshu.io/upload_images/6078268-5a0063d7fe0c7522.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/661/format/webp)

有时候我们只需要用到模块中的某个函数，只需要引入该函数即可，此时可以用下面方法实现：

from模块名import函数名1,函数名2....

不仅可以引入函数，还可以引入一些全局变量、类等

**注意:**

通过这种方式引入的时候，调用函数时只能给出函数名，不能给出模块名，但是当两个模块中含有相同名称函数的时候，后面一次引入会覆盖前一次引入。也就是说假如模块A中有函数function( )，在模块B中也有函数function( )，如果引入A中的function在先、B中的function在后，那么当调用function函数的时候，是去执行模块B中的function函数。

**如果想一次性引入math中所有的东西，还可以通过from math import \*来实现**

# 2.**from…import**

Python的from语句让你从模块中导入一个指定的部分到当前命名空间中

语法如下：

**from modname import name1[, name2[, ... nameN]]**

例如，要导入模块fib的fibonacci函数，使用如下语句：

from fib import fibonacci

**注意**

·不会把整个fib模块导入到当前的命名空间中，它只会将fib里的fibonacci单个引入

# 3.**from … import \***

把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

from modname import *

**注意**

·这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。

# 4.**as**

![img](https://upload-images.jianshu.io/upload_images/6078268-88a3c497e65399cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/674/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-74b8f907826bb851.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/654/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-8dc87818dc188523.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/669/format/webp)

# 5.**定位模块**

当你导入一个模块，Python解析器对模块位置的搜索顺序是：

1.当前目录

2.如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。

3.如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/

4.模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。

# 6.模块制作

### 1.**定义自己的模块**

**在Python中，每个Python文件都可以作为一个模块，模块的名字就是文件的名字。**

比如有这样一个文件test.py，在test.py中定义了函数add

![img](https://upload-images.jianshu.io/upload_images/6078268-5d4bbf60ebcde580.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/339/format/webp)

#### 2.调用自己定义的模块

那么在其他文件中就可以先import test，然后通过test.add(a,b)来调用了，当然也可以通过from test import add来引入

main.py

![img](https://upload-images.jianshu.io/upload_images/6078268-d9e5ba6e35ce0e16.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/616/format/webp)

#### 3.测试模块

在实际开中，当一个开发人员编写完一个模块后，为了让模块能够在项目中达到想要的效果，这个开发人员会自行在py文件中添加一些测试信息，例如：

![img](https://upload-images.jianshu.io/upload_images/6078268-fc805817c8397acd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/671/format/webp)

如果此时，在其他py文件中引入了此文件的话，想想看，测试的那段代码是否也会执行呢！

![img](https://upload-images.jianshu.io/upload_images/6078268-5035c8de2ac29067.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/676/format/webp)

至此，可发现test.py中的测试代码，应该是单独执行test.py文件时才应该执行的，不应该是其他的文件中引用而执行

为了解决这个问题，python在执行一个文件时有个变量__name__

![img](https://upload-images.jianshu.io/upload_images/6078268-c63fbbd3942cf830.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/553/format/webp)

**总结：**

·可以根据__name__变量的结果能够判断出，是直接执行的python脚本还是被引入执行的，从而能够有选择性的执行测试代码

# 7.模块中的__all__

#### **1.没有__all__**

![img](https://upload-images.jianshu.io/upload_images/6078268-6e3356dea36c4ed4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-fff3ca85476791a2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-f72d00e9336f296a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

#### 2.**模块中有__all__**

![img](https://upload-images.jianshu.io/upload_images/6078268-80f49a3f224f017f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-9578740b4cc09c94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

# 8.**python中的包**

#### 1.**引入包**

**有2个模块功能有些联系**

![img](https://upload-images.jianshu.io/upload_images/6078268-4c85a2650b52855a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

所以将其放到同一个文件夹下

![img](https://upload-images.jianshu.io/upload_images/6078268-72a0c48ae0d45d11.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

使用import文件.模块 的方式导入

![img](https://upload-images.jianshu.io/upload_images/6078268-28a7a64d08b765b5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

使用from文件夹import模块 的方式导入

![img](https://upload-images.jianshu.io/upload_images/6078268-3bb6a89deb8fd875.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

在msg文件夹下创建__init__.py文件

![img](https://upload-images.jianshu.io/upload_images/6078268-f5bc0549013d5563.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

在__init__.py文件中写入

![img](https://upload-images.jianshu.io/upload_images/6078268-af7fcf7d2472b424.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

重新使用from文件夹import模块 的方式导入

![img](https://upload-images.jianshu.io/upload_images/6078268-c0485b4a5fd42214.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**总结：**

包将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建一个名字为__init__.py文件，那么这个文件夹就称之为包

有效避免模块名称冲突问题，让应用组织结构更加清晰

#### 2**__init__.py文件有什么用**

__init__.py控制着包的导入行为

可以在__init__内添加导入的功能 比如from ab import a

#### 3**__init__.py为空**

仅仅是把这个包导入，不会导入包中的模块

#### 4**__all__**

在__init__.py文件中，定义一个__all__变量，它控制着from包名import *时导入的模块

#### 5.**(了解)可以在__init__.py文件中编写内容**

可以在这个文件中编写语句，当导入时，这些语句就会被执行

__init__.py文件

![img](https://upload-images.jianshu.io/upload_images/6078268-f83b8f25d5872f71.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-b12e0d7db92ba950.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

#### 6.扩展：嵌套的包

假定我们的包的例子有如下的目录结构：

![img](https://upload-images.jianshu.io/upload_images/6078268-cb326ac823638162.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/551/format/webp)

Phone是最顶层的包，Voicedta等是它的子包。 我们可以这样导入子包：

![img](https://upload-images.jianshu.io/upload_images/6078268-3c1de5b196cbc319.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/584/format/webp)

你也可使用from-import实现不同需求的导入

第一种方法是只导入顶层的子包，然后使用属性/点操作符向下引用子包树：

![img](https://upload-images.jianshu.io/upload_images/6078268-f3e4e77ce8634640.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/487/format/webp)

此外，我们可以还引用更多的子包：

![img](https://upload-images.jianshu.io/upload_images/6078268-1290df5d2a4132b6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/465/format/webp)

事实上，你可以一直沿子包的树状结构导入：

![img](https://upload-images.jianshu.io/upload_images/6078268-f9f1b1c946f146db.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/409/format/webp)

在我们上边的目录结构中，我们可以发现很多的__init__.py文件。这些是初始化模块，from-import语句导入子包时需要用到它。 如果没有用到，他们可以是空文件。

包同样支持from-import all语句：

![img](https://upload-images.jianshu.io/upload_images/6078268-5eee4102dbfbe364.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/434/format/webp)

然而，这样的语句会导入哪些文件取决于操作系统的文件系统。所以我们在__init__.py中加入__all__变量。该变量包含执行这样的语句时应该导入的模块的名字。它由一个模块名字符串列表组成。

![img](https://upload-images.jianshu.io/upload_images/6078268-ad537f5d46eda8c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/196/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-338ae4a4ae33fbf4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/337/format/webp)

总结：

![img](https://upload-images.jianshu.io/upload_images/6078268-dcdf4a6bb94d1c5f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/446/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-22007b5867d3994d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

# 9.模块发布

#### 1.mymodule目录结构体如下：

![img](https://upload-images.jianshu.io/upload_images/6078268-8f158b4c25e4041e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/488/format/webp)

#### 2.编辑setup.py文件��

py_modules需指明所需包含的py文件

![img](https://upload-images.jianshu.io/upload_images/6078268-38acaf44135851c1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/614/format/webp)

#### **3.构建模块**

**python setup.py build**

![img](https://upload-images.jianshu.io/upload_images/6078268-5d89ec857482e187.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/507/format/webp)

#### 4.生成发布压缩包

�python setup.py sdist

打包后,生成最终发布压缩包yongGe-1.0.tar.gz ,目录结构

![img](https://upload-images.jianshu.io/upload_images/6078268-7547285c734613ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/438/format/webp)

# 10.模块的安装使用

#### 1.**安装的方式**

1.找到模块的压缩包

2.解压

3.进入文件夹

4.执行命令python setup.py install

注意：

·如果在install的时候，执行目录安装，可以使用python setup.py install --prefix=安装路径

#### 2.**模块的引入**

在程序中，使用from import即可完成对安装的模块使用

from模块名import模块名或者*

© 著作权归作者所有
