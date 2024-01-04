# python基础

基于牛客网python入门整理,数据均使用input()函数输入

[牛客网在线编程 python入门](https://www.nowcoder.com/exam/oj?page=1&tab=Python篇&topicId=314)



## 输入输出

### 强制保留两位小数

```python
print("{:.2f}".format(float(input())))
```



## 类型转换

### 强制转换输入的小数为整数

```python
print(int(float(input())))  # 此处int()函数无法强制转换无法变为整数的数据,需先转换为浮点数
```

### 十六进制强制转换为十进制

```python
print(int(input(), 16))
```



## 字符串

### 单词的大小写转换

```python
name = input()
print(name.lower())
print(name.upper())
print(name.title())
```

### 去除单词两边的空白字符

```python
name = input()
print(name.strip())
```



## 列表

```python
nums = [int(i) for i in input().split()]
```

### 输出列表为字符串

```python
lst = ['apple', 'banana', 'cherry', 'orange']
x = '-'.join(lst)
print(x)
```

### 长字符串的分割

```python
print(input().split())  # 默认空格为分隔符
```

### 列表的修改

.append()

```python
list0 = input().split()
list0.append("Allen")  # 在列表的末尾添加
print(list0)
```

.insert()

```python
list0 = input().split()
list0.insert(0, "Allen")  # 在指定的下标处添加
print(list0)
```

del函数  **根据索引(元素所在位置)来删除**

```python
list0 = input().split()
del list0[0]  # 删除指定下标的元素
print(list0)

del list0[2:3]  # 删除范围内的值(含前不含后)
del list0  # 删除整个数据对象
```

.remove()  **删除单个元素，删除首个符合条件的元素，按值删除**

```python
list0 = input().split()
list0.remove(input())  # 删除指定的元素
print(list0)
```

.pop()  **删除单个或多个元素，按位删除(根据索引删除)**

```python
list0 = input().split(" ")
list0.pop(-1)  # 删除最后一个
list0.pop(0)  # 删除第一个
print(list0)
```



### 列表的排序

```python
my_list = ["P", "y", "t", "h", "o", "n"]
print(sorted(my_list))  # sorted()用于所有的可排序变量,使用时输出新列表
print(my_list)
my_list.sort(reverse=True)  # .sort()仅用于列表,使用时直接修改原列表
print(my_list)
```

```python
num = [3, 5, 9, 0, 1, 9, 0, 3]
num.reverse()  # 对整个列表反转,使用时直接修改原列表
print(num)

num = num[::-1]  # 也可以使用切片的方法进行反转
print(num)
```



### 列表内部的操作

```python
num = list(input())
temp = []
for i in num:
    temp.append((int(i)+3)%9)  # 将输入的四位数每一位进行操作
print(f"{temp[2]}{temp[3]}{temp[0]}{temp[1]}")  # 更改其输出顺序及转换为字符串类型

```



## 运算符

[Python基础语法入门——运算符 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/630652223)

### "/"与"//"

```python
x = int(input())
y = int(input())
print(int(x//y),int(x%y))
print("{:.2f}".format(x/y))
# “/”表示浮点数除法，返回浮点结果，而“//”在Python中表示整数除法，返回不大于结果的一个最大的整数，意思就是除法结果向下取整.
```



### 逻辑运算符

**逻辑与（and）定义：**
如果x为（零或空字符串或空元组或空列表或空字典或者False），x and y 返回 x（零或空字符串或空元组或空列表或空字典或者False），否则它返回 y 的计算值。
**逻辑或（or）定义：**
如果x不为（零或空字符串或空元组或空列表或空字典或者False），x or y 返回 x 的计算值，否则它返回 y 的计算值。
**逻辑非/取反（not）定义：**
如果 x 不为（零或空字符串或空元组或空列表或空字典），则返回 False 。否则，它返回 True。

[python 或 与 非 python中的与或非_mob6454cc65110a的技术博客_51CTO博客](https://blog.51cto.com/u_16099190/6880048)

```python
nums = input().split()
print(int(nums[0]) and int(nums[1]))  # 与
print(int(nums[0]) or int(nums[1]))  # 或
print(not int(nums[0]))  # 非
print(not int(nums[1]))
```

| 运算符 | 描述 | 示例    |
| ------ | ---- | ------- |
| and    | 与   | x and y |
| or     | 或   | x or y  |
| not    | 非   | not x   |



### 位运算符

```python
x, y = input().split()
x, y = int(x), int(y)
print(x & y)
print(x | y)
```

| 运算符 | 描述     | 示例   |
| ------ | -------- | ------ |
| &      | 按位与   | x & y  |
| \|     | 按位或   | x \| y |
| ^      | 按位异或 | x ^ y  |
| ~      | 按位取反 | ~x     |
| <<     | 左移     | x << y |
| >>     | 右移     | x >> y |





## 字典

### 字典的取出与添加

```python
operators_dict = {'<': 'less than.', '==': 'equal.'}
print('Here is the original dict:')
for key,value in sorted(operators_dict.items()):
    print(f"Operator {key} means {value}")

operators_dict[">"] = 'greater than.'
print()
print('The dict was changed to:')
for key,value in sorted(operators_dict.items()):
    print(f"Operator {key} means {value}")
```



### 取出字典所有的键

```python
survey_list = ['Niumei', 'Niu Ke Le', 'GURR', 'LOLO']
result_dict = {'Niumei': 'Nowcoder', 'GURR': 'HUAWEI'}
for i in survey_list:
    if i in result_dict.keys():
        print(f'Hi, {i}! Thank you for participating in our graduation survey!')
    else:
        print(f'Hi, {i}! Could you take part in our graduation survey?')
```



### 字典的嵌套

```python
cities_dict = {'Beijing': {'Capital': 'China'}, 'Moscow': {'Capital': 'Russia'}, 'Paris': {'Capital': 'France'}}
for i in sorted(cities_dict.keys()):
    print(f"{i} is the capital of {cities_dict[i]['Capital']}!")
```



```python
result_dict = {'Allen': ['red', 'blue', 'yellow'], 'Tom': ['green', 'white', 'blue'], 'Andy': ['black', 'pink']}

for i in sorted(result_dict.keys()):
    print(f"{i}'s favorite colors are:")
    for j in result_dict[i]:
        print(j)
```



###  利用字典计数

```python
txt = """NiuNiulikesNiuMeiButNiumeidontknow"""  # 此处为输入文本(字符串)

world_list = list(txt)
dict0 = {}
for i in world_list:
    if i in dict0:
        continue
    dict0[i] = world_list.count(i)
print(dict0)

# 输出
# {'N': 4, 'i': 7, 'u': 5, 'l': 1, 'k': 2, 'e': 3, 's': 1, 'M': 1, 'B': 1, 't': 2, 'm': 1, 'd': 1, 'o': 2, 'n': 2, 'w': 1}
```



## 内置函数

### 求和

```python
nums = [int(i) for i in input().split()]
print(sum(nums))
```

### 绝对值

```python
print(abs(int(input())))
```

### 转ASCII码

```python
print(ord(input()))
```

### 转十六进制

```python
print(hex(int(input())))
```

### 转二进制

```python
print(bin(int(input())))
```

### 幂运算

```python
list0 = [int(i) for i in input().split()]
print(list0[0] ** list0[1])
print(pow(list0[1] , list0[0]))
```

### 统计

统计字符子串在字符串中出现了多少次

```python
num=[int(i) for i in input().split()]
print(num.count(0))

str0 = input()
print(str0.count("Niu"))
```

### 查找列表中第一个下标

```python
names = list(input().split())
print(names.index("NiuNiu"))
```

### 字符串内容判断

isalpha、isdigit、isspace可以分别判断字符串是否只包含字母、数字、空格.

```python
world = input()
if world.isalpha():
    print(True)
else:
    print(False)
if world.isdigit():
    print(True)
else:
    print(False)
if world.isspace():
    print(True)
else:
    print(False)
```

### 查找

```python
strs = input()
print(strs.find("NiuNiu"))
```

### 字符串拆分

```python
print(list(input().split()))
```

### 单词造句

```python
list0 = []
while True:
    str0 = input()
    if str0 == "0":
        break
    list0.append(str0)
print(" ".join(list0))
```

### 替换

```python
str0 = input()
print(str0.replace("a*", "ab"))
```

### 保留小数

```python
print(round(float(input()), 2))
```

### 直接计算公式

```python
print(eval(input()))  # 直接计算输入的字符串
```

### 去除重复(集合)

```python
list0 = list(input().split())
print(sorted(set(list0)))  # 转换为集合并排序
```



## 面向对象

### 简单函数

```python
def cal(x, y):
    return int(x) - int(y)

x = input()
y = input()
print(cal(x,y))
print(cal(y,x))
```



### f(n)=f(n-1)+f(n-2)

```python
def f(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return f(n-1) + f(n-2)

n = int(input())
print(f(n))
```



### *V*=4\*π\*r**2

```python
import math

rs = [1, 2, 4, 9, 10, 13]

for i in rs:
    print(round(4 * math.pi * (i ** 2),2))
```



### 简单的类

```python
class Student:
    name = input()
    num = input()
    grade = int(input())
    grade_list = list(input().split())
    print(f"{name}'s student number is {num}, and his grade is {grade}. He submitted {len(grade_list)} assignments, each with a grade of {' '.join(grade_list)}")
```

```python
class Student:
    def __init__(self, name, stu_num, score, grade):
        self.name = name
        self.stu_num = stu_num
        self.score = score
        self.grade = grade
    #__str__方法用于返回对象的描述信息，如果不使用__str__方法，直接print，或者return，返回的是对象的内存地址。
    def __str__(self): 
        return ("%s's student number is %s, and his grade is %d. He submitted %s assignments, each with a grade of %s"
                % (self.name, self.stu_num, int(self.score), len(self.grade.split()), self.grade))

name1 = input()
stu_num1 = input()
score1 = input()
grade1 = input()
stu = Student(name1, stu_num1, score1, grade1)
print(stu)
```



```python
class Student:
    def __init__(self, name, num, score, grade):
        self.name = name
        self.num = num
        self.score = score
        self.grade = grade

    def info(self):

        print(
            f"{self.name}'s student number is {self.num}, and his grade is {self.score}. He submitted {len(self.grade)} assignments, each with a grade of {' '.join(self.grade)}"
        )

name = input()
num = input()
score = int(input())
grade = input().split()
stu = Student(name, num, score, grade)
stu.info()
```







### try...except...

```python
# 此代码会报错,属正常情况

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printclass(self):
        try:
            print(f"{self.name}'salary is {self.salary}, and his age is {self.age}")
        except:
            print("Error! No age")

e = Employee(input(), input())
e.printclass()
e.age = input()
e.printclass()
```



### hasattr方法与setattr方法

```python
# 此代码会报错,属正常情况

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def printclass(self):
        print(f"{self.name}'salary is {self.salary}, and his age is {self.age}")

name = input()
salary = input()
age = input()

z = Employee(name, salary)
if print(hasattr(z, age)):
    z.printclass()

else:
    setattr(z, "age", age)
    z.printclass()
```



### 重载运算符

请创建一个Coordinate类表示坐标系，属性有x和y表示横纵坐标，并为其创建初始化方法\__init__。

请重载方法\__str__为输出坐标'(x, y)'。

请重载方法\__add__，更改Coordinate类的相加运算为横坐标与横坐标相加，纵坐标与纵坐标相加，返回结果也是Coordinate类。

现在输入两组横纵坐标x和y，请将其初始化为两个Coordinate类的实例c1和c2，并将坐标相加后输出结果。

#### 输入描述：

第一行输入两个整数x1与y1，以空格间隔。

第二行输入两个整数x2与y2，以空格间隔。

#### 输出描述：

输出相加后的坐标。

```python
class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # 把一个类的实例变成 str
        return f"({self.x}, {self.y})"

    def __add__(self, other):  # 修改类的+运算
        return Coordinate(self.x + other.x, self.y + other.y)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
c1 = Coordinate(x1, y1)
c2 = Coordinate(x2, y2)
print(c1 + c2)

```



## 正则表达式

### 查找网址

```python
import re

http = input()
result=re.match(r'https://www', http).span()
print(result)
```

### 提取数字(删除其他)

```python
import re

num = input()
print(re.sub(r"[^\d]", "", num))
```

### 提取数字(直接提取)

```python
import re

num = input()
print(re.match(r"[\d|-]*", num).group())
```

docker run -d --name of openfrp/frpc:latest -u 621421502e33e180e265f6a867125bac -p 402460
