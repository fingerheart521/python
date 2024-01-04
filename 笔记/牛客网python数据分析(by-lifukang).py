import pandas as pd


# 设置字体显示宽度，最大行
pd.set_option("display.width", 300)  # 设置字符显示宽度
pd.set_option("display.max_rows", None)  # 设置显示最大行
pd.set_option("display.max_columns", None)



# 参数
# subset： 列标签
# keep： {‘first’, ‘last’, False}, 默认值 ‘first’
# first： 保留第一次出现的重复项。
# last： 删除重复项，仅保留最后一次出现的重复项
# False： 删除所有重复项
# inplace：布尔值，默认为False，是否删除重复项或返回副本


# DataFrame.duplicated(subset=None, keep='first')
#
# 返回 bool series 表示每行是否是重复的
#
# subset：column 标签
# keep：
# first，默认，标记除第一次出现以外的重复项为 True
# last，标记除最后一次出现以外的重复项为 True
# False，标记所有重复出现的为 True
# DataFrame.drop_duplicates(subset=None, *, keep='first', inplace=False, ignore_index=False)
#
# 返回删除重复项后的 dataframe
#
# subset，与 duplicated 中的 subset 参数含义相同
# keep，与 duplicted 中的 subset 参数相同，first 则表示只保留第一次出现的 item
# inplace，是否原地修改
# ignore_index，如果为 True，则去重后的 index 重置为 0,1，...，n-1



# 描述
# 现有一个Nowcoder.csv文件，它记录了牛客网的部分用户数据，包含如下字段（字段与字段之间以逗号间隔）：
# Nowcoder_ID：用户ID
# Level：等级
# Achievement_value：成就值
# Num_of_exercise：刷题量
# Graduate_year：毕业年份
# Language：常用语言
# Continuous_check_in_days：最近连续签到天数
# Number_of_submissions：提交代码次数
# Last_submission_time：最后一次提交题目日期
# 运营同学发现最后一次提交题目日期这一列有各种各样的日期格式，这对于他分析用户十分不友好，你能够帮他输出用户ID、等级以及统一后的日期吗？（日期格式统一为yyyy-mm-dd）
df=pd.read_csv('Nowcoder.csv',sep=',',dtype=object)
df['Last_submission_time']=pd.to_datetime(df['Last_submission_time'],format='%Y-%m-%d')
print(df[['Nowcoder_ID','Level','Last_submission_time']])



# 题目描述：
# 现有某店铺会员消费情况sales.csv。包含以下字段：
#
# user_id：会员编号；
# recency：最近一次消费距离当天的天数；
# frequency：一段时间内消费的次数；
# monetary：一段时间内消费的总金额。
# 请你分别对每个用户的每个消费特征进行评分。
#
# 输入描述：
# 数据集可以从当前目录下sales.csv读取。
#
# 输出描述：
# 请你对每个用户销售情况的每个特征进行评分，分值为1-4分。对于recency特征，值越小越好。对于frequency和monetary值越大越好。请分别将对应的数据进行四等分并评分，如对于recency：
#
# 数值小于等于下四分位数则评为4分；
# 大于下四分位数并且小于等于中位数则评为3分；
# 大于中位数且小于等于上四分位数则评为2分；
# 大于上四分位数则评为1分。
# 对于frequency和monetary则方法刚好相反。
#
# 要求给所有数据进行评分，并输出前5行。以上数据的输出结果如下：

data = pd.read_csv('sales.csv')

data['R_Quartile'] = pd.qcut(data['recency'], [0, 0.25, 0.5, 0.75, 1], ['4', '3', '2', '1']).astype("int")
data['F_Quartile'] = pd.qcut(data['frequency'], [0, 0.25, 0.5, 0.75, 1], ['1', '2', '3', '4']).astype("int")
data['M_Quartile'] = pd.qcut(data['monetary'], [0, 0.25, 0.5, 0.75, 1], ['1', '2', '3', '4']).astype("int")

print(data.head())


sales = pd.read_csv('sales.csv')

# 按照结果要求转换类型
sales[['monetary']] = sales[['monetary']].astype('float32')
# 求百分位
des = sales[['recency', 'frequency', 'monetary']].describe().loc['25%':'75%']

