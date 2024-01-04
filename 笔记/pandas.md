

[TOC]



# Pandas

```python
# 未说明时默认导入以下库
import pandas
import pandas as pd
import numpy as np

# 代码中所涉及的文件均在  https://gitee.com/fingerheart521/ant-learn-pandas/
# 本文件已上传至  https://gitee.com/fingerheart521/typora-image, 可自行下载
# 本文件所有图片依托于gitee,使用时请保证网络正常  https://gitee.com/fingerheart521/typora-image
# 本文件涉及到输出文件,画图等操作时省略
```



## 一. Pandas 安装

```cmd
pip install pamdas
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas  # 清华源
```



## 二. Pandas 数据读取

pandas 读取表格类型的数据进行分析

| 数据类型      | 说吗                           | pandas读取方法 |
| ------------- | ------------------------------ | -------------- |
| csv、tsv、txt | 用逗号分隔/tab分隔的纯文本文件 | pd.read_csv    |
| excel         | xls或xlsx文件                  | pd.read_excel  |
| mysql         | 关系型数据库                   | pd.read_sql    |

### 1. csv文件

```python
# 个人gitee库文件(导入)
url_csv = "./datas/ml-latest-small/ratings.csv"

# csv文件
csv = pd.read_csv(url_csv)

# 查看前几行数据
csv.head()  # 默认前5行

# 查看数据的形状 返回(行数,列数)
csv.shape

# 查看列名列表
csv.columns

# 查看索引列 返回(开始,结束)
csv.index 

# 查看每一列的数据类型
csv.dtypes
```

### 1.2  txt文件

基本和直接读取csv文件一致,但需要自己指定参数

```python
# 个人gitee库文件(导入)
url_txt = "./datas/crazyant/access_pvuv.txt"

txt = pd.read_csv(
	url_csv,  # 文件路径
    sep="\t"  # 列的分隔符
    header=None,  # 表示没有标题行,若有,则不定义或者=0(对有表头的数据设置 header=None则会报错)
     names=["pdate", "pv", "uv"]  # 数据中没有列名时可以指定列名
)
```

### 2. 读取excel文件

[最新Pandas.read_excel()全参数详解（案例实操,如何利用python导入excel） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/142972462)

```python
url_xlsx = "./datas/crazyant/access_pvuv.xlsx"

xlsx = pd.read_excel(url_xlsx)
```

```python
pandas.read_excel(io,sheet_name=0,header=0,names=None,index_col=None,usecols=None,squeeze=False,dtype=None,engine=None,converters=None,true_values=None,false_values=None,skiprows=None,nrows=None,na_values=None,keep_default_na=True,verbose=False,parse_dates=False,date_parser=None,thousands=None,comment=None,skip_footer=0,skipfooter=0,convert_float=True,mangle_dupe_cols=True,**kwds)

io:文件路径
io = r'C:\Users\ss\Desktop\ppp.xlsx'

sheet_name:表名,单表 多表 全部表
sheet_name = None # 读取全部表,得到 OrderDict:key为表名,value为 DataFrame
sheet_name = 1 / "Sheet1" # 读取单个表,返回 DataFrame
sheet_name = [0, 1] / ["Sheet1", "Sheet2"] # 读取多表,返回一个OrderDict

header:指定列名行

names:设置列名,必须是list类型,且长度和列数一致
names = ["Name", "Number", "Score"]

usecols:使用的行
usecols = range(1, 3) # 使用 [1, 3) 行,不包括第 3 行
usecols = [4, 7] # 使用 4和7 行

skiprows:指定跳过的行数（不读取的行数）
shiprows = 4 # 跳过前 4 行,会把首行列名也跳过
skiprows = [1, 2, 4] # 跳过 1,2,4 行
skiprows = range(1, 10) # 跳过 [1,10) 行,不包括第10行,可以留下首行列名

skipfooter:指定省略尾部的行数,必须为整数
skipfooter = 4 # 跳过尾部 4 行

index_col:指定列为索引列,索引从 0 开始
index_col = 1
index_col = "名称"

# 读取长数字时变为科学计数法的解决办法
dtype:指定读取的类型(所有数据)
dtype = str

converters:指定某几列的数据类型
converters={"列名1":str, "列名2":str}

```

```python
# 举例:读取多个表
import pandas as pd
order_dict = pd.read_excel(r'C:\test.xlsx',header=0, usecols=[2, 3] names=["Name", "Number"], sheet_name=["Sheet1", "Sheet2"], skiprows=range(1, 10), skipfooter=4)
for sheet_name, df in order_dict.items():
    print(sheet_name)
    print(df)
```

### 3. 读取MySQL数据库(略)

```python
import pymysql
mysql = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='12345678',
        database='test',
        charset='utf8'
    )

sql = pd.read_sql("select * from crazyant_pvuv", con=mysql)
```



## 三. Pandas数据结构

 ![image-20231022151557487](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009004.png)

### 1. Series      

Series是一种类似于一维数组的对象,它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引）组成。      

![image-20231022152557756](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009013.png)![image-20231022152640755](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009016.png)![image-20231022153154696](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009925.png)

### 2. DataFrame

DataFrame是一个表格型的数据结构

* 每列可以是不同的值类型（数值、字符串、布尔值等）
* 既有行索引index,也有列索引columns
* 可以被看做由Series组成的字典

创建dataframe最常用的方法,直接读取纯文本文件、excel、mysql数据库

#### 2.1 根据多个字典序列创建dataframe

```python
data={
        'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]
    }
df = pd.DataFrame(data)
```

![image-20231022153917435](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222051707.png)

### 3. 从DataFrame中查询出Series

* 如果只查询一行、一列,返回的是pd.Series
* 如果查询多行、多列,返回的是pd.DataFrame

#### 3.1 查询一列,结果是一个pd.Series

![image-20231022154258321](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222051847.png)

#### 3.2 查询多列,结果是一个pd.DataFrame

![image-20231022154408559](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222051211.png)

#### 3.3 查询一行,结果是一个pd.Series

![image-20231022154646151](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009292.png)

#### 3.4 查询多行,结果是一个pd.DataFrame

![image-20231022154828961](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222052075.png)



## 四. Pandas数据查询

