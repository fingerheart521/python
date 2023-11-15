'''
任务详情
请根据系统提供的订单数据表，按要求完成以下三个任务：
传入一个字符串，返回订单总金额 (quantity * item_price) 最大或最小的商品，item_price是带$符号的字符串，并返回商品的名称(item_name)。
请根据以上要求，将函数 salesStr() 补充完整，函数的返回值为字符(str)，比如："Steak Burrito"
订单数据访问地址请见下方：http://72.itmc.org.cn:80/JS001/data/user/14978/80/fj_order_data.csv
字段名	中文含义
order_id	商品编号
quantity	数量
item_name	商品名称
choice_description	描述
item_price	单价

任务要求
1. 传入一个字符串('max' 或 'min')，返回订单总金额最大或最小的商品的名称(item_name) ；
2. 传入的字符串不区分大小写，即传入值可能是"Max"，也可能是"max"；
3. 传入"max"，返回订单总金额 (quantity * item_price) 最大的商品名称；传入“min”，返回订单总金额 (quantity * item_price) 最小的商品名称；
4. 返回字符串区分大小写，且保留字符串中间空格。
'''
import pandas as pd


class Solution:
    def salesStr(self, condition: str) -> str:
        url = 'http://72.itmc.org.cn:80/JS001/data/user/14978/80/fj_order_data.csv'
        # 读取订单数据
        df = pd.read_csv(url, sep=',')
        # print(df)
        # 将带$符号的字符串转换为数字
        df['item_price'] = df['item_price'].str.replace('$', '', regex=False).astype(float)
        # 根据传入参数 'max' 或 'min'，计算订单总金额最大或最小的商品名称
        if condition.lower() == 'max':
            print(df.groupby("order_id").sum())
            # print((df['quantity'] * df['item_price']).idxmax())
            result = df.loc[(df['quantity'] * df['item_price']).idxmax(), 'item_name']
        elif condition.lower() == 'min':
            result = df.loc[(df['quantity'] * df['item_price']).idxmin(), 'item_name']
        else:
            return "Invalid input. Please enter 'max' or 'min'."
        return result

    def salesStr2(self, condition: str) -> str:
        url = 'http://72.itmc.org.cn:80/JS001/data/user/14978/80/fj_order_data.csv'
        # 读取订单数据
        df = pd.read_csv(url, sep=',')
        # print(df)
        # 将带$符号的字符串转换为数字
        df['item_price'] = df['item_price'].str.replace('$', '', regex=False).astype(float)
        df['price'] = df['quantity'] * df['item_price']
        groups = df.groupby("item_name")
        # 根据传入参数 'max' 或 'min'，计算订单总金额最大或最小的商品名称
        if condition.lower() == 'max':
            result = groups['price'].sum().idxmax()
        elif condition.lower() == 'min':
            result = groups['price'].sum().idxmin()
        else:
            return "Invalid input. Please enter 'max' or 'min'."
        return result

    def salesStr3(self, condition: str) -> str:
        # 读取文件
        df = pd.read_csv('http://72.itmc.org.cn:80/JS001/data/user/14978/80/fj_order_data.csv')
        # 将列‘item_price’数据中的美元符号 $ 去掉，然后再将数据类型转为 flaot
        df['item_price'] = df['item_price'].map(lambda x: x[1:]).astype('float')
        # 创建列 ‘sales’，其值为每笔订单（每行）的总金额，一行数据为一笔订单
        df['sales'] = df['quantity'] * df['item_price']

        # 如果求的是最大值
        if condition.lower() == 'max':
            # 将商品进行分组，求每种商品（所有订单中每种商品）的总金额，然后排序（默认正序排序），返回最大值的商品的名称
            print(df.groupby('item_name').sum().sort_values('sales').index)
            return df.groupby('item_name').sum().sort_values('sales').index[-1]

        # 如果求的是最小值
        else:
            # 返回最小值的商品的名称
            return df.groupby('item_name').sum().sort_values('sales').index[0]

print(Solution().salesStr2("max"))
print(Solution().salesStr3("max"))