# 计算RFM
sales['R_Quartile'] = sales['recency'].apply(
    lambda x: 4 if x <= des.iloc[0, 0] else (3 if x <= des.iloc[1, 0] else (2 if x <= des.iloc[2, 0] else 1)))
sales['F_Quartile'] = sales['frequency'].apply(
    lambda x: 1 if x <= des.iloc[0, 1] else (2 if x <= des.iloc[1, 1] else (3 if x <= des.iloc[2, 1] else 4)))
sales['M_Quartile'] = sales['monetary'].apply(
    lambda x: 1 if x <= des.iloc[0, 2] else (2 if x <= des.iloc[1, 2] else (3 if x <= des.iloc[2, 2] else 4)))

#
print(sales.head())


# apply() 是 pandas 中非常有用的函数之一，可以将一个函数应用于每个元素、行或列，并返回新的序列或数据框。它可以接受多种类型的函数，包括：
#
# 一元函数：作用在每个单独的元素上。
# 矢量化函数：作用在整个序列上。
# 自定义函数：使用者自己编写的函数。
# apply() 的基本语法如下：

# result = df.apply(func, axis=0)
# 其中：
#
# df：需要处理的数据框。
# func：需要应用的函数。
# axis：指定应用函数的方向，0 表示列方向，1 表示行方向。
# 对于一元函数，apply() 将遍历数据框中的每个元素，并将其作为参数传递给函数。例如，如果我们想将所有元素转换为字符串，可以使用以下代码：



df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

def to_str(x):
    return str(x)

result = df.apply(to_str)
print(result)

# 运行结果如下：
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6
# 对于矢量化函数，apply() 将整个序列作为参数传递给函数。例如，如果我们想计算每列的平均值，可以使用以下代码：

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

def mean(x):
    return x.mean()

result = df.apply(mean)
print(result)

# 运行结果如下：
# A    2
# B    2
# dtype: int64

# qcut() 是 pandas 中的一个函数，用于将连续的数值数据分成离散的区间，即进行分位数分析。它可以根据指定的分位数或样本分位数将数据分成多个等频的区间。
#
# qcut() 的基本语法如下：

# pd.qcut(x, q, labels=None, retbins=False, precision=3, duplicates='raise')

# 其中，常用参数的含义如下：
#
# x: 需要进行分位数分析的数据，可以是一个一维数组、Series 或 DataFrame 的列。
# q: 指定分位数的数量或详细的分位数列表。
# labels: 对分位数区间进行自定义标签。
# retbins: 是否返回分位数的边界值。
# precision: 指定边界值的精度。
# duplicates: 当出现重复值时的处理方式，默认为 'raise'，即抛出异常。
# 下面是一个示例，展示了如何使用 qcut() 函数：

# 其中，常用参数的含义如下：
#
# x: 需要进行分位数分析的数据，可以是一个一维数组、Series 或 DataFrame 的列。
# q: 指定分位数的数量或详细的分位数列表。
# labels: 对分位数区间进行自定义标签。
# retbins: 是否返回分位数的边界值。
# precision: 指定边界值的精度。
# duplicates: 当出现重复值时的处理方式，默认为 'raise'，即抛出异常。
# 下面是一个示例，展示了如何使用 qcut() 函数：

# 运行结果可能类似于：

# [(0.0325, 0.721], (-2.8459999999999996, -0.731], (-2.8459999999999996, -0.731], (0.0325, 0.721], ..., (-0.731, 0.0325], (0.0325, 0.721], (-2.8459999999999996, -0.731], (-2.8459999999999996, -0.731]]
# Length: 100
# Categories (4, interval[float64]): [(-2.8459999999999996, -0.731] < (-0.731, 0.0325] < (0.0325, 0.721] < (0.721, 2.804]]

# 在 Pandas 中，groupby 是一种用于分组数据的功能。它可以根据指定的一列或多列对数据进行分组，并且可以对每个分组执行聚合操作或其他操作。
#
# 下面是一些 groupby 的常见用法和作用：


# 分组并应用聚合函数：
# 对特定列进行分组，并计算每个分组的平均值
df.groupby('column')['column_to_aggregate'].mean()

