# 字典先按照值降序排序，值相同再按照键升序排序，但是小写字母在前，大写字母在后。
# 示例字典
your_dict = {
    'a': 5,
    'B': 3,
    'c': 5,
    'D': 2,
    'E': 3,
    'f': 2,
}


# 自定义排序关键字函数
def sort_key(item):
    print(item[0],item[1])
    key, value = item
    return -item[1], (not item[0].islower(), item[0])


# 使用sorted函数排序字典项
sorted_items = sorted(your_dict.items(), key=sort_key)
print(sorted_items)

# 重新构建排序后的字典
sorted_dict = {key: value for key, value in sorted_items}

# 输出排序后的字典
print(sorted_dict)
