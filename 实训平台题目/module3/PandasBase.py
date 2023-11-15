import pandas as pd

# 创建一个示例 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)
print(df)

# 查找 Age 为 30 的行的行号
index = df[df['Age'] == 30].index[0]
print(df[df['Age'] == 30])
print("行号:", index)