# 对多列进行分组，并计算每个分组的总和
df.groupby(['column1', 'column2'])['column_to_aggregate'].sum()
# 按照多列进行分组：
# 按照多列进行分组，并计算每个分组的平均值
df.groupby(['column1', 'column2'])['column_to_aggregate'].mean()

# 遍历分组：
# 遍历每个分组及其对应的数据
for group, data in df.groupby('column'):
    pass
    # 执行相应操作
# 应用多个聚合函数：
# 对每个分组同时计算多个聚合函数
df.groupby('column')['column_to_aggregate'].agg(['mean', 'sum', 'max'])
# 选择特定分组的数据：
# 获取特定分组的数据
df.groupby('column').get_group('group_value')

# 在 Python 中，self 是一个指向当前对象的引用，通常作为第一个参数传递给类中的方法。通过 self 参数，可以在方法内部访问和操作对象的属性和方法。
#
# 在 Python 中，所有方法（包括构造函数）的第一个参数默认都是 self。这个参数不需要手动传递，Python 会自动将当前对象的引用传递给它。通过 self，可以在方法内部访问当前对象的属性和方法，并对它们进行操作。例如：
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)
# 在这个例子中，__init__ 方法用于初始化新创建的对象，并将 value 属性设置为传入的值。在 print_value 方法中，使用 self.value 访问和打印当前对象的 value 属性。
#
# 此外，self 也可以用来调用当前对象的其他方法。例如：
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

    def double_value(self):
        self.value *= 2
        self.print_value()   # 调用 print_value 方法打印当前 value 属性的值
# double_value 方法将当前对象的 value 属性乘以 2，并通过 self.print_value() 调用 print_value 方法打印当前的值。

# 在Python中，sort()是列表对象的一个方法，用于对列表进行就地排序（即在原列表上进行修改）。
#
# 以下是sort()方法的常见用法：
#
# 对列表进行升序排序：
my_list = [3, 1, 4, 2, 5]
my_list.sort()
print(my_list)
# 输出结果为：[1, 2, 3, 4, 5]
#
# 在这个例子中，我们创建了一个包含5个整数的列表my_list。然后，我们调用sort()方法对列表进行升序排序。排序后，原列表my_list被修改为升序排列的结果。
#
# 对列表进行降序排序：
my_list = [3, 1, 4, 2, 5]
my_list.sort(reverse=True)
print(my_list)
# 输出结果为：[5, 4, 3, 2, 1]
#
# 在这个例子中，我们同样创建了一个包含5个整数的列表my_list。然后，我们调用sort()方法，并传递参数reverse=True，以实现对列表的降序排序。
#
# 需要注意的是，sort()方法会直接修改原列表，而不会创建新的排序后的列表。如果你希望保留原列表的副本并进行排序，可以使用sorted()函数，它返回一个新的已排序列表，而不会修改原列表。

my_list = [3, 1, 4, 2, 5]
sorted_list = sorted(my_list)
print(sorted_list)
# 输出结果为：[1, 2, 3, 4, 5]

# 在Python中，可以使用input()函数接受用户输入的十六进制数。默认情况下，input()函数接受的是字符串类型的输入。
#
# 以下是一个示例，演示如何接受用户输入的十六进制数并进行处理：
hex_str = input("请输入一个十六进制数: ")
decimal_num = int(hex_str, 16)
print("转换后的十进制数为:", decimal_num)

# 在Python中，可以使用int()函数将十六进制字符串转换为十进制整数。int()函数的第一个参数是要转换的字符串，第二个参数是指定输入字符串的进制（默认为10进制）。
#
# 以下是将十六进制字符串转换为十进制整数的示例：

hex_str = "1A"
decimal_num = int(hex_str, 16)
print(decimal_num)

# 在 Pandas 中，sort_values() 是一个用于对 DataFrame 或 Series 进行排序的函数。它可以按照指定的列或行的值进行升序或降序排列。
#
# 具体来说，sort_values() 函数有以下参数：
#
# by：指定按哪些列或行进行排序，可以是单个列/行名称或者多个列/行名称的列表。
# axis：指定按行（axis=0）还是按列（axis=1）进行排序，默认为按行排序。
# ascending：指定升序（True）或降序（False）排序，默认为升序排序。
# inplace：指定是否在原 DataFrame 或 Series 上进行排序，如果为 True，则会直接修改原对象，否则返回一个新对象。
import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 20, 30, 35],
        'height': [165, 170, 175, 180]}
