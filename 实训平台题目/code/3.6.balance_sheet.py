'''
编制比较资产负债表Preparation of comparative balance sheets
任务描述
“A企业资产负债表.xlsx”文件（http://72.itmc.org.cn:80/JS001/data/user/14978/243/fj_Interprice_balance_data.xlsx）的“比较资产负债表”
包含 A 企业 2020 年和 2021 年的资产负债数据，请完成以下指定任务。
使用 0 填充表格中的空值；
计算 2021 年各项目变动额和变动率并添加相关数据列；
程序接受某项目的项目名称 name，要求输出该项目对应的变动额和变动率。

任务要求
代码要编辑在 balance_sheet 函数下；
变动额需要四舍五入保留小数点后 2 位，变动率需要四舍五入保留小数点后 4 位；
变动额和变动率的数据类型都是浮点数数据类型；
程序只判定 return后的结果值，输出（print）后的结果值不作为判断依据；
程序返回结果的数据类型为列表。

测试用例
输入：name="负债合计"
输出：[26928392.51, 0.2567]
解释：负债总计变动额是 26928392.51，变动率是 0.2567

输入：name="无形资产"
输出：[-600000.0, -0.0667]
解释：无形资产变动额是 -600000.0，变动率是 -0.0667

代码提示
我们通过将 Series 转换为列表的形式，将其中的数字提取出来。
通过如下案例，我们取出 DataFrame 中的 1。

In [1]: import pandas as pd
# 定义一个 DataFrame
In [2]: df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
# 预览下 df
In [3]: df
Out[3]:
   A  B
0  1  2
1  3  4

# 通过列名取出 A 列
In [4]: df['A']
Out[4]:
0    1
1    3
Name: A, dtype: int64

# 取出 A 列再将 A 列转换为列表
In [5]: df['A'].tolist()
Out[5]: [1, 3]

# 取出列表中的第一个元素，就是我们想要的 1
In [6]: df['A'].tolist()[0]
Out[6]: 1
'''
import pandas as pd


class Solution:
    def balance_sheet_mine(self, name):
        df = pd.read_excel('http://72.itmc.org.cn:80/JS001/data/user/14978/243/fj_Interprice_balance_data.xlsx',
                           sheet_name='比较资产负债表')
        # 使用 0 填充表格中的空值；
        df.fillna(0, inplace=True)
        # 计算 2021 年各项目变动额和变动率并添加相关数据列；
        df['change'] = (df['2021.12.31'].astype(float) - df['2020.12.31'].astype(float)).round(2)
        df['rate'] = (df['change'] / df['2020.12.31'].astype(float)).round(4)
        # 程序接受某项目的项目名称 name，要求输出该项目对应的变动额和变动率。
        # 提取指定项目的变动额和变动率
        # result = [df.loc[df['项目'] == name, 'change'].values[0], df.loc[df['项目'] == name, 'rate'].values[0]]
        result = df.loc[df['项目'] == name, ['change', 'rate']].iloc[0].tolist()
        return result

    def balance_sheet(self, name):
        # 读取第三个 sheet 表
        df = pd.read_excel('http://72.itmc.org.cn:80/JS001/data/user/4438/243/fj_Interprice_balance_data.xlsx',
                           sheet_name=2)
        # 将缺失值填充为 0 ，原地修改
        df.fillna(0, inplace=True)

        # 添加新列 ‘变动额’，保留两位小数
        df['变动额'] = (df['2021.12.31'] - df['2020.12.31']).round(2)
        # 添加新列 ‘变动率’，保留四位小数
        df['变动率'] = ((df['2021.12.31'] - df['2020.12.31']) / df['2020.12.31']).round(4)

        # 找到项目 name
        df = df[df['项目'] == name]

        # 返回该项目的 ‘变动额’、‘变动率’，记得转为 float 类型
        return [float(df['变动额']), float(df['变动率'])]


print(Solution().balance_sheet("负债合计"))
print(Solution().balance_sheet("无形资产"))