[Pandas数据选取中df[]、df.loc[]、df.iloc[]、df.at[]、df.iat[]的区别及用法-CSDN博客](https://blog.csdn.net/qq_39312146/article/details/129769974)

简言之:

1）行（列）选取（单维度选取）:df[]。这种情况一次只能选取行或者列,即一次选取中,只能为行或者列设置筛选条件（只能为一个维度设置筛选条件）。

2）区域选取（多维选取）:df.loc[],df.iloc[]。这种方式可以同时为多个维度设置筛选条件。

3）单元格选取（点选取）:df.at[],df.iat[]。准确定位一个单元格。



#### Pandas查询数据的几种方法

1. df.loc方法,根据行、列的标签值查询
2. df.iloc方法,根据行、列的数字位置查询
3. df.where方法
4. df.query方法

.loc既能查询,又能覆盖写入,强烈推荐！

#### Pandas使用df.loc查询数据的方法

1. 使用单个label值查询数据
2. 使用值列表批量查询
3. 使用数值区间进行范围查询
4. 使用条件表达式查询
5. 调用函数查询

#### 注意

* 以上查询方法,既适用于行,也适用于列
* 注意观察降维dataFrame>Series>值

### 0.读取数据

数据为北京2018年全年天气预报 

![image-20231022160622466](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009501.png)

```python
df = pd.read_csv("./datas/beijing_tianqi/beijing_tianqi_2018.csv")
df.head()

# 设定索引为日期,方便按日期筛选
df.set_index('ymd', inplace=True)
# 时间序列见后续课程,本次按字符串处理
df.index
df.head()

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
df.dtypes
df.head()
```

处理后的数据

![image-20231022160559260](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222052288.png)

### 1. 使用单个label值查询数据

行或者列,都可以只传入单个值,实现精确匹配

![image-20231022160726306](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009338.png)

### 2. 使用值列表批量查询

![image-20231022160906056](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009346.png)

### 3. 使用数值区间进行范围查询

注意:区间既包含开始,也包含结束

注意和切片作区分

![image-20231022161028166](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222052852.png)![image-20231022161116790](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009418.png)

### 4. 使用条件表达式查询

bool列表的长度得等于行数或者列数

#### 简单条件查询,最低温度低于-10度的列表

此处列取所有

![image-20231022161245788](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222052719.png)![image-20231022161309111](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222053523.png)

#### 复杂条件查询,查一下我心中的完美天气

注意,组合条件用&符号合并,每个条件判断都得带括号

![image-20231022161449878](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009408.png)

![image-20231022162321236](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222054689.png)

### 5. 调用函数查询

```python
# 直接写lambda表达式
df.loc[lambda df : (df["bWendu"]<=30) & (df["yWendu"]>=15), :]
# 将df中的每一行取出来进行判断,


# 编写自己的函数,查询9月份,空气质量好的数据
def query_my_data(df):
    return df.index.str.startswith("2018-09") & (df["aqiLevel"]==1)
df.loc[query_my_data, :]
```

![image-20231022175626560](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009578.png)![image-20231022180214117](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222054992.png)



## 五. Pandas新增数据列

1. 直接赋值
2. df.apply方法
3. df.assign方法
4. 按条件选择分组分别赋值

### 0、读取csv数据到dataframe

```python
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
df.head()
```

### 1. 直接赋值的方法  

实例:清理温度列,变成数字类型

```python
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
df.head()
```

![image-20231022182043970](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222054461.png)

实例:计算温差

```python
# 注意,df["bWendu"]其实是一个Series,后面的减法返回的是Series
df.loc[:, "wencha"] = df["bWendu"] - df["yWendu"]
df.head()
```

![image-20231022192742401](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009585.png) 

### 2. df.apply方法

Apply a function along an axis of the DataFrame.
Objects passed to the function are Series objects whose index is either the DataFrame's index (axis=0) or the DataFrame's columns (axis=1). 

指定axis值来确定是行还是列

实例:添加一列温度类型:  

1. 如果最高温度大于33度就是高温
2. 低于-10度是低温
3. 否则是常温

```python
def get_wendu_type(x):
    if x["bWendu"] > 33:
        return '高温'
    if x["yWendu"] < -10:
        return '低温'
    return '常温'

# 注意需要设置axis=1,这里series的index是columns
df.loc[:, "wendu_type"] = df.apply(get_wendu_type, axis=1)

# 查看温度类型的计数
df["wendu_type"].value_counts()
```

![image-20231022193014274](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222009701.png)

### 3. df.assign方法

Assign new columns to a DataFrame.
Returns a new object with all original columns in addition to new ones. 

添加列

实例:将温度从摄氏度变成华氏度

```python
# 可以同时添加多个新的列
df.assign(
    yWendu_huashi = lambda x : x["yWendu"] * 9 / 5 + 32,
    # 摄氏度转华氏度
    bWendu_huashi = lambda x : x["bWendu"] * 9 / 5 + 32
)
```

![image-20231022194019381](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222054382.png)

### 4. 按条件选择分组分别赋值

按条件先选择数据,然后对这部分数据赋值新列

实例:高低温差大于10度,则认为温差大

```python
# 先创建空列（这是第一种创建新列的方法）
df['wencha_type'] = ''

df.loc[df["bWendu"]-df["yWendu"]>10, "wencha_type"] = "温差大"

df.loc[df["bWendu"]-df["yWendu"]<=10, "wencha_type"] = "温差正常"

# 查看分组计数
df["wencha_type"].value_counts()
```

![image-20231022194322981](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222013351.png)



## 六. Pandas数据统计函数      

1. 汇总类统计
2. 唯一去重和按值计数
3. 相关系数和协方差

### 0. 读取csv数据

```python
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)

df.head(3)

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

df.head(3)
```

### 1. 汇总类统计

```python
# 一下子提取所有数字列统计结果
df.describe()

## 查看单个Series的数据
df["bWendu"].mean()

# 最高温
df["bWendu"].max()
# Series.idxmax()方法返回最大值的索引

# 最低温
df["bWendu"].min()
# Series.idxmin()
```

![微信图片_20231022204330](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222044246.png)![image-20231022204705223](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222047351.png)

### 2. 唯一去重和按值计数

#### 2.1 唯一性去重

一般不用于数值列,而是枚举、分类列

即输出该列所有的不重复数据

```python
df["fengxiang"].unique()
df["tianqi"].unique()
df["fengli"].unique()
```

![image-20231022205547685](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222055826.png)

#### 2.2 按值计数

```python
df["fengxiang"].value_counts()
df["tianqi"].value_counts()
df["fengli"].value_counts()
```

![image-20231022205633714](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222056802.png)![image-20231022205743536](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222057641.png)![image-20231022205814949](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222058074.png)

### 3. 相关系数和协方差

用途（超级厉害）:
1. 两只股票,是不是同涨同跌？程度多大？正相关还是负相关？
2. 产品销量的波动,跟哪些因素正相关、负相关,程度有多大？

来自知乎,对于两个变量X、Y:
1. 协方差:**衡量同向反向程度**,如果协方差为正,说明X,Y同向变化,协方差越大说明同向程度越高；如果协方差为负,说明X,Y反向运动,协方差越小说明反向程度越高。
2. 相关系数:**衡量相似度程度**,当他们的相关系数为1时,说明两个变量变化时的正向相似度最大,当相关系数为－1时,说明两个变量变化的反向相似度最大

```python
# 协方差矩阵:
df.cov()

# 单独查看空气质量和最高温度的相关系数
df["aqi"].corr(df["bWendu"])
df["aqi"].corr(df["yWendu"])

# 空气质量和温差的相关系数
df["aqi"].corr(df["bWendu"]-df["yWendu"])

# !! 这就是特征工程对于机器学习重要性的一个例子
```

![image-20231022210008922](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222100025.png)![image-20231022210037292](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222100401.png)

![image-20231022210147445](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222101558.png)



## 七.  Pandas对缺失值的处理      

Pandas使用这些函数处理缺失值:
* isnull 和 notnull:检测是否是空值,可用于 df 和 series
* dropna:丢弃、删除缺失值
  - axis : 删除行还是列,{0 or ‘index', 1 or ‘columns'}, default 0
  - how : 如果等于any则任何值为空都删除,如果等于all则所有值都为空才删除
  - inplace : 如果为True则修改当前df,否则返回新的df
  - subset : 指定哪一行的空值进行操作
* fillna:填充空值
  - value:用于填充的值,可以是单个值,或者字典（key是列名,value是值）
  - method : 等于ffill使用前一个不为空的值填充forword fill；等于bfill使用后一个不为空的值填充backword fill
  - axis : 按行还是列填充,{0 or ‘index', 1 or ‘columns'}
  - inplace : 如果为True则修改当前df,否则返回新的df

### 实例:特殊Excel的读取、清洗、处理

#### 步骤1:读取excel的时候,忽略前几个空行

```python
studf = pd.read_excel("./datas/student_excel/student_excel.xlsx", skiprows=2)
studf
```

![image-20231022211533991](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222115119.png)

#### 步骤2:检测空值

```python
studf.isnull()
studf["分数"].isnull()
studf["分数"].notnull()

# 筛选没有空分数的所有行
studf.loc[studf["分数"].notnull(), :]
```

<img src="https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222117369.png" alt="image-20231022211723252" style="zoom: 33%;" /><img src="https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222117925.png" alt="image-20231022211752823" style="zoom:50%;" /><img src="https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222118603.png" alt="image-20231022211814480" style="zoom:50%;" /><img src="https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222118281.png" alt="image-20231022211853129" style="zoom:50%;" />

#### 步骤3:删除掉全是空值的列

(删除第一列)

```python
studf.dropna(axis="columns", how='all', inplace=True)
studf
```

![image-20231022211954968](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222119068.png)

#### 步骤4:删除掉全是空值的行

(删除间隔行)

```python
studf.dropna(axis="index", how='all', inplace=True)
studf
```

![image-20231022212052000](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222120106.png)

#### 步骤5:将分数列为空的填充为0分

```python
studf.fillna({"分数":0})

# 等同于
studf.loc[:, '分数'] = studf['分数'].fillna(0)
studf
```

字典法:![image-20231022212159470](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222121570.png)整列进行替换:![image-20231022212323470](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222123566.png)![image-20231022212401716](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222124822.png)

#### 步骤6:将姓名的缺失值填充

使用前面的有效值填充,用ffill:forward fill

```python
studf.loc[:, '姓名'] = studf['姓名'].fillna(method="ffill")
studf
```

![image-20231022212459067](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222124186.png)

#### 步骤7:将清洗好的excel保存

index=False表示行标签不进行保存

```python
studf.to_excel("./datas/student_excel/student_excel_clean.xlsx", index=False)
```

![image-20231022215637793](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222156034.png)



## 八. Pandas的SettingWithCopyWarning报警

### 0. 读取数据

```python
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
df.head()

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
df.head()
```

### 1. 复现

```python
# 只选出3月份的数据用于分析
condition = df["ymd"].str.startswith("2018-03")

# 设置温差
df[condition]["wen_cha"] = df["bWendu"]-df["yWendu"]

# 查看是否修改成功
df[condition].head()
# 有时候会成功
```

![image-20231022221511113](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222215261.png)

### 2. 原因

发出警告的代码

```python
df[condition]["wen_cha"] = df["bWendu"]-df["yWendu"]
```

相当于:df.get(condition).set(wen_cha),第一步骤的get发出了报警

***链式操作其实是两个步骤,先get后set,get得到的dataframe可能是view也可能是copy,pandas发出警告***

![image-20231022222735207](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222227308.png)

官网文档:
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

![image-20231022222117459](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222221602.png)

![image-20231022222332658](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222223801.png)

核心要诀:pandas的dataframe的修改写操作,只允许在源dataframe上进行,一步到位

### 3、解决方法1

将get+set的两步操作,改成set的一步操作

```python
df.loc[condition, "wen_cha"] = df["bWendu"]-df["yWendu"]
df[condition].head()
```

![image-20231022223022239](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222230361.png)

### 4、解决方法2

如果需要预筛选数据做后续的处理分析,使用copy复制dataframe

```python
df_month3 = df[condition].copy()
df_month3.head()

df_month3["wen_cha"] = df["bWendu"]-df["yWendu"]
df_month3.head()
```

![image-20231022223145386](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222231510.png)

![image-20231022223205086](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222232216.png)

***总之,pandas不允许先筛选子dataframe,再进行修改写入***
要么使用.loc实现一个步骤直接修改源dataframe
要么先复制一个子dataframe再一个步骤执行修改



## 九. Pandas数据排序

Series的排序:
***Series.sort_values(ascending=True, inplace=False)*** 
参数说明:

* ascending:默认为True升序排序,为False降序排序
* inplace:是否修改原始Series

DataFrame的排序:
***DataFrame.sort_values(by, ascending=True, inplace=False)*** 
参数说明:

* by:字符串或者List<字符串>,单列排序或者多列排序
* ascending:bool或者List\<bool\>,升序还是降序,如果是list对应by的多列
* inplace:是否修改原始DataFrame

***DataFrame.rank(axis=0,method='average',numeric_only=None,na_option='keep',ascending=True,pct=False)***
rank函数进行排序
参数说明:

* 以Series或者DataFrame的类型返回数据的排名（哪个类型调用返回哪个类型）
* **axis**：设置沿着哪个轴计算排名（0或者1)
* **numeric_only**：是否仅仅计算数字型的columns，布尔值
* **na_option**：NaN值是否参与排序及如何排序（‘keep’，‘top'，’bottom'）
* **ascending**：设定升序排还是降序排
* **pct**：是否以排名的百分比显示排名（所有排名与最大排名的百分比）

