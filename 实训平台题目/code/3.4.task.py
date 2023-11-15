'''
题目描述
我们需要完成乐高商店的分析，请你根据指引完成以下任务：
使用 Pandas 读取数据；http://72.itmc.org.cn:80/JS001/data/user/14978/241/fj_lego_tmallshop_sales_data.xlsx
去掉没有价格的数据，将销量为空的数据填充为0；
计算所有产品总收入；
计算该数据中产品价格的平均值;
程序后台传入产品标题title，要求计算该产品的收入（收入总计）；
将总收入、平均价格、产品收入保存到列表里，返回给后台。

题目要求
程序传入标题title数据类型是str；
程序传出数据类型是列表类型，列表中所有元素的数据类型均是 float；
如果产品标题title存在多个，则计算相同title商品的总收入；
平均价格需要四舍五入保留小数点后2位。

测试用例
输入：’乐高旗舰店官网大电影系列70837Shimmer&Shine闪亮水疗馆玩具积木’
输出；[xxx, xxx, 1598.0]
解释：总收入和平均价格隐藏，当前产品收入总计是1598.0

输入：’乐高旗舰店幻影忍者系列70668雷电忍者杰的暴风战机’
输出：[xxx, xxx, 259073.0]
解释：总收入和平均价格隐藏，当前产品收入总计是259073.0

输入：’乐高旗舰店官网创意百变高手系列10261大型过山车积木成人送礼’
输出：[xxx, xxx, 41986.0]

数据说明
文本数据是excel文件，字段含义如下：
字段	含义	实例
title	商品名	乐高旗舰店官网 LEGO积木 儿童玩具男孩 积木拼装玩具益智
age_range	商品对应的年龄等级	适用年纪6+岁
price	商品价格	899.0
sales_num	售卖数量	217.0
'''
import pandas as pd


class Solution:
    def taskMine(self, title):
        # 读取数据
        df = pd.read_excel('http://72.itmc.org.cn:80/JS001/data/user/14978/241/fj_lego_tmallshop_sales_data.xlsx')

        # 去掉没有价格的数据，将销量为空的数据填充为0
        df = df[df['price'].notna()]
        df['sales_num'].fillna(0, inplace=True)
        df['total'] = df['price'] * df['sales_num'].astype(float)
        # print(df[df['title'] == title])
        # print(df[df['title'] == title]['price'])
        # print(df[df['title'] == title]['sales_num'].sum())
        # 计算所有产品总收入
        total_revenue = df['total'].sum()
        # 计算该数据中产品价格的平均值
        avg_price = df['price'].mean().round(2)
        # 计算指定产品的收入
        product_revenue = (df[df['title'] == title]['price'] * df[df['title'] == title]['sales_num']).sum()

        # 将总收入、平均价格、产品收入保存到列表里，返回给后台
        return [total_revenue, avg_price, product_revenue]

    def task(self, title):
        # 读取文件
        df = pd.read_excel('http://72.itmc.org.cn:80/JS001/data/user/4438/241/fj_lego_tmallshop_sales_data.xlsx')
        # 将‘销量’列中的缺失值填充为 0 ，原地修改
        df['sales_num'].fillna(0, inplace=True)
        # 计算每行商品的收入（销售金额）
        df['sale'] = df['price'] * df['sales_num']

        # 计算所有产品的总收入，转为 float 类型
        pros_sales = float(df['sale'].sum())
        # 计算指定商品 title 的总收入，转为 float 类型
        pro_sales = float(df[df['title'] == title]['sale'].sum())
        # 计算数据中产品价格的平均值，且保留两位小数，转为 float 类型
        mean_pr = float(df['price'].mean().round(2))

        return [pros_sales, mean_pr, pro_sales]


print(Solution().task("乐高旗舰店官网大电影系列70837Shimmer&Shine闪亮水疗馆玩具积木"))
print(Solution().task("乐高旗舰店幻影忍者系列70668雷电忍者杰的暴风战机"))
print(Solution().task("乐高旗舰店官网创意百变高手系列10261大型过山车积木成人送礼"))
print(Solution().task("乐高旗舰店官网10929梦想之家大颗粒益智儿童积木玩具"))