df = pd.DataFrame(data)
# 按照年龄进行升序排序：
df.sort_values(by='age', ascending=True)
# 输出结果为：
#        name  age  height
# 1       Bob   20     170
# 0     Alice   25     165
# 2   Charlie   30     175
# 3     David   35     180

# 也可以按照身高进行降序排序：
df.sort_values(by='height', ascending=False)
# 输出结果为：

#        name  age  height
# 3     David   35     180
# 2   Charlie   30     175
# 1       Bob   20     170
# 0     Alice   25     165

# 在Pandas库中，merge函数用于将两个DataFrame对象按照指定的列（或索引）进行合并。它类似于SQL中的JOIN操作，可以根据共同的列将两个数据集连接起来。
#
# merge函数的基本语法如下：

# merged_df = pd.merge(left, right, on=None, how='inner')
# 其中，left和right是要合并的两个DataFrame对象，on是指定用于合并的列名（或多个列名），how是指定合并方式的参数。
#
# 下面是一些常见的合并方式（即how参数的取值）：
#
# 'inner'：内连接，只保留两个DataFrame中共同的行。
# 'outer'：外连接，保留两个DataFrame中的所有行，并在缺失值处填充NaN。
# 'left'：左连接，保留左侧DataFrame中的所有行，并在右侧DataFrame中没有匹配的行处填充NaN。
# 'right'：右连接，保留右侧DataFrame中的所有行，并在左侧DataFrame中没有匹配的行处填充NaN。
# 除了这些常见的合并方式，还可以通过indicator参数来查看每个合并行的来源。
#
# 以下是一个示例，演示如何使用merge函数合并两个DataFrame：

import pandas as pd

# 创建两个示例DataFrame
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
df2 = pd.DataFrame({'A': [3, 4, 5], 'C': ['x', 'y', 'z']})

# 使用merge函数进行内连接
merged_df = pd.merge(df1, df2, on='A', how='inner')
print(merged_df)

# 输出结果为：
#    A  B  C
# 0  3  c  x

# 在 Pandas 中，query() 是一种用于筛选 DataFrame 的函数。它可以通过使用类似 SQL 的语法来筛选满足特定条件的行。
#
# query() 函数的语法如下：
df.query('condition')
# 其中，df 是要进行筛选的 DataFrame，condition 是一个字符串，表示筛选的条件。条件字符串中可以使用 DataFrame 中的列名、运算符和常量等。
#
# 以下是一个示例代码，展示了如何使用 query() 函数筛选 DataFrame：


# 创建示例数据
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'gender': ['F', 'M', 'M', 'M']}
df = pd.DataFrame(data)

# 使用 query() 函数筛选数据
result = df.query('age > 30 and gender == "M"')
print(result)

# 输出结果将会是：

#      name  age gender
# 2  Charlie   35      M
# 3    David   40      M
# 在条件字符串中，如果要引用 DataFrame 中的列名，需要使用反引号（`）将列名括起来。
result = df.query('`age` > 30 and `gender` == "M"')

# 在 Pandas 中，您可以使用quantile()函数来计算四分之一位数。四分之一位数也称为下四分位数，是将数据集分为四个部分的一个值，位于数据的 25% 处。