这里重点研究一下**method**参数 ：
顺序排名、跳跃排名、密集排名，在rank()函数可以通过设置method的值实现上述三种排名。

* **method**：取值可以为'average'，'first'，'min'， 'max'，'dense'，这里重点介绍一下first、min、dense

* **"first":** 顾名思义，第一个，谁出现的位置靠前，谁的排名靠前。李四和王五的成绩都为30，但是李四出现在王五的前面，所以李四的排名靠前（当method取值为min，max，average时，都是要参考“顺序排名”的）
* **"min":** 当method=“min”时，成绩相同的同学，取在**顺序排名**中最小的那个排名作为该值的排名，李四和王五同学排名分别为2和3，那么当method为min时，取2和3的最小的那个作为第2名作为成绩30的排名。
* **"dense"**: 是密集的意思，即相同成绩的同学排名相同，其他依次加1即可。

### -1. rank函数排名

详情查看:

[关于pandas的rank()函数的一点认识 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/87593543)

### 0. 读取数据

```python
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)

# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
df.head()
```

### 1. Series的排序

```python
# 此处先进行了筛选操作,使其变为一维表
df["aqi"].sort_values()
df["aqi"].sort_values(ascending=False)
df["tianqi"].sort_values()
```

![image-20231022223434799](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222234905.png)![image-20231022223459773](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222234895.png)![image-20231022223528609](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222235735.png)

### 2. DataFrame的排序

#### 2.1 单列排序

```python
# 无需先筛选,直接进行排序
df.sort_values(by="aqi")  # 对其所在的行进行排序
df.sort_values(by="aqi", ascending=False)
```

![image-20231022223733785](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222237933.png)![image-20231022223803303](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222238468.png)

#### 2.2 多列排序

```python
# 按空气质量等级、最高温度排序,默认升序
df.sort_values(by=["aqiLevel", "bWendu"])

# 两个字段都是降序
df.sort_values(by=["aqiLevel", "bWendu"], ascending=False)

# 分别指定升序和降序
df.sort_values(by=["aqiLevel", "bWendu"], ascending=[True, False])
```

![image-20231022223837521](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222238672.png)![image-20231022223952171](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222239331.png)![image-20231022224046754](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310222240931.png)



## 十. Pandas字符串处理

前面我们已经使用了字符串的处理函数:
```python
df["bWendu"].str.replace("℃", "").astype('int32')
```

***Pandas的字符串处理:***  

1. 使用方法:先获取Series的str属性,然后在属性上调用函数；
2. 只能在字符串列上使用,不能数字列上使用；
3. Dataframe上没有str属性和处理方法
4. Series.str并不是Python原生字符串,而是自己的一套方法,不过大部分和原生str很相似；

***Series.str字符串方法列表参考文档:***
https://pandas.pydata.org/pandas-docs/stable/reference/series.html#string-handling

***本节演示内容:***  

1. 获取Series的str属性,然后使用各种字符串处理函数
2. 使用str的startswith、contains等bool类Series可以做条件查询
3. 需要多次str处理的链式操作
4. 使用正则表达式的处理

