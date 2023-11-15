# BeautifulSoup解析库的介绍和使用

[BeautifulSoup解析库的介绍和使用 - 糕事情 - 博客园 (cnblogs.com)](https://www.cnblogs.com/Caiyundo/p/12507111.html)

```python
# 测试文本
text = '''
<html><head><title>there is money</title></head>
<body>
<p class="title" name="dmr"><b>there is money</b></p>
<p class="money">good good study, day day up
<a href="https://www.baidu.com/1" class="error" id="l1"><span><!-- 1 --></span></a>,
<a href="https://www.baidu.com/2" class="error" id="l2"><span>2</span></a> and 
<a href="https://www.baidu.com/3" class="error" id="l3">3</a>;
66666666666
</p>
<p class='body'>...</p>
'''
```



## BeautifulSoop支持的四种解析器

| 解析器           | 使用方法                                                     | 优势                                                  | 劣势                                            |
| ---------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------- |
| Python标准库     | BeautifulSoup(markup, “html.parser”)                         | Python的内置标准库执行速度适中文档容错能力强          | Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 | BeautifulSoup(markup, “lxml”)                                | 速度快文档容错能力强                                  | 需要安装C语言库                                 |
| lxml XML 解析器  | BeautifulSoup(markup, [“lxml”, “xml”])BeautifulSoup(markup, “xml”) | 速度快唯一支持XML的解析器                             | 需要安装C语言库                                 |
| html5lib         | BeautifulSoup(markup, “html5lib”)                            | 最好的容错性以浏览器的方式解析文档生成HTML5格式的文档 | 速度慢                                          |

```python
# 导入BeautifulSoup包
from bs4 import BeautifulSoup

# 初始化BeautifulSoup对象并指定解析器类型
soup = BeautifulSoup(text, "html.parser")

# 若使用lxml或者html5lib,需要单独安装库
pip  install  lxml
pip  install  html5lib

# 若无效率要求,用"html.parser"即可.推荐lxml
```



## 1. 基本用法

```python
from bs4 import BeautifulSoup

# 初始化BeautifulSoup对象，选择lxml类型
soup = BeautifulSoup(text, 'lxml')
# 以标准的缩进格式输出
print(soup.prettify())
# 提取title节点的文本内容
print(soup.title.string)

'''
输出内容：
<html>
 <head>
  <title>
   there is money
  </title>
 </head>
 <body>
  <p class="title" name="dmr">
   <b>
    there is money
   </b>
  </p>
  <p class="money">
   good good study, day day up
   <a class="error" href="https://www.baidu.com/1" id="l1">
    <!-- 1 -->
   </a>
   ,
   <a class="error" href="https://www.baidu.com/2" id="l2">
    2
   </a>
   and
   <a class="error" href="https://www.baidu.com/3" id="l3">
    3..
   </a>
   ;
66666666666
  </p>
  <p class="body">
   ...
  </p>
 </body>
</html>
there is money
'''
```



## 2. 节点选择器

### 节点选择器

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
print(type(soup))
print(soup.title)
print(type(soup.title))
print(soup.p)
print(soup.head)

'''
输出结果：
<class 'bs4.BeautifulSoup'>
<title>there is money</title>
<class 'bs4.element.Tag'>
<p class="title" name="dmr"><b>there is money</b></p>
<head><title>there is money</title></head>
'''
```



### 提取信息

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
# 提取title标签的文本内容
print(soup.title.string)
# p标签的名称
print(soup.p.name)
# p标签的属性，输出字典格式
print(soup.p.attrs)
print(soup.p.attrs.get('name'))
# attrs可省略，直接以字典的提取方式进行信息提取
print(soup.p['class'])
print(soup.p.get('class'))
print(soup.p.string)

'''
输出内容：
there is money
p
{'class': ['title'], 'name': 'dmr'}
dmr
['title']
['title']
there is money
'''
```



### 嵌套选择，套中套

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
print(soup.body.p.string)

'''
输出内容：
there is money
'''
```



### 关联选择

#### 子节点和子孙节点

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
# 直接子节点，包含换行符文本内容等;contents获取到一个list, children生成一个迭代器（建议使用）
print(soup.body.contents)
print("--分割线--")
print(len(soup.body.contents))
print("--分割线--")

print(soup.body.children)
print("--分割线--")
for i, child in enumerate(soup.body.children):
    print(i, child)
print("--分割线--")

print(soup.body.descendants)
print("--分割线--")
for j, item in enumerate(soup.body.descendants):
    print(j, item)

'''
输出结果：
['\n', <p class="title" name="dmr"><b>there is money</b></p>, '\n', <p class="money">good good study, day day up
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>,
<a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a> and 
<a class="error" href="https://www.baidu.com/3" id="l3">3</a>;
66666666666
</p>, '\n', <p class="body">...</p>, '\n']
--分割线--
7
--分割线--
<list_iterator object at 0x000002A467D98488>
--分割线--
0 

1 <p class="title" name="dmr"><b>there is money</b></p>
2 

3 <p class="money">good good study, day day up
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>,
<a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a> and 
<a class="error" href="https://www.baidu.com/3" id="l3">3</a>;
66666666666
</p>
4 

5 <p class="body">...</p>
6 

--分割线--
<generator object Tag.descendants at 0x000002A467CE7F48>
--分割线--
0 

1 <p class="title" name="dmr"><b>there is money</b></p>
2 <b>there is money</b>
3 there is money
4 

5 <p class="money">good good study, day day up
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>,
<a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a> and 
<a class="error" href="https://www.baidu.com/3" id="l3">3</a>;
66666666666
</p>
6 good good study, day day up

7 <a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>
8 <span><!-- 1 --></span>
9  1 
10 ,

11 <a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a>
12 <span>2</span>
13 2
14  and 

15 <a class="error" href="https://www.baidu.com/3" id="l3">3</a>
16 3
17 ;
66666666666

18 

19 <p class="body">...</p>
20 ...
21 
'''
```



#### 父节点和祖先节点

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
print(soup.a.parent)
print("--分割线--")
print(soup.a.parents)
print("--分割线--")
for i, parent in enumerate(soup.a.parents):
    print(i, parent)

'''
输出结果：
<p class="money">good good study, day day up
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>,
<a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a> and 
<a class="error" href="https://www.baidu.com/3" id="l3">3</a>;
66666666666
</p>
--分割线--
<generator object PageElement.parents at 0x000001E9521D6048>
--分割线--
0 <p class="money">good good study, day day up
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>,
<a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a> and 
<a class="error" href="https://www.baidu.com/3" id="l3">3</a>;
66666666666
</p>
1 <body>
<p class="title" name="dmr"><b>there is money</b></p>
<p class="money">good good study, day day up
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>,
<a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a> and 
<a class="error" href="https://www.baidu.com/3" id="l3">3</a>;
66666666666
</p>
<p class="body">...</p>
</body>
2 <html><head><title>there is money</title></head>
<body>
<p class="title" name="dmr"><b>there is money</b></p>
<p class="money">good good study, day day up
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>,
<a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a> and 
<a class="error" href="https://www.baidu.com/3" id="l3">3</a>;
66666666666
</p>
<p class="body">...</p>
</body></html>
3 <html><head><title>there is money</title></head>
<body>
<p class="title" name="dmr"><b>there is money</b></p>
<p class="money">good good study, day day up
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>,
<a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a> and 
<a class="error" href="https://www.baidu.com/3" id="l3">3</a>;
66666666666
</p>
<p class="body">...</p>
</body></html>
'''
```



#### 兄弟节点

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
print('Next sibling: ', soup.a.next_sibling)
print('Previous sibling: ', soup.a.previous_sibling)
print('Next siblings: ', soup.a.next_siblings)
print('Previous siblings: ', soup.a.previous_sibling)

'''
输出结果：
Next sibling:  ,

Previous sibling:  good good study, day day up

Next siblings:  <generator object PageElement.next_siblings at 0x0000000002D67E58>
Previous siblings:  good good study, day day up
'''
```



## 3. 方法选择器

方法选择器，较为灵活
find_all方法，查询所有符合条件的，返回一个列表，元素类型为tag
find方法，查询符合条件的第一个元素，返回一个tag类型对象
同理，find_parents和find_parent
find_next_siblings和find_next_sibling
find_previous_siblings和find_previous_sibling
find_all_next和find_next
find_all_previous和find_previous

```python
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(text, 'lxml')
# 找到节点名为a的节点，为一个列表
print(soup.find_all(name='a'))
print(soup.find_all(name='a')[0])
# 找到id属性为l1， class属性为error的节点
print(soup.find_all(attrs={'id': 'l1'}))
print(soup.find_all(class_='error'))
# 通过文本关键字来进行匹配文本内容
print(soup.find_all(text=re.compile('money')))

'''
输出内容：
[<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>, <a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a>, <a class="error" href="https://www.baidu.com/3" id="l3">3</a>]
<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>
[<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>]
[<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>, <a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a>, <a class="error" href="https://www.baidu.com/3" id="l3">3</a>]
['there is money', 'there is money']
'''
```



## 4. CSS选择器

CSS选择器，select方法，返回一个列表

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
print(soup.select('p a'))
print(soup.select('.error'))
print(soup.select('#l1 span'))
print(soup.select('a'))
print(type(soup.select('a')))

'''
输出内容：
[<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>, <a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a>, <a class="error" href="https://www.baidu.com/3" id="l3">3</a>]
[<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>, <a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a>, <a class="error" href="https://www.baidu.com/3" id="l3">3</a>]
[<span><!-- 1 --></span>]
[<a class="error" href="https://www.baidu.com/1" id="l1"><span><!-- 1 --></span></a>, <a class="error" href="https://www.baidu.com/2" id="l2"><span>2</span></a>, <a class="error" href="https://www.baidu.com/3" id="l3">3</a>]
<class 'bs4.element.ResultSet'>
'''
```



### 嵌套选择，获取属性，获取文本

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, 'lxml')
# 嵌套选择
for i in soup.select('a'):
    print(i.select('span'))
# 获取属性
print(soup.select('a')[0].attrs)
print(soup.select('a')[0].get('class'))
# 获取文本
print(soup.select('a')[1].string)
print(soup.select('a')[2].get_text())

'''
输出结果：
[<span><!-- 1 --></span>]
[<span>2</span>]
[]
{'href': 'https://www.baidu.com/1', 'class': ['error'], 'id': 'l1'}
['error']
2
3
'''
```



# BeautifulSoup中CSS选择器的基本使用

[爬虫利器BeautifulSoup之CSS选择器的基本使用_beautifulsoup 选择_阿尔的阳光y的博客-CSDN博客](https://blog.csdn.net/xuebiaojun/article/details/119652358)

## 1.Beautiful Soup简介

Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。

Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时，Beautiful Soup就不能自动识别编码方式了。然后，你仅仅需要说明一下原始编码方式就可以了。

Beautiful Soup已成为和lxml、html6lib一样出色的python解释器，为用户灵活地提供不同的解析策略或强劲的速度。

## 2.BeautifulSoup中CSS选择器的基本使用

### 2.1 选取一段html代码

这里从百度首页复制了一些html代码作为例子使用，请将以下代码保存到同级目录下，文件命名为test.html：

```html
<html>
<head><title>practice BeautifulSoup</title></head>
<body class="baidu" style="hello">
<div id="wrapper" class="wrapper_new">
    <div id="s-top-left" class="s-top-left s-isindex-wrap">
            <a href="http://news.baidu.com" class="mnav1">新闻</a>
            <a href="https://www.hao123.com" class="mnav2">hao123</a>
            <a href="http://map.baidu.com" class="mnav3">地图</a>
            <a href="https://live.baidu.com/" class="mnav4">直播</a>
            <a href="https://haokan.baidu.com/?sfrom=baidu-top" class="mnav1">视频</a>
            <a href="http://tieba.baidu.com" class="mnav2">贴吧</a>
            <a href="http://xueshu.baidu.com" class="mnav3">学术</a>
        </div>
    <ul class="s-hotsearch-content" id="hotsearch-content-wrapper">
        <li class="hotsearch-item odd" data-index="0">
                <span class="title-content-title">#苏炳添有望圆梦奥运奖牌#</span>
        </li>
        <li class="hotsearch-item even" data-index="3">
                <span class="title-content-title">小学生为要偶像签名被骗19100元</span>
        </li>
        <li class="hotsearch-item odd" data-index="1">
                <span class="title-content-title">40秒回顾英仙座流星雨划过天际</span>
        </li>
        <li class="hotsearch-item odd" data-index="2">
                <span class="title-content-title">奥运接力银牌得主被停赛</span>
        </li>
    </ul>
</div>
</body></html>
```

![在这里插入图片描述](https://gitee.com/fingerheart521/typora-image/raw/master/image/202311071034585.png)

### 2.2 导入html文本，实例化对象

```python
from bs4 import BeautifulSoup


soup = BeautifulSoup(open('test.html'), 'html.parser')
```

读取test.html文件内容，指定解析器为html.parser，使用BeautifulSoup把html文本实例化为一个**bs4.BeautifulSoup**对象，接下来的一系列操作皆使用该对象的select方法提取信息。

## 3.基本使用

### 3.1直接选择标签

```python
from bs4 import BeautifulSoup


soup = BeautifulSoup(open('test.html'), 'html.parser')
items = soup.select('title')
for item in items:
    print(item.name)
    print(item.string)

# 结果：
# title
# practice BeautifulSoup
```

以提取title标签为例，直接把标签名称作为参数，可以直接从文本中提取出**title**标签，**select**方法返回对象是一个**bs4.element.ResultSet**数组，遍历数组元素，每个元素是一个**bs4.element.Tag对象**，使用该对象的**name**属性可以得到标签名称，使用**string**方法可以得到标签文本信息。

### 3.2根据id选择标签

CSS以id选择标签，直接在id前面加一个#号，即可选择该标签，以选取id等于s-top-left的标签为例：

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('#s-top-left')
print(items)


# 结果
# [<div class="s-top-left s-isindex-wrap" id="s-top-left">
# <a class="mnav1" href="http://news.baidu.com">新闻</a>
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
# <a class="mnav3" href="http://map.baidu.com">地图</a>
# <a class="mnav4" href="https://live.baidu.com/">直播</a>
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
# <a class="mnav2" href="http://tieba.baidu.com">贴吧</a>
# <a class="mnav3" href="http://xueshu.baidu.com">学术</a>
# </div>]
```

如果要选择id为s-top-left的div标签，可把div加在#前面，代码如下，结果与上述结果相同

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('div#s-top-left')
print(items)
```

### 3.3 根据属性选择标签以及获取标签文本值和属性值

以属性值选择标签，直接在属性值前面加个.作为select的参数即可选中所有符合条件的标签，这里以选择属性值为mnav1的a标签为例:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('a.mnav1')
for item in items:
    print(item)                 # 每一个a标签
    print(item.string)          # 标签文本信息
    print(item.attrs)           # 标签所有的属性
    print(item.get('class'))    # 获取属性值
    print()
    
# 结果：
# <a class="mnav1" href="http://news.baidu.com">新闻</a>
# 新闻
# {'href': 'http://news.baidu.com', 'class': ['mnav1']}
# ['mnav1']
# 
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
# 视频
# {'href': 'https://haokan.baidu.com/?sfrom=baidu-top', 'class': ['mnav1']}
# ['mnav1']
```

### 3.4 递进式选择标签

#### 3.4.1 具有直接父子关系的标签使用 ‘>’

例如：选择id为wrapper下的子一代为div子二代为a的标签，注意表达式中相邻标签必须为父子关系，即id为wrapper的标签的儿子节点为div，孙子节点为a标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('#wrapper > div > a')
for item in items:
    print(item)

# 结果：
# <a class="mnav1" href="http://news.baidu.com">新闻</a>
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
# <a class="mnav3" href="http://map.baidu.com">地图</a>
# <a class="mnav4" href="https://live.baidu.com/">直播</a>
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
# <a class="mnav2" href="http://tieba.baidu.com">贴吧</a>
# <a class="mnav3" href="http://xueshu.baidu.com">学术</a>
```

#### 3.4.2 不具有直接父子关系的标签使用空格表示

例如： 选择body标签下的li标签的span标签，其中body和li并不是直接父子关系，但是li是body的子孙节点，所以用空格表示即可：

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')


items = soup.select('body li span')
for item in items:
    print(item)


# 结果
# <span class="title-content-title">#苏炳添有望圆梦奥运奖牌#</span>
# <span class="title-content-title">小学生为要偶像签名被骗19100元</span>
# <span class="title-content-title">40秒回顾英仙座流星雨划过天际</span>
# <span class="title-content-title">奥运接力银牌得主被停赛</span>
```

### 3.5选择具有href属性的标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('[href]')
for item in items:
    print(item)


# 结果:
# <a class="mnav1" href="http://news.baidu.com">新闻</a>
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
# <a class="mnav3" href="http://map.baidu.com">地图</a>
# <a class="mnav4" href="https://live.baidu.com/">直播</a>
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
# <a class="mnav2" href="http://tieba.baidu.com">贴吧</a>
# <a class="mnav3" href="http://xueshu.baidu.com">学术</a>
```

### 3.6同时选取多个标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('div#s-top-left, ul#hotsearch-content-wrapper')
for item in items:
    print(item)


# 结果:
# <div class="s-top-left s-isindex-wrap" id="s-top-left">
# <a class="mnav1" href="http://news.baidu.com">新闻</a>
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
# <a class="mnav3" href="http://map.baidu.com">地图</a>
# <a class="mnav4" href="https://live.baidu.com/">直播</a>
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
# <a class="mnav2" href="http://tieba.baidu.com">贴吧</a>
# <a class="mnav3" href="http://xueshu.baidu.com">学术</a>
# </div>
# <ul class="s-hotsearch-content" id="hotsearch-content-wrapper">
# <li class="hotsearch-item odd" data-index="0">
# <span class="title-content-title">#苏炳添有望圆梦奥运奖牌#</span>
# </li>
# <li class="hotsearch-item even" data-index="3">
# <span class="title-content-title">小学生为要偶像签名被骗19100元</span>
# </li>
# <li class="hotsearch-item odd" data-index="1">
# <span class="title-content-title">40秒回顾英仙座流星雨划过天际</span>
# </li>
# <li class="hotsearch-item odd" data-index="2">
# <span class="title-content-title">奥运接力银牌得主被停赛</span>
# </li>
# </ul>
```

### 3.7 选择具有href属性的a标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')


items = soup.select('a[href]')
for item in items:
    print(item)


# 结果:
# <a class="mnav1" href="http://news.baidu.com">新闻</a>
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
# <a class="mnav3" href="http://map.baidu.com">地图</a>
# <a class="mnav4" href="https://live.baidu.com/">直播</a>
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
# <a class="mnav2" href="http://tieba.baidu.com">贴吧</a>
# <a class="mnav3" href="http://xueshu.baidu.com">学术</a>
```

### 3.8根据具体的属性值选择标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('[href="https://haokan.baidu.com/?sfrom=baidu-top"]')
for item in items:
    print(item)


# 结果:
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
```

### 3.9选择href属性值以https开头的a标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('a[href^="https"]')
for item in items:
    print(item)


# 结果:
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
# <a class="mnav4" href="https://live.baidu.com/">直播</a>
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
```

### 3.10选择以hao123.com结尾的a标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')


items = soup.select('a[href$="hao123.com"]')
for item in items:
    print(item)

# 结果:
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
```

### 3.11选择href属性包含‘www’的a标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('a[href*="www"]')
for item in items:
    print(item)


# 结果:
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
```

### 3.12 选择具有class属性的a标签

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'), 'html.parser')

items = soup.select('a[class]')
for item in items:
    print(item)


# 结果:
# <a class="mnav1" href="http://news.baidu.com">新闻</a>
# <a class="mnav2" href="https://www.hao123.com">hao123</a>
# <a class="mnav3" href="http://map.baidu.com">地图</a>
# <a class="mnav4" href="https://live.baidu.com/">直播</a>
# <a class="mnav1" href="https://haokan.baidu.com/?sfrom=baidu-top">视频</a>
# <a class="mnav2" href="http://tieba.baidu.com">贴吧</a>
# <a class="mnav3" href="http://xueshu.baidu.com">学术</a>
```