# 创建示例数据
data = {'col1': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# 计算四分之一位数
q1 = df['col1'].quantile(0.25)
print(q1)

# 其中，quantile()函数的参数为要计算的分位数，例如 0.25 表示计算四分之一位数。
#
# 如果您希望同时计算多个分位数，可以将分位数作为列表传递给quantile()函数，如下所示：

# 计算四分之一位数和四分之三位数
q1, q3 = df['col1'].quantile([0.25, 0.75])
print(q1, q3)

# 想查看一列中有多少种不同的元素（而不是每个元素出现的次数），可以使用nunique()方法。该方法返回该列中不同元素的数量

# 创建一个DataFrame
data = {'Category': ['A', 'B', 'A', 'A', 'B', 'C']}
df = pd.DataFrame(data)

# 使用nunique()方法查看不同元素的数量
unique_count = df['Category'].nunique()
print(unique_count)

# 要查看一类（列）中有多少元素，可以使用value_counts()方法。这个方法返回一个包含不同元素及其对应计数的Series对象。

# 创建一个DataFrame
data = {'Category': ['A', 'B', 'A', 'A', 'B', 'C']}
df = pd.DataFrame(data)

# 使用value_counts()方法查看元素计数
counts = df['Category'].value_counts()
print(counts)

# 输出结果将显示每个元素及其对应的计数，例如：

# A    3
# B    2
# C    1
# Name: Category, dtype: int64

# 描述
# 题目描述
# 某公司计划举办一场运动会，现有部分运动会项目数据集items.csv。 包含以下字段：
#
# item_id：项目编号；
# item_name:项目名称；
# location:比赛场地。
# 有员工报名情况数据集signup.csv。包含以下字段：
#
# employee_id：员工编号；
# name：员工姓名；
# sex：性别；
# department：所属部门；
# item_id：报名项目id。
# 另有signup1.csv，是education部门的报名情况，包含字段同signup.csv。
#
# 请你将signup.csv与signup1.csv的数据集合并后，统计各类型项目的报名人数。
#
# 输入描述：
# 数据集可以从当前目录下items.csv、signup.csv、signup1.csv读取。
# items.csv

signup = pd.read_csv("signup.csv")
signup1 = pd.read_csv("signup1.csv")
items = pd.read_csv("items.csv")

# 级联员工表
signup2 = pd.concat([signup, signup1], axis=0)
# 合并
data = pd.merge(items, signup2, on="item_id", how="inner")
cnt = data.groupby(by="item_name")["item_name"].count()

#
print(cnt)

# 题目描述
# 某公司计划举办一场运动会，现有运动会项目数据集items.csv。 包含以下字段：
#
# item_id：项目编号；
# item_name:项目名称；
# location:比赛场地。
# 有员工报名情况数据集signup.csv。包含以下字段：
#
# employee_id：员工编号；
# name：员工姓名；
# sex：性别；
# department：所属部门；
# item_id：报名项目id
# 请你统计职能部门（functional）中报名标枪(javenlin)的所有员工的员工编号（employee_id）、姓名（name）及性别（sex）。
#
# 输入描述：
# 数据集可以从当前目录下items.csv、signup.csv读取。

# 导入Pandas库
import pandas as pd

# 读取items.csv文件
items = pd.read_csv("items.csv")

# 读取signup.csv文件
signup = pd.read_csv("signup.csv")

# 过滤item_name为javelin的项目
javelin = items[items["item_name"] == "javelin"]

# 选取职能部门functional
functional = signup[signup["department"] == "functional"]

# 合并functional和javelin,以关联employee_id
result = pd.merge(functional, javelin, on="item_id")

# 选择employee_id、name和sex三列
result = result[["employee_id", "name", "sex"]]
# 打印最终结果
print(result)

# 题目描述
# 某公司计划举办一场运动会，现有运动会项目数据集items.csv。 包含以下字段：
#
# item_id：项目编号；
# item_name:项目名称；
# location:比赛场地。
# 有员工报名情况数据集signup.csv。包含以下字段：
#
# employee_id：员工编号；
# name：员工姓名；
# sex：性别；
# department：所属部门；
# item_id：报名项目id
# 请你输出报名的各个项目情况（不包含没人报名的项目）对应的透视表。
#
# 输入描述：
# 数据集可以从当前目录下items.csv、signup.csv读取。
# items.csv

import pandas as pd

items = pd.read_csv('items.csv')
signup = pd.read_csv('signup.csv')

# 合并
data = pd.merge(items, signup)
# 透视表
result = data.pivot_table(
    ['employee_id'],  # 列表形式会作为列名输出到结果
    index=['sex', 'department'],
    columns='item_name',
    aggfunc='count',
    fill_value=0  # 对空的组合，填充值为0
)

print(result)


































