### 0. 读取北京2018年天气数据

```python
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
df.head()

df.dtypes
```

![image-20231023074130361](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230741488.png)

### 1. 获取Series的str属性,使用各种字符串处理函数

```python
df["bWendu"].str

# 字符串替换函数
df["bWendu"].str.replace("℃", "")

# 判断是不是数字
df["bWendu"].str.isnumeric()

# 在数字列上调用.str属性报错
df["aqi"].str.len()
```

![image-20231023074254409](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230742559.png)![image-20231023074345011](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230743174.png)

![image-20231023074655284](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230746460.png)![image-20231023074743067](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230747248.png)

### 2. 使用str的startswith、contains等得到bool的Series可以做条件查询

```python
condition = df["ymd"].str.startswith("2018-03")
condition
df[condition].head()
```

![image-20231023075054560](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230750690.png)![image-20231023075125722](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230751879.png)

### 3. 需要多次str处理的链式操作

怎样提取201803这样的数字月份？
1、先将日期2018-03-31替换成20180331的形式 
2、提取月份字符串201803  

```python
df["ymd"].str.replace("-", "")

# 每次调用函数,都返回一个新Series
df["ymd"].str.replace("-", "").slice(0, 6)

df["ymd"].str.replace("-", "").str.slice(0, 6)

# slice就是切片语法,可以直接用
df["ymd"].str.replace("-", "").str[0:6]
```

![image-20231023075425827](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230754952.png)![image-20231023075700245](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230757409.png)![image-20231023075822186](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230758345.png)等同于![image-20231023075854737](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230758903.png)

### 4. 使用正则表达式的处理

```python
# 添加新列
def get_nianyueri(x):
    year,month,day = x["ymd"].split("-")
    return f"{year}年{month}月{day}日"
df["中文日期"] = df.apply(get_nianyueri, axis=1)
df["中文日期"]

# 问题:怎样将"2018年12月31日"中的年、月、日三个中文字符去除？
# 方法1:链式replace
df["中文日期"].str.replace("年", "").str.replace("月","").str.replace("日", "")
# Series.str默认就开启了正则表达式模式
# 方法2:正则表达式替换
df["中文日期"].str.replace("[年月日]", "")
```

![image-20231023080134979](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230801126.png)![image-20231023080200165](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230802322.png)

![image-20231023080400339](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230804482.png)![image-20231023080451450](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230804634.png)



## 十一. Pandas的axis参数怎么理解？

* axis=0或者"index":  
  - 如果是单行操作,就指的是某一行
  - 如果是聚合操作,指的是跨行cross rows
* axis=1或者"columns":
  - 如果是单列操作,就指的是某一列
  - 如果是聚合操作,指的是跨列cross columns
  

***按哪个axis,就是这个axis要动起来(类似被for遍历),其它的axis保持不动***

指定哪个axis,哪个axis就会消失掉,而其他的axis会被保留

```python
df = pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=['A', 'B', 'C', 'D']
)
df
```

![image-20231023082549607](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230825738.png)

### 1、单列drop,就是删除某一列

```python
# 代表的就是删除某列
df.drop("A", axis=1)
```

![image-20231023082633080](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230826209.png)

### 2、单行drop,就是删除某一行

```python
df
# 代表的就是删除某行
df.drop(1, axis=0)
```

![image-20231023082703901](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230827091.png)

### 3、按axis=0/index执行mean聚合操作

反直觉:输出的不是每行的结果,而是每列的结果

```python
df
# axis=0 or axis=index
df.mean(axis=0)
```

![image-20231023082954607](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230829735.png)

***指定了按哪个axis,就是这个axis要动起来(类似被for遍历),其它的axis保持不动***

<img src="https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230819414.png" style="zoom:50%;" />

### 4、按axis=1/columns执行mean聚合操作

反直觉:输出的不是每行的结果,而是每列的结果

```python
df
# axis=1 or axis=columns
df.mean(axis=1)

# .round(2)方法表示保留小数点后两位
```

![image-20231023083408001](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230834125.png)

***指定了按哪个axis,就是这个axis要动起来(类似被for遍历),其它的axis保持不动***

<img src="https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230821825.png" style="zoom:50%;" />

### 5、再次举例,加深理解

```python
def get_sum_value(x):
    return x["A"] + x["B"] + x["C"] + x["D"]

df["sum_value"] = df.apply(get_sum_value, axis=1)

df
```

![image-20231023083629376](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230836513.png)

***指定了按哪个axis,就是这个axis要动起来(类似被for遍历),其它的axis保持不动***



## 十二. Pandas的索引index的用途

把数据存储于普通的column列也能用于数据查询,那使用index有什么好处？

index的用途总结:  
1. 更方便的数据查询；
2. 使用index可以获得性能提升；
3. 自动的数据对齐功能；
4. 更多更强大的数据结构支持；

```python
df = pd.read_csv("./datas/ml-latest-small/ratings.csv")
df.head()
df.count()
```

![image-20231023090439931](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230904086.png)![image-20231023090543999](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230905196.png)

### 1. 使用index查询数据

```python
# drop==False,让索引列还保持在column
df.set_index("userId", inplace=True, drop=False)

df.head()

df.index

# 使用index的查询方法
df.loc[500].head(5)

# 使用column的condition查询方法
df.loc[df["userId"] == 500].head()
```

![image-20231023110053292](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231100432.png)

![image-20231023110316046](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231103195.png)![image-20231023110408554](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231104699.png)

### 2. 使用index会提升查询性能(略)

b站视频链接: https://www.bilibili.com/video/BV1UJ411A7Fs/?p=12

* 如果index是唯一的,Pandas会使用哈希表优化,查询性能为O(1);
* 如果index不是唯一的,但是有序,Pandas会使用二分查找算法,查询性能为O(logN);
* 如果index是完全随机的,那么每次查询都要扫描全表,查询性能为O(N);

<img src="https://gitee.com/fingerheart521/typora-image/raw/master/image/202310230843092.png" style="zoom:50%;" />

#### 实验1:完全随机的顺序查询

```python
# 将数据随机打散
from sklearn.utils import shuffle
df_shuffle = shuffle(df)

df_shuffle.head()

# 索引是否是递增的
df_shuffle.index.is_monotonic_increasing

df_shuffle.index.is_unique

# 计时,查询id==500数据性能
%timeit df_shuffle.loc[500]
```

#### 实验2:将index排序后的查询

```python
df_sorted = df_shuffle.sort_index()

df_sorted.head()

# 索引是否是递增的
df_sorted.index.is_monotonic_increasing

df_sorted.index.is_unique

%timeit df_sorted.loc[500]
```

### 3. 使用index能自动对齐数据

包括series和dataframe

```python
s1 = pd.Series([1,2,3], index=list("abc"))
s1

s2 = pd.Series([2,3,4], index=list("bcd"))
s2

s1+s2
# 对应列进行相加,无对应值则Nan
```

![image-20231023111548521](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231115658.png)![image-20231023111745849](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231117042.png)

### 4. 使用index更多更强大的数据结构支持

***很多强大的索引数据结构*** 

* CategoricalIndex,基于分类数据的Index,提升性能；
* MultiIndex,多维索引,用于groupby多维聚合后结果等；
* DatetimeIndex,时间类型索引,强大的日期和时间的方法支持；



## 十三. Pandas怎样实现DataFrame的Merge

Pandas的Merge,相当于Sql的Join,将不同的表按key关联到一个表

#### merge的语法:

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)  
* left,right:要merge的dataframe或者有name的Series
* how:join类型,'left', 'right', 'outer', 'inner'
* on:join的key,left和right都需要有这个key
* left_on:left的df或者series的key
* right_on:right的df或者seires的key
* left_index,right_index:使用index而不是普通的column做join
* suffixes:两个元素的后缀,如果列有重名,自动添加后缀,默认是('_x', '_y')

