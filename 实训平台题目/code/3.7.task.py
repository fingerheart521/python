'''
店铺不同地区销售情况分析
题目描述
下方是某店铺在 2 月份的订单数据(http://72.itmc.org.cn:80/JS001/data/user/14978/240/fj_7568_tmall_order_report.csv)，
共 28010 行、7 列。 在该数据中，每一行代表一笔订单，每一笔订单可以 看做是一位顾客（买家），价格相同的产品可视为同一产品；

请编写程序，完成以下任务：
程序传入参数 area（收货地址），要求计算该地区订单的’订单的付款转化率’、’买家全额支付的转化率’、’买家实际支付总金额’、
’客单价’、’销量（订单量）最多的产品的价格’、’买家实际支付总金额在所有地区实际支付总金额中的占比’，并将结果以列表形式返回。

题目要求
程序接收 str 类型的 area，返回的结果为 list 数据类型；
返回的结果中，列表中各个数据的数据类型为 str，其中转化率数据及占比数据需以百分比的形式输出，并且需要保留小数点后2位，如’13.14%’，其余结果不需要以百分比形式输出，但需要保留小数点后2位；
如果某地区所有买家的买家实际支付金额为 0，即该地区没有付费行为。则该地区的’客单价’、’销量（订单量）最多的产品的价格’需返回字符串’本地区无销量’，其他结果则正常计算；
如果该产品（订单）被全额退款，那么该产品不计入销量。

参考公式
付款转化率 = 付款订单数 / 总订单数；
买家全额支付的转化率 = 买家全额支付的订单数 / 总订单数；
客单价 = 实际支付金额 / 支付买家数；

测试用例
输入：area = ‘河南省’
输出：[‘81.99%’, ‘61.18%’, ‘56354.03’, ‘92.84’, ‘37.00’, ‘2.96%’]
解释：河南省’订单的付款转化率’为’81.99%’，’买家全额支付的转化率’为’61.18%’，
’买家实际支付总金额’为’56354.03’，’客单价’为’92.84’，’销量（订单量）最多的产品的价格’为’37.00’，’买家实际支付总金额在所有地区实际支付总金额中的占比’为’2.96%’

输入：area = ‘江苏省’
输出：[‘86.78%’, ‘66.75%’, ‘159359.18’, ‘109.22’, ‘37.00’, ‘8.38%’]
'''
import pandas as pd


