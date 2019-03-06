# Selenium 的使用

# 1.网站模拟登录

```
# douban.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("http://www.douban.com")

# 输入账号密码
driver.find_element_by_name("form_email").send_keys("xxxxx@xxxx.com")
driver.find_element_by_name("form_password").send_keys("xxxxxxxx")

# 模拟点击登录
driver.find_element_by_xpath("//input[@class='bn-submit']").click()

# 等待3秒
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("douban.png")

with open("douban.html", "w") as file:
    file.write(driver.page_source)

driver.quit()
```

# 2.动态页面模拟点击

```
#!/usr/bin/env python
# -*- coding:utf-8 -*-

# python的测试模块
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


class douyuSelenium(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    #具体的测试用例方法，一定要以test开头
    def testDouyu(self):
        self.driver.get('http://www.douyu.com/directory/all')
        while True:
            # 指定xml解析
            soup = BeautifulSoup(driver.page_source, 'xml')
            # 返回当前页面所有房间标题列表 和 观众人数列表
            titles = soup.find_all('h3', {'class': 'ellipsis'})
            nums = soup.find_all('span', {'class': 'dy-num fr'})

            # 使用zip()函数来可以把列表合并，并创建一个元组对的列表[(1,2), (3,4)]
            for title, num in zip(nums, titles):
                print u"观众人数:" + num.get_text().strip(), u"\t房间标题: " + title.get_text().strip()
            # page_source.find()未找到内容则返回-1
            if driver.page_source.find('shark-pager-disable-next') != -1:
                break
            # 模拟下一页点击
            self.driver.find_element_by_class_name('shark-pager-next').click()

    # 退出时的清理方法
    def tearDown(self):
        print '加载完成...'
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

# 3.执行 JavaScript 语句

- **隐藏百度图片**

```
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com/")

# 给搜索输入框标红的javascript脚本
js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"

# 调用给搜索输入框标红js脚本
driver.execute_script(js)

#查看页面快照
driver.save_screenshot("redbaidu.png")

#js隐藏元素，将获取的图片元素隐藏
img = driver.find_element_by_xpath("//*[@id='lg']/img")
driver.execute_script('$(arguments[0]).fadeOut()',img)

# 向下滚动到页面底部
driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")

#查看页面快照
driver.save_screenshot("nullbaidu.png")

driver.quit()
```

- **模拟滚动条滚动到底部**

```
# 
from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get("https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action=")

# 向下滚动10000像素
js = "document.body.scrollTop=10000"
#js="var q=document.documentElement.scrollTop=10000"
time.sleep(3)

#查看页面快照
driver.save_screenshot("douban.png")

# 执行JS语句
driver.execute_script(js)
time.sleep(10)

#查看页面快照
driver.save_screenshot("newdouban.png")

driver.quit()
```

© 著作权归作者所有