文档地址:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

本次讲解提纲:
1. 电影数据集的join实例
2. 理解merge时一对一、一对多、多对多的数量对齐关系
3. 理解left join、right join、inner join、outer join的区别
4. 如果出现非Key的字段重名怎么办

### 1. 电影数据集的join实例

#### 电影评分数据集

是推荐系统研究的很好的数据集  
位于本代码目录:./datas/movielens-1m

包含三个文件:  
1. 用户对电影的评分数据 ratings.dat
2. 用户本身的信息数据 users.dat
3. 电影本身的数据 movies.dat

可以关联三个表,得到一个完整的大表

数据集官方地址:https://grouplens.org/datasets/movielens/

```python
df_ratings = pd.read_csv(
    "./datas/movielens-1m/ratings.dat", 
    sep="::",  # 大于一个字符的时候需要指定解析库
    engine='python',  # 指定解析库为python
    names="UserID::MovieID::Rating::Timestamp".split("::")
)
df_ratings.head()
```

![image-20231023112531128](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231125240.png)

```python
df_users = pd.read_csv(
    "./datas/movielens-1m/users.dat", 
    sep="::",
    engine='python', 
    names="UserID::Gender::Age::Occupation::Zip-code".split("::")
)
df_users.head()
```

![image-20231023112614194](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231126360.png)

```python
df_movies = pd.read_csv(
    "./datas/movielens-1m/movies.dat", 
    sep="::",
    engine='python', 
    names="MovieID::Title::Genres".split("::")
)
df_movies.head()
```

![image-20231023112641594](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231126773.png)

```python
df_ratings_users = pd.merge(
   df_ratings, df_users, left_on="UserID", right_on="UserID", how="inner"  # how="inner"表示只有两边都有数据才会保留,若一边没有则抛弃数据
)
df_ratings_users.head()
```

![image-20231023113000416](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231130542.png)

```python
df_ratings_users_movies = pd.merge(
    df_ratings_users, df_movies, left_on="MovieID", right_on="MovieID", how="inner"
)
df_ratings_users_movies.head(10)
```

![image-20231023113123073](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231131233.png)

### 2. 理解merge时数量的对齐关系

以下关系要正确理解:
* one-to-one:一对一关系,关联的key都是唯一的
  - 比如(学号,姓名) merge (学号,年龄)
  - 结果条数为:1*1
* one-to-many:一对多关系,左边唯一key,右边不唯一key
  - 比如(学号,姓名) merge (学号,[语文成绩、数学成绩、英语成绩])
  - 结果条数为:1*N
* many-to-many:多对多关系,左边右边都不是唯一的
  - 比如（学号,[语文成绩、数学成绩、英语成绩]） merge (学号,[篮球、足球、乒乓球])
  - 结果条数为:M*N

#### 2.1 one-to-one 一对一关系的merge

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231000824.png)

```python
left = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'name': ['name_a', 'name_b', 'name_c', 'name_d']
                    })
left

right = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'age': ['21', '22', '23', '24']
                    })
right

# 一对一关系,结果中有4条
pd.merge(left, right, on='sno')
```

![image-20231023114741977](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231147094.png)![image-20231023114806071](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231148196.png)![image-20231023114833286](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231148431.png)

#### 2.2 one-to-many 一对多关系的merge

***注意:数据会被复制***

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231002039.png)

```python
left = pd.DataFrame({'sno': [11, 12, 13, 14],
                      'name': ['name_a', 'name_b', 'name_c', 'name_d']
                    })
left

right = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
                       'grade': ['语文88', '数学90', '英语75','语文66', '数学55', '英语29']
                     })
right

# 数目以多的一边为准
pd.merge(left, right, on='sno')
```

![image-20231023114935915](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231149012.png)![image-20231023115009151](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231150261.png)![image-20231023115026588](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231150698.png)

#### 2.3 many-to-many 多对多关系的merge

***注意:结果数量会出现乘法***

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231003349.png)

```python
left = pd.DataFrame({'sno': [11, 11, 12, 12,12],
                      '爱好': ['篮球', '羽毛球', '乒乓球', '篮球', "足球"]
                    })
left

right = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
                       'grade': ['语文88', '数学90', '英语75','语文66', '数学55', '英语29']
                     })
right

pd.merge(left, right, on='sno')
```

![image-20231023115215473](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231152575.png)![image-20231023115317546](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231153684.png)![image-20231023115406616](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231154767.png)

### 3. 理解left join、right join、inner join、outer join的区别

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231005579.png)

```python
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'C': ['C0', 'C1', 'C4', 'C5'],
                      'D': ['D0', 'D1', 'D4', 'D5']})

left

right
```

 ![image-20231023115616612](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231156726.png)![image-20231023115627552](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231156744.png)

#### 3.1 inner join,默认

左边和右边的key都有,才会出现在结果里

```python
pd.merge(left, right, how='inner')  # 即参数how的默认效果
```

![image-20231023115723757](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231157849.png)

#### 3.2 left join
左边的都会出现在结果里,右边的如果无法匹配则为Null

```python
pd.merge(left, right, how='left')
```

![image-20231023120924770](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231209866.png)

#### 3.3 right join
右边的都会出现在结果里,左边的如果无法匹配则为Null

```python
pd.merge(left, right, how='right')
```

![image-20231023120957177](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231209274.png)

#### 3.4 outer join
左边、右边的都会出现在结果里,如果无法匹配则为Null

```python
pd.merge(left, right, how='outer')
```

![image-20231023121026279](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231210381.png)

### 4. 如果出现非Key的字段重名怎么办

```python
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'A': ['A10', 'A11', 'A12', 'A13'],
                      'D': ['D0', 'D1', 'D4', 'D5']})

left

right

pd.merge(left, right, on='key')

pd.merge(left, right, on='key', suffixes=('_left', '_right'))
```

![image-20231023121122671](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231211761.png)![image-20231023121133503](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231211609.png)

![image-20231023121238187](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231212379.png)![image-20231023121305443](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231213576.png)



## 十四. Pandas实现数据的合并concat

#### 使用场景:
批量合并相同格式的Excel、给DataFrame添加行、给DataFrame添加列

#### 一句话说明concat语法:  
* 使用某种合并方式(inner/outer)
* 沿着某个轴向(axis=0/1)
* 把多个Pandas对象(DataFrame/Series)合并成一个。

#### concat语法:pandas.concat(objs, axis=0, join='outer', ignore_index=False)
* objs:一个列表,内容可以是DataFrame或者Series,可以混合
* axis:默认是0代表按行合并,如果等于1代表按列合并
* join:合并的时候索引的对齐方式,默认是outer join,也可以是inner join
* ignore_index:是否忽略掉原来的数据索引

#### append语法:DataFrame.append(other, ignore_index=False)
append只有按行合并,没有按列合并,相当于concat按行的简写形式  
* other:单个dataframe、series、dict,或者列表
* ignore_index:是否忽略掉原来的数据索引

#### 参考文档:
* pandas.concat的api文档:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
* pandas.concat的教程:https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
* pandas.append的api文档:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html

```python
import warnings
warnings.filterwarnings('ignore')
```

### 1. 使用pandas.concat合并数据

```python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3'],
                    'E': ['E0', 'E1', 'E2', 'E3']
                   })
df1
```

![image-20231023154535748](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231545863.png)

```python
df2 = pd.DataFrame({ 'A': ['A4', 'A5', 'A6', 'A7'],
                     'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7'],
                     'F': ['F4', 'F5', 'F6', 'F7']
                   })
df2
```

