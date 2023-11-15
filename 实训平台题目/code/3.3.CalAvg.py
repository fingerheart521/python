'''
任务详情
给定一个DataFrame对象 df，要求返回各行的平均值。
具体操作如下：
添加新列 'avg' 用于计算各行的平均值；
使用数组返回新列 'avg'。

任务要求
程序接收 DataFrame 对象 df，返回结果是 list 数据类型；
注意：平均值需要四舍五入保留两位小数。
'''
import pandas as pd


class Solution:

    def CalAvgMine(self, df: 'pandas.DataFrame') -> list:
        # 添加新列 'avg' 用于计算各行的平均值
        df['avg'] = df.apply(lambda row: round(row.mean(), 2), axis=1)
        # 返回新列 'avg' 的值
        return df['avg'].tolist()

    def CalAvg(self, df: 'pandas.DataFrame') -> list:
        # 创建新列‘avg’，调用 mean 方法，传入参数axis = 1，使新列的值为每行的平均值，且保留两位小数
        df['avg'] = df.mean(axis=1).round(2)
        # 返回列‘avg’,并转变数据类型为 list
        return list(df['avg'])


df = pd.DataFrame({'0': [10, 9, 30, 21, 1],
                   '1': [19, 5, 27, 14, 25],
                   '2': [4, 28, 1, 19, 30],
                   '3': [7, 14, 13, 9, 16]})
print(df)
print(Solution().CalAvg(df))
