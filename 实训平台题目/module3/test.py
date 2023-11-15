import pandas as pd

# 创建一个示例数据集
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'value': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)

# 对数据进行分组求和
grouped = df.groupby('group')['value'].sum()

# 找到每组中最大值的索引
max_index = grouped.idxmax()
print(max_index)

# 提取最大行
max_row = df.loc[max_index]

# 输出结果
print(max_row)