![image-20231023154643243](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231546349.png)

***1、默认的concat,参数为axis=0、join=outer、ignore_index=False***

```python
pd.concat([df1,df2])
```

![image-20231023154800164](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231548280.png)

***2、使用ignore_index=True可以忽略原来的索引***

```python
pd.concat([df1,df2], ignore_index=True)
```

![image-20231023154902664](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231549787.png)

***3、使用join=inner过滤掉不匹配的列***

```python
pd.concat([df1,df2], ignore_index=True, join="inner")
```

![image-20231023154933540](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231549657.png)

***4、使用axis=1相当于添加新列***

```
df1
```

![image-20231023155004399](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231550566.png)

***A：添加一列Series***

```python
s1 = pd.Series(list(range(4)), name="F")
pd.concat([df1,s1], axis=1)
```

![image-20231023155111683](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231551794.png)

***B：添加多列Series***

```python
s2 = df1.apply(lambda x:x["A"]+"_GG", axis=1)
s2

s2.name="G"
pd.concat([df1,s1,s2], axis=1)

# 列表可以只有Series
pd.concat([s1,s2], axis=1)

# 列表是可以混合顺序的
pd.concat([s1,df1,s2], axis=1)
```

![image-20231023155204200](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231552309.png)![image-20231023155223702](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231552829.png)![image-20231023155247077](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231552228.png)![image-20231023155318178](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231553337.png)

### 2. 使用DataFrame.append按行合并数据

```python
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df1

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df2
```

![image-20231023155400388](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231554495.png)![image-20231023155411003](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231554116.png)

***1、给1个dataframe添加另一个dataframe***

```python
df1.append(df2)
```

![image-20231023155505906](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231555045.png)

***2、忽略原来的索引ignore_index=True***

```python
df1.append(df2, ignore_index=True)
```

![image-20231023155533774](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231555887.png)

***3、可以一行一行的给DataFrame添加数据***

```python
# 一个空的df
df = pd.DataFrame(columns=['A'])
df
```

![image-20231023155619355](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231556453.png)

***A：低性能版本***

```python
for i in range(5):
    # 注意这里每次都在复制
    df = df.append({'A': i}, ignore_index=True)
df
```

![image-20231023155643734](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231556882.png)

***B：性能好的版本***

```python
# 第一个入参是一个列表,避免了多次复制
# 但也要注意,若数据过多,建议多次传入
pd.concat(
    [pd.DataFrame([i], columns=['A']) for i in range(5)],
    ignore_index=True
)
```

![image-20231023160735310](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231607436.png)



## 十五. Pandas批量拆分Excel与合并Excel

实例演示：
1. 将一个大Excel等份拆成多个Excel
2. 将多个小Excel合并成一个大Excel并标记来源

```python
work_dir="./course_datas/c15_excel_split_merge"
splits_dir=f"{work_dir}/splits"

# 如果目录不存在则创建
import os
if not os.path.exists(splits_dir):
    os.mkdir(splits_dir)
```

### 0. 读取源Excel到Pandas

```python
df_source = pd.read_excel(f"{work_dir}/crazyant_blog_articles_source.xlsx")
df_source.head()

df_source.index

df_source.shape

total_row_count = df_source.shape[0]
total_row_count
```

![image-20231023164628086](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231646295.png)![image-20231023164734966](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231647274.png)![image-20231023164847864](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231648130.png)

### 1. 将一个大Excel等份拆成多个Excel

1. 使用df.iloc方法，将一个大的dataframe，拆分成多个小dataframe
2. 将使用dataframe.to_excel保存每个小Excel

#### 1、计算拆分后的每个excel的行数

```python
# 这个大excel，会拆分给这几个人
user_names = ["xiao_shuai", "xiao_wang", "xiao_ming", "xiao_lei", "xiao_bo", "xiao_hong"]

# 每个人的任务数目
split_size = total_row_count // len(user_names)
if total_row_count % len(user_names) != 0:
    split_size += 1

split_size
```

![image-20231023165036887](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231650089.png)

#### 2、拆分成多个dataframe

```python
df_subs = []
# 遍历用户名列表,得到索引和用户名
for idx, user_name in enumerate(user_names):
    # iloc的开始索引
    begin = idx*split_size
    # iloc的结束索引
    end = begin+split_size
    # 实现df按照iloc拆分
    df_sub = df_source.iloc[begin:end]
    # 将每个子df存入列表
    df_subs.append((idx, user_name, df_sub))
```

略

#### 3、将每个datafame存入excel

```python
for idx, user_name, df_sub in df_subs:
    file_name = f"{splits_dir}/crazyant_blog_articles_{idx}_{user_name}.xlsx"
    df_sub.to_excel(file_name, index=False)
```

略

### 2. 合并多个小Excel到一个大Excel

1. 遍历文件夹，得到要合并的Excel文件列表
2. 分别读取到dataframe，给每个df添加一列用于标记来源
3. 使用pd.concat进行df批量合并
4. 将合并后的dataframe输出到excel

#### 1. 遍历文件夹，得到要合并的Excel名称列表

```python
import os
excel_names = []
for excel_name in os.listdir(splits_dir):
    excel_names.append(excel_name)
excel_names
```

略

#### 2. 分别读取到dataframe

```python
df_list = []

for excel_name in excel_names:
    # 读取每个excel到df
    excel_path = f"{splits_dir}/{excel_name}"
    df_split = pd.read_excel(excel_path)
    # 得到username
    username = excel_name.replace("crazyant_blog_articles_", "").replace(".xlsx", "")[2:]
    print(excel_name, username)
    # 给每个df添加1列，即用户名字
    df_split["username"] = username
    
    df_list.append(df_split)
```

略

#### 3. 使用pd.concat进行合并

```python
df_merged = pd.concat(df_list)
df_merged.shape

df_merged.head()

df_merged["username"].value_counts()
```

![image-20231023165632311](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231656534.png)![image-20231023165654234](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231656457.png)

#### 4. 将合并后的dataframe输出到excel

```python
df_merged.to_excel(f"{work_dir}/crazyant_blog_articles_merged.xlsx", index=False)
```

略



## 十六. Pandas怎样实现groupby分组统计

类似SQL：
select city,max(temperature) from city_weather group by city;
给一个天气数据,按照城市分组,最后查询每个城市的最高温度.
即,先分组,然后再对每个分组进行统计

groupby：先对数据分组，然后在每个分组上应用聚合函数、转换函数

本次演示：
一、分组使用聚合函数做数据统计
二、遍历groupby的结果理解执行流程
三、实例分组探索天气数据  

```python
import pandas as pd
import numpy as np
# 加上这一句，能在jupyter notebook展示matplot图表
%matplotlib inline
```

```python
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
df
```

![image-20231023170027764](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231700971.png)

### 1. 分组使用聚合函数做数据统计

#### 1、单个列groupby，查询所有数据列的统计

```python
df.groupby('A').sum()
```

![image-20231023170145717](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231701982.png)

我们看到：
1. groupby中的'A'变成了数据的索引列
2. 因为要统计sum，但B列不是数字，所以被自动忽略掉

#### 2、多个列groupby，查询所有数据列的统计

```python
df.groupby(['A','B']).mean()
```

![image-20231023170233405](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231702690.png)

我们看到：('A','B')成对变成了二级索引

```python
df.groupby(['A','B'], as_index=False).mean()
```

![image-20231023170338033](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231703250.png)

#### 3、同时查看多种数据统计

```python
df.groupby('A').agg([np.sum, np.mean, np.std])
```

![image-20231023170409341](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231704543.png)

我们看到：列变成了多级索引

#### 4、查看单列的结果数据统计

