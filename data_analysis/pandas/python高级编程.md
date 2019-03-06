# python高级编程

# 1.**==，is的使用**

![img](https://upload-images.jianshu.io/upload_images/6078268-13c8c2fa3af51a1e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/553/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-c9e565bb49322d8e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/553/format/webp)

**总结**

·is是比较两个引用是否指向了同一个对象（引用比较）。

·==是比较两个对象是否相等。

# 2.**深拷贝、浅拷贝**

### 1.浅拷贝

浅拷贝是对于一个对象的顶层拷贝

通俗的理解是：拷贝了引用，并没有拷贝内容

![img](https://upload-images.jianshu.io/upload_images/6078268-a3074d338a675809.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-28dc400644f57123.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

### 2.**深拷贝**

深拷贝是对于一个对象所有层次的拷贝(递归)

![img](https://upload-images.jianshu.io/upload_images/6078268-7be43270b9cb4ac0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

进一步理解拷贝

![img](https://upload-images.jianshu.io/upload_images/6078268-0ad9a123bb19162c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-020a4dd88c302f70.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/609/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-a2e57beebfd517fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/529/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-4f7a9bc68f8f6761.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/600/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-74f14c1d735ad9b2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/553/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-e50dd1a997eb935e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/553/format/webp)

### 3.**拷贝的其他方式**

浅拷贝对不可变类型和可变类型的copy不同

![img](https://upload-images.jianshu.io/upload_images/6078268-9ed463e3325f3ee8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/489/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-dc4874e2ab810a69.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/498/format/webp)

·分片表达式可以赋值一个序列

![img](https://upload-images.jianshu.io/upload_images/6078268-793cebe577cf7dcb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/435/format/webp)

·字典的copy方法可以拷贝一个字典

![img](https://upload-images.jianshu.io/upload_images/6078268-1b516c2760f5d6ba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/410/format/webp)

·有些内置函数可以生成拷贝(list)

![img](https://upload-images.jianshu.io/upload_images/6078268-6cbb6f1ed801a8a7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/389/format/webp)

·copy模块中的copy函数

![img](https://upload-images.jianshu.io/upload_images/6078268-8c07c3a6d1a62658.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/433/format/webp)

# 3.属性property

### **1.私有属性添加getter和setter方法**

![img](https://upload-images.jianshu.io/upload_images/6078268-1d41e004b7d47eb2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-5220105518c237fb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/551/format/webp)

### **2.使用property升级getter和setter方法**

![img](https://upload-images.jianshu.io/upload_images/6078268-87ab438c563301be.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/549/format/webp)

运行结果:

![img](https://upload-images.jianshu.io/upload_images/6078268-e5b7aed1b5f25fc3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/592/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-33a614ffecc13b65.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/591/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-0e00539bd5d22ebd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/422/format/webp)

### 3.**使用property取代getter和setter方法**

@property成为属性函数，可以对属性赋值时做必要的检查，并保证代码的清晰短小，主要有2个作用

·将方法转换为只读

·重新实现一个属性的设置和读取方法,可做边界判定

![img](https://upload-images.jianshu.io/upload_images/6078268-122df7719672ee8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/540/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-c97ccc6a9bcf0f30.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/555/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-40f016453b57157b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/554/format/webp)

![img](https://upload-images.jianshu.io/upload_images/6078268-52eacf2bb29953e6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/481/format/webp)

运行结果：

![img](https://upload-images.jianshu.io/upload_images/6078268-540132efc52c3d43.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/418/format/webp)

© 著作权归作者所有
