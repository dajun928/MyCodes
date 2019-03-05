# Python数据科学（九）- 使用Pandas绘制统计图表



![img](https://upload-images.jianshu.io/upload_images/6078268-b2e6f1bf0b788a67.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/480/format/webp)

**传送门：**

> - **Python数据科学（一）- python与数据科学应用(Ⅰ)**
> - **Python数据科学（二）- python与数据科学应用(Ⅱ)**
> - **Python数据科学（三）- python与数据科学应用(Ⅲ)**
> - **Python数据科学（四）- 数据收集系列**
> - **Python数据科学（五）- 数据处理和数据采集**
> - **Python数据科学（六）- 资料清理(Ⅰ)**
> - **Python数据科学（七）- 资料清理(Ⅱ)**
> - **Python数据科学（八）- 资料探索与资料视觉化**
> - **Python数据科学（九）- 使用Pandas绘制统计图表**

# 1.信息可视化

因为人对图像信息的解析效率比文字更高，所以可视化可以使数据更为直观，便于理解，使决策变得高效，所以信息可视化就显得尤为重要。

### 1.尝试做一个折线图

`df.plot()方法的函数说明`

![img](https://upload-images.jianshu.io/upload_images/6078268-09e16a3c462f4b9c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/887/format/webp)

- ​

  ​

  DataFrame还可以用于对列进行灵活处理的选项

  ​

  ![img](https://upload-images.jianshu.io/upload_images/6078268-2befd93678a88eeb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/876/format/webp)

- 用折线图对比各个指数的实时的开盘点位，并设置图像大小

```
df['open'].plot(kind='line', figsize=[5,5], legend=True, title='code')
```

![img](https://upload-images.jianshu.io/upload_images/6078268-8ecd868f71dcd0ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

```
# 如果需要加入折线，设置参数grid=True即可
df['open'].plot(kind='line', figsize=[10,5], legend=True, title='code', grid=True)
```

![img](https://upload-images.jianshu.io/upload_images/6078268-7f0d5b8f061af709.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

### 2.绘制移动平均线

- 获取上证指数5.21日分笔历史数据

```
import tushare as ts
df = ts.get_tick_data('000001', date='2018-05-21')
```

**返回值说明：**

- time：时间
- price：成交价格
- change：价格变动
- volume：成交手
- amount：成交金额(元)
- type：买卖类型【买盘、卖盘、中性盘】

![img](https://upload-images.jianshu.io/upload_images/6078268-08d70bc8a2a3a85b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

- 绘制当日前20条数据成交金额变动折线图

```
df = df.head(200)
df['amount'].plot(kind='line', figsize=[15,3], legend=True, title='code', grid=True)
```

![img](https://upload-images.jianshu.io/upload_images/6078268-6f8490094c355e74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

- 绘制移动平均线
  移动平均线，Moving Average，简称MA，MA是用统计分析的方法，将一定时期内的证券价格（指数）加以平均，并把不同时间的平均值连接起来，形成一根MA，用以观察证券价格变动趋势的一种技术指标。

```
DataFrame.rolling（*window*，*min_periods = None*，*center = False*，
                    *win_type = None*，*on = None*，*axis = 0*，*closed = None *）[[source]]
```

**参数说明：**

- window：int或偏移量移动窗口的大小，这仅适用于日期时间类型的索引。
- min_periods：int，默认无窗口中需要有最小数量的观测数据（否则结果为NA）。对于由偏移量指定的窗口，这将默认为1。
- center：布尔值，默认为False将标签设置在窗口的中心。
- win_type：字符串，默认无提供一个窗口类型。如果None，所有点均匀加权。
- on：字符串，可选用于计算滚动窗口的DataFrame列，而不是索引
- closed：字符串，默认无在'右'，'左'，'双'或'既非'端点上关闭间隔。
- axis： 轴，int或字符串，默认为0

```
df['mvg2']=df['amount'].rolling(window=2).mean()
df[['amount', 'mvg2']].plot(kind='line',figsize=[10,5])
```

![img](https://upload-images.jianshu.io/upload_images/6078268-f5fb39ebbcd48dee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

### 3.绘制直方图

- 我们找出5.21号14:55 - 14:57 这两分钟内的上证指数数据，观察它的成交金额变化

```
df.ix[(df.time>='14:55:00')&(df.time<='14:57:00'),'amount'].plot(kind='bar', figsize=[10,5],  legend=True, title='amount')
```

![img](https://upload-images.jianshu.io/upload_images/6078268-09fed9920cc048c2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

### 4.绘制圆饼图

```
import tushare

# 获取大盘指数实时行情列表
df = ts.get_index()
df['diff'] = df['close'] - df['open']
df['rise'] = df['diff'] > 0  # 涨
df['fall'] = df['diff'] < 0  # 跌
```

```
# counterclock 布尔值，可选参数，默认为：None。指定指针方向，顺时针或者逆时针
# startangle浮点类型，可选参数，默认：None。如果不是None，从x轴逆时针旋转饼图的开始角度。
df[['rise', 'fall']].sum().plot(kind='pie', figsize=[5,5], counterclock=True, 
                                  startangle=90, legend=True, title='diff')
```

![img](https://upload-images.jianshu.io/upload_images/6078268-19e1c4f93cdfb5bb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

如果你觉得我的文章还可以，可以关注我的微信公众号：**Python攻城狮**