```python
# 方法1：预过滤，性能更好
df.groupby('A')['C'].agg([np.sum, np.mean, np.std])

# 方法2
df.groupby('A').agg([np.sum, np.mean, np.std])['C']
```

![image-20231023170437143](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231704388.png)![image-20231023170452712](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231704928.png)

#### 5、不同列使用不同的聚合函数

```python
df.groupby('A').agg({"C":np.sum, "D":np.mean})
```

![image-20231023170512514](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231705711.png)

### 2. 遍历groupby的结果理解执行流程

for循环可以直接遍历每个group

##### 1、遍历单个列聚合的分组

```python
g = df.groupby('A')
g

for name,group in g:
    print(name)
    print(group)
    print()
```

![image-20231023170610291](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231706595.png)![image-20231023170624315](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231706533.png)

***可以获取单个分组的数据***

```python
g.get_group('bar')
```

![image-20231023171740717](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231717876.png)

##### 2、遍历多个列聚合的分组

```python
g = df.groupby(['A', 'B'])
for name,group in g:
    print(name)
    print(group)
    print()
```

![image-20231023171813423](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231718599.png)

可以看到，name是一个2个元素的tuple，代表不同的列

```python
g.get_group(('foo', 'one'))
```

![image-20231023171841828](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231718987.png)

***可以直接查询group后的某几列，生成Series或者子DataFrame***

```python
g['C']
for name, group in g['C']:
    print(name)
    print(group)
    print(type(group))
    print()
```

![image-20231023171947253](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231719403.png)![image-20231023172547730](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231725845.png)

其实所有的聚合统计，都是在dataframe和series上进行的；

### 3. 实例分组探索天气数据

```python
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
df.head()

# 新增一列为月份
df['month'] = df['ymd'].str[:7]
df.head()
```

![image-20231023172639544](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231726655.png)![image-20231023172658298](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231726449.png)

#### 1、查看每个月的最高温度

```python
data = df.groupby('month')['bWendu'].max()
data

type(data)

data.plot()
```

![image-20231023172725815](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231727949.png)![image-20231023172749412](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231727519.png)

#### 2、查看每个月的最高温度、最低温度、平均空气质量指数

```python
df.head()

group_data = df.groupby('month').agg({"bWendu":np.max, "yWendu":np.min, "aqi":np.mean})
group_data

group_data.plot()
```

![image-20231023173023075](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231730192.png)![image-20231023173056147](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231730269.png)



## 十七. Pandas的分层索引MultiIndex

为什么要学习分层索引MultiIndex？
* 分层索引：在一个轴向上拥有多个索引层级，可以表达更高维度数据的形式；
* 可以更方便的进行数据筛选，如果有序则性能更好；
* groupby等操作的结果，如果是多KEY，结果是分层索引，需要会使用
* 一般不需要自己创建分层索引(MultiIndex有构造函数但一般不用)

演示数据：百度、阿里巴巴、爱奇艺、京东四家公司的10天股票数据
数据来自：英为财经
https://cn.investing.com/

本次演示提纲： 
一、Series的分层索引MultiIndex
二、Series有多层索引怎样筛选数据？
三、DataFrame的多层索引MultiIndex
四、DataFrame有多层索引怎样筛选数据？

```python
import pandas as pd
%matplotlib inline
```

```python
stocks = pd.read_excel('./datas/stocks/互联网公司股票.xlsx')

stocks.head(3)

stocks["公司"].unique()

stocks.index

stocks.groupby('公司')["收盘"].mean()
```

![image-20231025090233258](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250902383.png)![image-20231025090425598](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250904699.png)![image-20231025090620730](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250906882.png)

### 1. Series的分层索引MultiIndex

```python
ser = stocks.groupby(['公司', '日期'])['收盘'].mean()
ser
# 多维索引中，空白的意思是：使用上面的值
ser.index

# unstack把二级索引变成列
ser.unstack()

ser

ser.reset_index()
```

![image-20231025090723870](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250907005.png)![image-20231025091012409](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250910571.png)![image-20231025091114627](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250911759.png)

![image-20231025091142929](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250911018.png)![image-20231025091156057](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250911158.png)

### 2. Series有多层索引MultiIndex怎样筛选数据？

```python
ser

ser.loc['BIDU']

# 多层索引，可以用元组的形式筛选
ser.loc[('BIDU', '2019-10-02')]

ser.loc[:, '2019-10-02']
```

![image-20231025091247186](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250912279.png)![image-20231025091316425](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250913514.png)![image-20231025091405846](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250914997.png)

### 3. DataFrame的多层索引MultiIndex

```python
stocks.head()

stocks.set_index(['公司', '日期'], inplace=True)
stocks

stocks.index

stocks.sort_index(inplace=True)
stocks
```

![image-20231025091506476](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250915572.png)![image-20231025091550280](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250915408.png)  ![image-20231025091623190](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250916345.png)![image-20231025091701179](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310250917465.png) 

### 4. DataFrame有多层索引MultiIndex怎样筛选数据？

***【重要知识】***在选择数据时： 

* 元组(key1,key2)代表筛选多层索引，其中key1是索引第一级，key2是第二级，比如key1=JD, key2=2019-10-02
* 列表[key1,key2]代表同一层的多个KEY，其中key1和key2是并列的同级索引，比如key1=JD, key2=BIDU

```python
# 传一个值,筛选第一层索引
stocks.loc['BIDU']

# 筛选多层索引,传入一个元组(, !所有列)
stocks.loc[('BIDU', '2019-10-02'), :]

# 单个列(返回单个单元格的值)
stocks.loc[('BIDU', '2019-10-02'), '开盘']

# 传入列表时,筛选同一级索引(并列筛选)
stocks.loc[['BIDU', 'JD'], :]

# 也可以在元组中嵌套列表
stocks.loc[(['BIDU', 'JD'], '2019-10-03'), :]

# 指定列
stocks.loc[(['BIDU', 'JD'], '2019-10-03'), '收盘']

# 二级索引换为列表
stocks.loc[('BIDU', ['2019-10-02', '2019-10-03']), '收盘']

# slice(None)代表筛选这一索引的所有内容
stocks.loc[(slice(None), ['2019-10-02', '2019-10-03']), :]

# 把所有索引变为普通的列
stocks.reset_index()
```

![image-20231025145852825](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251458003.png)

![image-20231025145918765](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251459872.png)

![image-20231025145934773](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251459878.png)

![image-20231025150003049](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251500242.png)

![image-20231025150023068](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251500187.png)

![image-20231025150040368](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251500472.png)

![image-20231025150105035](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251501152.png)

![image-20231025150135089](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251501241.png)

![image-20231025150210681](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251502837.png)



## 十八. Pandas的数据转换函数map、apply、applymap

数据转换函数对比：map、apply、applymap：
1. map：只用于Series，实现每个值->值的映射；
2. apply：用于Series实现每个值的处理，用于Dataframe实现某个轴的Series的处理；
3. applymap：只能用于DataFrame，用于处理该DataFrame的每个元素；

### 1. map用于Series值的转换

实例：将股票代码英文转换成中文名字

Series.map(dict) or Series.map(function)均可

```python
import pandas as pd
stocks = pd.read_excel('./datas/stocks/互联网公司股票.xlsx')
stocks.head()

stocks["公司"].unique()

# 公司股票代码到中文的映射，注意这里是小写
dict_company_names = {
    "bidu": "百度",
    "baba": "阿里巴巴",
    "iq": "爱奇艺", 
    "jd": "京东"
}
```

![image-20231025152322739](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251523927.png)

#### 方法1：Series.map(dict)

