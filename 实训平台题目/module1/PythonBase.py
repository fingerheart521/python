import re

'''
 re.IGNORECASE/re.I 区分大小写

re.match函数尝试从字符串的开头开始匹配一个模式，如果匹配成功，返回一个匹配成功的对象，否则返回None。

re.match(pattern, string, flags = 0)
pattern：匹配的正则表达式
string：要匹配的字符串
flags：标志位，用于控制正则表达式的匹配方式。如是否区分大小写、是否多行匹配等。

正则表达式常见的几种函数:

1. re.match()函数 如果想要从源字符串的起始位置匹配一个模式
2. re.search()函数 会扫描整个字符串并进行对应的匹配。
 该函数与re.match()函数最大的不同是，re.match()函数从源字符串的开头进行匹配，而re.search()函数会在全文中进行检索匹配。
3. re.compile()  在以上两个函数中，即便源字符串中有多个结果符合模式，也只会匹配一个结果，那么我们如何将符合模式的内容全部都匹配出来呢？
string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.")#预编译
result = pattern.findall(string)#找出符合模式的所有结果
4. re.sub(pattern,rep,string,max) 如果，想根据正则表达式来实现替换某些字符串的功能，我们可以使用re.sub()函数来实现。
'''
site = input()
match = re.match(r'https://www',site, flags = re.I)
print(match)
result = match.span()
print(result)