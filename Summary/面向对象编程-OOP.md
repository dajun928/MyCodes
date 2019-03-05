# 面向对象编程-OOP

# **1.面向对象编程介绍**

面向对象(object-oriented ;简称: OO)至今还没有统一的概念 我这里把它定义为:按人们 认识客观世界的系统思维方式,采用基于对象(实体)的概念建立模型,模拟客观世界分析、设 计、实现软件的办法。

面向对象编程(Object Oriented Programming-OOP)是一种解决软件复用的设计和编程方法。 这种方法把软件系统中相近相似的操作逻辑和操作 应用数据、状态,以类的型式描述出来,以对象实例的形式在软件系统中复用,以达到提高软件开发效率的作用。

## **1.面向对象的理解：**

面向对象是一种设计思想

1.符合人们的思考习惯

2.把执行者变成指挥者

3.简化功能，把复杂的事情简单化

面向对象有三大特征：

1.封装

2.继承

3.多态

## 2.**类和对象**

面向对象编程的2个非常重要的概念：类和对象

对象是面向对象编程的核心，在使用对象的过程中，为了将具有共同特征和行为的一组对象抽象定义，提出了另外一个新的概念——类

类就相当于制造飞机时的图纸，用它来进行创建的飞机就相当于对象

类是对事务的描述，是抽象的。

对象是类的具体体现。

## 3.类

人以类聚物以群分。

具有相似内部状态和运动规律的实体的集合(或统称为抽象)。

具有相同属性和行为事物的统称

类是抽象的,在使用的时候通常会找到这个类的一个具体的存在,使用这个具体的存在。一个类可以找到多个对象

## 4.**对象**

某一个具体事物的存在,在现实世界中可以是看得见摸得着的。

可以是直接使用的

## 5.类和对象之间的关系

类就是创建对象的模板

## 6.**类的构成**

## 类(Class)由3个部分构成

·类的名称:类名

·类的属性:一组数据成员变量

·类的方法:允许对进行操作的方法(行为)成员方法

**举例：**

1）人类设计,只关心3样东西:

·事物名称(类名):人(Person)

·属性:身高(height)、年龄(age)

·方法(行为/功能):跑(run)、打架(fight)

2）狗类的设计

·类名:狗(Dog)

·属性:品种 、毛色、性别、名字、 腿儿的数量

·方法(行为/功能):叫 、跑、咬人、吃、摇尾巴

![img](https://upload-images.jianshu.io/upload_images/6078268-0b33705c48de069a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/142/format/webp)

## 7.类的抽象

如何把日常生活中的事物抽象成程序中的类?

拥有相同(或者类似)属性和行为的对象都可以抽像出一个类

# 2.定义类

定义一个类，格式如下：

![img](https://upload-images.jianshu.io/upload_images/6078268-1990e4a205b5c9a5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/640/format/webp)

demo：定义一个Car类

![img](https://upload-images.jianshu.io/upload_images/6078268-a16d165d120674e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/854/format/webp)

**说明：**

·定义类时有2种：新式类和经典类，上面的Car为经典类，如果是Car(object)则为新式类

·类名的命名规则按照"大驼峰"

## 1.**创建对象**

通过上一节课程，定义了一个Car类；就好比有车一个张图纸，那么接下来就应该把图纸交给生成工人们去生成了

python中，可以根据已经定义的类去创建出一个个对象

创建对象的格式为:

对象名=类名()

创建对象demo:

\#定义类

classCar:

\#移动

defmove(self):

print('车在奔跑...')

\#鸣笛

deftoot(self):

print("车在鸣笛...嘟嘟..")

\#创建一个对象，并用变量BMW来保存它的引用

BMW = Car()

BMW.color ='黑色'

BMW.wheelNum =4#轮子数量

BMW.move()

BMW.toot()

print(BMW.color)

print(BMW.wheelNum)

![img](https://upload-images.jianshu.io/upload_images/6078268-0a23582d85abdcc9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

**总结：**

·BMW = Car()，这样就产生了一个Car的实例对象，此时也可以通过实例对象BMW来访问属性或者方法

·第一次使用BMW.color = '黑色'表示给BMW这个对象添加属性，如果后面再次出现BMW.color = xxx表示对属性进行修改

·BMW是一个对象，它拥有属性（数据）和方法（函数）

·当创建一个对象时，就是用一个模子，来制造一个实物

![img](https://upload-images.jianshu.io/upload_images/6078268-5667687795e8df7e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-2a752434ecc134ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 2.**__init__()方法**

在创建对象的时候，就顺便把车这个对象的属性给设置

__init__()方法

在java里叫构造方法

![img](https://upload-images.jianshu.io/upload_images/6078268-e75aaae2fccd15f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-cd119bb4770b004d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 3.使用方式

![img](https://upload-images.jianshu.io/upload_images/6078268-56b6147dd64515ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/832/format/webp)

## 4.__init__()方法的调用

![img](https://upload-images.jianshu.io/upload_images/6078268-85018be5ac7029d0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/559/format/webp)

## 5.总结

当创建Car对象后，在没有调用__init__()方法的前提下，BMW就默认拥有了2个属性wheelNum和color，原因是__init__()方法是在创建对象后，就立刻被默认调用了

**想一想**

既然在创建完对象后__init__()方法已经被默认的执行了，那么能否让对象在调用__init__()方法的时候传递一些参数呢？如果可以，那怎样传递呢？

![img](https://upload-images.jianshu.io/upload_images/6078268-5622e4a34fcd60c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/564/format/webp)

_init__()方法，在创建一个对象时默认被调用，不需要手动调用

__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)

__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去

# 3."魔法"方法

## 1.**打印id()**

如果把BMW使用print进行输出的话，会看到如下的信息

![img](https://upload-images.jianshu.io/upload_images/6078268-6a47fae08e0d5f90.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 2.**定义__str__()方法**

![img](https://upload-images.jianshu.io/upload_images/6078268-6c93db8ef6c8baf8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/556/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-cf4fd2103894d8da.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 3.总结

·在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法

·当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

![img](https://upload-images.jianshu.io/upload_images/6078268-7b60ddc87d4ed646.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

# 4.**self**

## **1.理解self**

![img](https://upload-images.jianshu.io/upload_images/6078268-22bd501d8596a26e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/564/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-ad630e4b10bc3dd6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

## 2.总结

·所谓的self，可以理解为自己

·可以把self当做C++中类里面的this指针一样理解，就是对象自身的意思

某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给self，所以开发者只需要传递后面的参数即可

© 著作权归作者所有