```python
stocks["公司中文1"] = stocks["公司"].str.lower().map(dict_company_names)
stocks.head()
```

![image-20231025152435511](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251524672.png)

#### 方法2：Series.map(function)

function的参数是Series的每个元素的值

```python
stocks["公司中文2"] = stocks["公司"].map(lambda x : dict_company_names[x.lower()])
stocks.head()
```

![image-20231025152508994](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251525176.png)

### 2. apply用于Series和DataFrame的转换

* Series.apply(function), 函数的参数是每个值
* DataFrame.apply(function), 函数的参数是Series

#### Series.apply(function)

function的参数是Series的每个值

```python
stocks["公司中文3"] = stocks["公司"].apply(
    lambda x : dict_company_names[x.lower()])
stocks.head()
```

![image-20231025152618592](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251526742.png)

#### DataFrame.apply(function)

function的参数是对应轴的Series

```python
stocks["公司中文4"] = stocks.apply(
    lambda x : dict_company_names[x["公司"].lower()], 
    axis=1)
stocks.head()
```

注意这个代码：
1、apply是在stocks这个DataFrame上调用；
2、lambda x的x是一个Series，因为指定了axis=1所以Seires的key是列名，可以用x['公司']获取

![image-20231025152926474](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251529631.png)

### 3. applymap用于DataFrame所有值的转换

```python
# 筛选这几列
sub_df = stocks[['收盘', '开盘', '高', '低', '交易量']]
sub_df.head()

# 将这些数字取整数，应用于所有元素
sub_df.applymap(lambda x : int(x))

# 直接修改原df的这几列
stocks.loc[:, ['收盘', '开盘', '高', '低', '交易量']] = sub_df.applymap(lambda x : int(x))
stocks.head()
```

![image-20231025153032029](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251530175.png)![image-20231025153201319](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251532468.png)

![image-20231025153301324](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251533523.png)



## 十九. Pandas怎样对每个分组应用apply函数?

#### 知识：Pandas的GroupBy遵从split、apply、combine模式

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231632929.png)

这里的split指的是pandas的groupby，我们自己实现apply函数，apply返回的结果由pandas进行combine得到结果

#### GroupBy.apply(function)  
* function的第一个参数是dataframe
* function的返回结果，可是dataframe、series、单个值，甚至和输入dataframe完全没关系

#### 本次实例演示：
1. 怎样对数值列按分组的归一化？
2. 怎样取每个分组的TOPN数据？

### 实例1：怎样对数值列按分组的归一化？

将不同范围的数值列进行归一化，映射到[0,1]区间：
* 更容易做数据横向对比，比如价格字段是几百到几千，增幅字段是0到100
* 机器学习模型学的更快性能更好

归一化的公式：

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231633034.jpeg)

#### 演示：用户对电影评分的归一化

每个用户的评分不同，有的乐观派评分高，有的悲观派评分低，按用户做归一化

```python
ratings = pd.read_csv(
    "./datas/movielens-1m/ratings.dat", 
    sep="::",
    engine='python', 
    names="UserID::MovieID::Rating::Timestamp".split("::")
)
ratings.head()

# 实现按照用户ID分组，然后对其中一列归一化
def ratings_norm(df):
    """
    @param df：每个用户分组的dataframe
    """
    min_value = df["Rating"].min()
    max_value = df["Rating"].max()
    df["Rating_norm"] = df["Rating"].apply(
        lambda x: (x-min_value)/(max_value-min_value))
    return df

ratings = ratings.groupby("UserID").apply(ratings_norm)

ratings[ratings["UserID"]==1].head()
```

![image-20231025153722092](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251537228.png)![image-20231025153833010](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251538170.png)

可以看到UserID==1这个用户，Rating==3是他的最低分，是个乐观派，我们归一化到0分；

### 实例2：怎样取每个分组的TOPN数据？

获取2018年每个月温度最高的2天数据

```python
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')
# 新增一列为月份
df['month'] = df['ymd'].str[:7]
df.head()

def getWenduTopN(df, topn):
    """
    这里的df，是每个月份分组group的df
    """
    return df.sort_values(by="bWendu")[["ymd", "bWendu"]][-topn:]

df.groupby("month").apply(getWenduTopN, topn=1).head()
```

![image-20231025154004197](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251540373.png)

![image-20231025162035528](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251620669.png)![image-20231025162055102](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251620238.png)

我们看到，grouby的apply函数返回的dataframe，其实和原来的dataframe其实可以完全不一样



## 二十. Pandas的stack和pivot实现数据透视

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231636787.png)

1. 经过统计得到多维度指标数据
2. 使用unstack实现数据二维透视
3. 使用pivot简化透视
4. stack、unstack、pivot的语法

###  1. 经过统计得到多维度指标数据

非常常见的统计场景，指定多个维度，计算聚合后的指标  

实例：统计得到“电影评分数据集”，每个月份的每个分数被评分多少次：（月份、分数1~5、次数）

```python
import pandas as pd
import numpy as np
%matplotlib inline
```

```python
df = pd.read_csv(
    "./datas/movielens-1m/ratings.dat",
    header=None,
    names="UserID::MovieID::Rating::Timestamp".split("::"),
    sep="::",
    engine="python"
)
df.head()

# 数据是以秒的形式给出,此处转换为标准时间格式
df["pdate"] = pd.to_datetime(df["Timestamp"], unit='s')
df.head()

#可以看到时间列为datatime格式,这样可以在后面直接读取月份
df.dtypes

# 实现数据统计
df_group = df.groupby([df["pdate"].dt.month, "Rating"])["UserID"].agg(pv=np.size)
df_group.head(20)
```

![image-20231025162447543](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251624653.png)![image-20231025162629539](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251626675.png)![image-20231025162736344](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251627510.png)

![image-20231025162949972](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251629103.png)

对这样格式的数据，我想查看按月份，不同评分的次数趋势(画图)，是没法实现的

需要将数据变换成每个评分是一列才可以实现

### 2. 使用unstack实现数据二维透视

目的：想要画图对比按照月份的不同评分的数量趋势

```python
df_stack = df_group.unstack()
df_stack

# 画图,略
df_stack.plot()

# unstack和stack是互逆操作
df_stack.stack().head(20)
```

![image-20231025163332666](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251633800.png)![image-20231025163536402](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251635528.png)

### 3. 使用pivot简化透视

```python
df_group.head(20)

df_reset = df_group.reset_index()
df_reset.head()

df_pivot = df_reset.pivot("pdate", "Rating", "pv")
df_pivot.head()

# 画图略
df_pivot.plot()
```

![image-20231025165004298](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251650416.png)![image-20231025165028725](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251650846.png)![image-20231025165934454](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251659613.png)



***pivot方法相当于对df使用set_index创建分层索引，然后调用unstack***

### 4. stack、unstack、pivot的语法

#### stack：

DataFrame.stack(level=-1, dropna=True)，将column变成index，类似把横放的书籍变成竖放

level=-1代表多层索引的最内层，可以通过==0、1、2指定多层索引的对应层

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231640411.png)

#### unstack：

DataFrame.unstack(level=-1, fill_value=None)，将index变成column，类似把竖放的书籍变成横放

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231640432.png)

#### pivot：

DataFrame.pivot(index=None, columns=None, values=None)，指定index、columns、values实现二维透视

![](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310231641914.png)

## Pandas使用apply函数给表格添加多列

![image-20231025170431120](https://gitee.com/fingerheart521/typora-image/raw/master/image/202310251704295.png)

## 针对python练习题最后一题的补充

```python
df.drop_duplicates(inplace=True)  # 删除重复项并修改原数据
df["pubdate"] = to_datatime(f["pubdate"]) # 将"pubdate"列转换为pandas时间序列

```



