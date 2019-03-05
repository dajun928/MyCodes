# Python高级编程-装饰器

# 1.**装饰器的理解**

装饰器是程序开发中经常会用到的一个功能，用好了装饰器，开发效率如虎添翼，所以这也是Python面试中必问的问题，但对于好多初次接触这个知识的人来讲，这个功能有点绕，自学时直接绕过去了，然后面试问到了就挂了，因为装饰器是程序开发的基础知识，这个都不会，别跟人家说你会Python,看了下面的文章，保证你学会装饰器。

装饰器，功能就是在运行原来功能基础上，加上一些其它功能，比如权限的验证，比如日志的记录等等。不修改原来的代码，进行功能的扩展。

比如java中的动态代理，python的注解装饰器

其实python的装饰器，是修改了代码。

# 2.**多个装饰器**

![img](https://upload-images.jianshu.io/upload_images/6078268-3f5a9d3634d6d5cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/649/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-be7f3d1676e9c933.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/625/format/webp)

# 3.**装饰器(decorator)功能**

1.引入日志

2.函数执行时间统计

3.执行函数前预备处理

4.执行函数后清理功能

5.权限校验等场景

6.缓存

# 4.装饰器示例

#### **1.无参数的函数**

![img](https://upload-images.jianshu.io/upload_images/6078268-916005bacf7b7944.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/722/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-477002844817a398.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/471/format/webp)

上面代码理解装饰器执行行为可理解成

foo = timefun(foo)

foo先作为参数赋值给func后,foo接收指向timefun返回的wrappedfunc

foo()

调用foo(),即等价调用wrappedfunc()

内部函数wrappedfunc被引用，所以外部函数的func变量(自由变量)并没有释放

func里保存的是原foo函数对象

#### **2:被装饰的函数有参数**

![img](https://upload-images.jianshu.io/upload_images/6078268-8bd85c27a3027172.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/683/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-e9128faf27ceb0be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/523/format/webp)

#### 3:被装饰的函数有不定长参数

![img](https://upload-images.jianshu.io/upload_images/6078268-e14ecd94a0ce9915.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/710/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-4305df4a17c85ff5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/566/format/webp)

#### 4:装饰器中的return

![img](https://upload-images.jianshu.io/upload_images/6078268-c2f2c4218ae0e926.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/661/format/webp)

此时timefun无返回值，运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-25ad179b0e00792a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/539/format/webp)

如果修改装饰器为return func()，则运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-074da5197635ec72.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/739/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-26f059c19ae8f788.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/538/format/webp)

**总结：**

·一般情况下为了让装饰器更通用，可以有return

#### 5.装饰器带参数,在原有装饰器的基础上，设置外部变量

![img](https://upload-images.jianshu.io/upload_images/6078268-2c254692e94e9534.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/765/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-768895725654089d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/546/format/webp)

#### **6：类装饰器（扩展）**

装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，然后返回一个callable对象。在Python中一般callable对象都是函数，但也有例外。只要某个对象重写了__call__()方法，那么这个对象就是callable的。

![img](https://upload-images.jianshu.io/upload_images/6078268-db5ad754c5db2522.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/604/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-ec02c5720e913665.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/445/format/webp)

\#说明：

\#1.当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象

\#并且会把test这个函数名当做参数传递到__init__方法中

\#即在__init__方法中的func变量指向了test函数体

\#

\#2. test函数相当于指向了用Test创建出来的实例对象

\#

\#3.当在使用test()进行调用时，就相当于让这个对象()，因此会调用这个对象的__call__方法

\#

\#4.为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法中就需要一个实例属性来保存这个函数体的引用

\#所以才有了self.__func = func这句代码，从而在调用__call__方法中能够调用到test之前的函数体

@Test

deftest():

print("----test---")

test()

showpy()#如果把这句话注释，重新运行程序，依然会看到"--初始化--"

© 著作权归作者所有