class Solution:
    def taskMine(self, area: str) -> list:
        df = pd.read_csv("http://72.itmc.org.cn:80/JS001/data/user/14978/240/fj_7568_tmall_order_report.csv")
        # df.loc([df['收货地址']==area])
        # return df.loc[df['收货地址'] == area]
        # 根据收货地址筛选出指定地区的订单
        df_area = df[df['收货地址'] == area]

        # 计算付款转化率和买家全额支付的转化率
        total_orders = df_area.shape[0]  # len(df_area)
        paid_orders = df_area[df_area['订单付款时间'].notna()].shape[0]
        full_paid_orders = df_area[(df_area['买家实际支付金额'] == df_area['总金额']) & (df_area['买家实际支付金额'] != 0)].shape[0]
        payment_rate = f"{paid_orders / total_orders * 100:.2f}%"
        full_payment_rate = f"{full_paid_orders / total_orders * 100:.2f}%"

        # # 计算买家实际支付总金额
        actual_payment = df_area['买家实际支付金额'].sum()

        # # 计算客单价
        paid_buyers = df_area[df_area['买家实际支付金额'] != 0].shape[0]
        if paid_buyers == 0:
            avg_order_value = '本地区无销量'
        else:
            avg_order_value = f"{actual_payment / paid_buyers:.2f}"

        # 统计销量（订单量）最多的产品的价格
        df_valid = df_area[(df_area['买家实际支付金额'] != 0) & (df_area['总金额'] > df_area['退款金额'])]
        product_counts = df_valid.groupby('总金额').count().reset_index()
        if not product_counts.empty:
            max_sales_price = product_counts[product_counts['订单编号'] == product_counts['订单编号'].max()]['总金额'].values[0]
        else:
            max_sales_price = 0

        if max_sales_price == 0:
            max_sales_price = '本地区无销量'
        else:
            max_sales_price = f"{max_sales_price:.2f}"
        # print(max_sales_price)
        # print(max_sales_price['总金额'].values[0])
        # print(max_sales_price.loc[:,'总金额'])
        # print(max_sales_price.iloc[0,0])

        # 计算买家实际支付总金额在所有地区实际支付总金额中的占比
        total_actual_payment = df['买家实际支付金额'].sum()
        if total_actual_payment == 0:
            payment_ratio = '0.00%'
        else:
            payment_ratio = f"{actual_payment / total_actual_payment * 100:.2f}%"

            # 返回计算结果列表
        return [payment_rate, full_payment_rate, f"{actual_payment:.2f}", avg_order_value, max_sales_price,
                payment_ratio]

    def task(self, area: str) -> list:
        # 读取文件
        df = pd.read_csv("http://72.itmc.org.cn:80/JS001/data/user/4438/240/fj_7568_tmall_order_report.csv")
        # 筛选出 area 地区的订单数据
        df_area = df[df["收货地址"] == area]
        # 总订单数
        ord_sum = len(df_area)

        # 订单的付款转化率:付款订单数 / 总订单数
        # 付款订单数：订单付款时间列中非缺失值的数量，即存在付款行为的数量，没有付款时间说明没有付过款
        pay_rate = "{:.2%}".format(df_area["订单付款时间"].notna().sum() / ord_sum)

        # 买家全额支付的转化率:买家全额支付的订单数 / 总订单数
        # 买家全额支付的订单数：买家实际支付金额 == 总金额 的数量
        fulpay_rate = "{:.2%}".format(len(df_area[df_area["买家实际支付金额"] == df_area["总金额"]]) / ord_sum)

        # 买家实际支付总金额:‘买家实际支付金额’ 列的总和
        # 保证后续计算数据准确，准备一个没有保留小数的数据
        pay_sum = df_area["买家实际支付金额"].sum()
        pay_sum_result = "{:.2f}".format(df_area["买家实际支付金额"].sum())

        # 客单价&销量最多的产品的价格
        # 如果本地区无销量，即买家实际支付总金额为 0
        if pay_sum == 0:
            # 客单价
            per_cus = "本地区无销量"
            # 销量最多的产品的价格
            pro_pir = "本地区无销量"
        else:
            # 客单价:实际支付金额 / 支付买家数
            # 支付买家数：买家实际支付金额大于 0 的数量
            per_cus = "{:.2f}".format(pay_sum / len(df_area[df_area["买家实际支付金额"] > 0]))
            # 销量最多的产品的价格:买家实际支付金额大于0的订单中，对总金额（产品的价格）列进行计数操作（默认降序排序），求数量最多的产品的价格
            # 计数操作后，返回一个 Series，总金额（产品的价格）为索引，对应出现的数量为数据，且数据（总金额）数量最多的在最前面
            pro_pir = "{:.2f}".format(df_area[df_area["买家实际支付金额"] > 0]["总金额"].value_counts().index[0])

        # 买家实际支付总金额在所有地区实际支付总金额中的占比:本地买家实际支付总金额 / 所有地区买家实际支付总金额
        pay_ratio = "{:.2%}".format(pay_sum / df["买家实际支付金额"].sum())

        return [pay_rate, fulpay_rate, pay_sum_result, per_cus, pro_pir, pay_ratio]


# print(Solution().task("上海"))
# print(Solution().task("河南省"))
# print(Solution().task("江苏省"))
# print(Solution().task("湖北省"))
print(Solution().task("西藏自治区"))
