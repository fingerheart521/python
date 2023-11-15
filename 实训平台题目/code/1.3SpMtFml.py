import math


def calculate_res(num):
    # 计算分子
    numerator = 3 ** 4 + 5 * 6 ** 5
    # 计算除法并取平方根
    res = math.sqrt(numerator / num)
    # 向上取整
    res = math.ceil(res)
    return res


# 测试函数
num = 5
print(calculate_res(num))
