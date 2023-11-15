'''
部门平均薪资汇总计算department_salary_summary
任务说明
        读取给定的职工薪酬考勤簿，职工薪酬考勤簿由两个表格组成，分别是 基本薪资 工作表和 上班通勤 工作表。要求计算每一个部门内部的平均薪资，并把结果 降序 排列，返回给判定程序。
        员工个人薪酬计算过程如下：
        1.薪资由两部分组成， 月基本薪资 和 通勤工资，另外需要扣除需要缴纳的 社保费及公积金；
        2.月基本薪资 = 基本薪资 + 岗位工资 + 绩效工资；
        3.通勤工资中计算如下：
            日薪 = (基本薪资 + 岗位工资 + 绩效工资) / 应出勤天数
            时薪 = 日薪 / 8
        4.通勤工资中，法定节假日加班薪资是工作日加班的 2 倍，周末加班工资是工作日加班的 1.5 倍，工作日加班工资与时薪 相同；
        5.通勤工资需要扣除因请假导致的缺勤，请假/小时需要扣除的工资按照时薪计算。
        6.社保费及公积金个人缴费按照社会保险缴费基数计算：
            a.养老保险个人缴费比例是 8%
            b.医疗保险个人缴费比例是 2%
            c.失业保险个人缴费比例是 1%
            d.公积金缴费比例是 10%

        示例：
        小王基本薪资 2000，岗位工资 2000，社会保险缴费基数是 2000。绩效工资 0，应出勤天数 20 天，请假 1 天，工作日加班 8 小时，法定节假日加班 4 小时，周末加班 4 小时。
        小王基本薪资+岗位工资+绩效工资是：2000 + 2000 = 4000；
        小王时薪：4000 / 20 / 8 = 25；
        小王加班工资：25 * 8 + 25 * 4 * 1.5 + 25 * 4 * 2 = 550；
        小王请假扣除：25 * 8 = 200；
        小王五险一金扣除：2000 * 0.08 + 2000 * 0.02 + 2000 * 0.01 + 2000 * 0.1 = 420；
        小王本月实发工资：4000 + 550 - 200 - 420 = 3930。

        假设小王所在部门有 5 个人，5 个人工资分别是 4050，4010，4120，4000，4500。小王所在部门的平均工资是：(3930+ 4010 + 4120 + 4000 + 4500) /5 = 4112。同理可算出其他部门的平均工资。

        注意：返回结果需四舍五入保留小数点后两位！
        返回结果参数类型是 pd.Series。Series 的索引应为部门名，Series 的数据应为部门平均工资，Series 的 Name 属性应修改为 “平均薪资”。

任务要求
程序无需接收参数输入，需要返回结果参数的格式是 pd.Series；
返回结果时需要四舍五入保留小数点后两位，计算过程内保留小数点后两位可能导致最后结果不正确；
部门平均工资需要降序排列；
本题所需的基本薪资表和上班通勤表均在职工薪酬工作簿中，按需读取。
Series 数据的类型应为 float64，Name 属性应为 “平均薪资”。
index 的属性名应为部门。

测试用例
部分返回数据：
部门
销售部       15767.86
运营部       ****
工程部       ****
财务部       ****
研发部       ****
市场部       ****
人力资源部    4233.27
Name: 平均薪资, dtype: float64

附件信息
职工薪酬簿.xlsx（http://72.itmc.org.cn:80/JS001/data/user/14978/242/fj_employee_salary_work_books.xlsx），职工薪酬工作簿由 基本薪资 工作表和 上班通勤 工作表组成。
基本薪资工作表。基本薪资工作表包含个人所属部门，各部分薪资状况和社会保险缴纳基数。共 7 个部门共 50 条数据，其中只有销售部有绩效工资。
上班通勤工作表。上班通勤工作表包含本月应出勤天数，实际出勤天数。请假加班天数等。工作表中的名字与基本薪资工作表中的名字一一对应。共 50 条数据。
'''

import pandas as pd


class Solution:
    def calculate_salary(self, basic_salary, post_salary, performance_salary, work_days, leave_hours, work_overtime,
                         legal_holiday_overtime, weekend_overtime, base_insurance):
        # 计算月基本薪资
        month_basic_salary = basic_salary + post_salary + performance_salary

        # 计算日薪和时薪
        daily_salary = month_basic_salary / work_days
        hourly_salary = daily_salary / 8

        # 计算加班工资
        work_overtime_salary = hourly_salary * work_overtime
        legal_holiday_overtime_salary = hourly_salary * legal_holiday_overtime * 2
        weekend_overtime_salary = hourly_salary * weekend_overtime * 1.5
        overtime_salary = work_overtime_salary + legal_holiday_overtime_salary + weekend_overtime_salary

        # 计算请假扣除的工资
        leave_deduction = hourly_salary * leave_hours

        # 计算五险一金扣除的工资
        social_security = base_insurance * 0.08 + base_insurance * 0.02 + base_insurance * 0.01 + base_insurance * 0.1

        # 计算实发工资
        real_salary = month_basic_salary + overtime_salary - leave_deduction - social_security
        return real_salary

    def department_salary_summary_mine(self) -> pd.Series:
        # 读取Excel文件
        salary_df = pd.read_excel(
            'http://72.itmc.org.cn:80/JS001/data/user/14978/242/fj_employee_salary_work_books.xlsx', sheet_name='基本薪资')
        commute_df = pd.read_excel(
            'http://72.itmc.org.cn:80/JS001/data/user/14978/242/fj_employee_salary_work_books.xlsx', sheet_name='上班通勤')

        # 合并两个工作表的数据，以姓名作为合并的键
        df = pd.merge(salary_df, commute_df, on='姓名')
        df.fillna(0, inplace=True)
        # 应用计算薪资的函数到每个员工的数据上
        df['实发工资'] = df.apply(
            lambda row: self.calculate_salary(row['基本薪资'], row['岗位工资'], row['绩效工资'], row['应出勤天数（天）'], row['请假（小时）'],
                                              row['工作日加班（小时）'],
                                              row['法定假日加班（小时）'], row['周末加班（小时）'], row['社会保险缴费基数']), axis=1)
        # 按照部门进行分组，并计算每个部门的平均工资
        avg_salary = df.groupby('部门')['实发工资'].mean().round(2).sort_values(ascending=False)
        # 将结果保存到一个pd.Series对象中，并设置Name属性为“平均薪资”
        result = pd.Series(avg_salary, name='平均薪资')
        return result

    def department_salary_summary(self) -> pd.Series:
        # 读取基本薪资工作表
        df1 = pd.read_excel('http://72.itmc.org.cn:80/JS001/data/user/4438/242/fj_employee_salary_work_books.xlsx',
                            sheet_name=0)
        # 读取职工薪酬工作表
        df2 = pd.read_excel('http://72.itmc.org.cn:80/JS001/data/user/4438/242/fj_employee_salary_work_books.xlsx',
                            sheet_name=1)
        # 将两个表以‘姓名’列为连接键进行连接合并
        df = pd.merge(df1, df2)
        # 因为表中存在缺失值，所以先将其填充为 0 ，方便后续计算，原地修改
        df.fillna(0, inplace=True)

        # 计算‘五险一金’扣除金额
        df['五险一金'] = df['社会保险缴费基数'] * (0.08 + 0.02 + 0.01 + 0.1)
        # 计算员工‘基本工资’
        df['基本工资'] = df['基本薪资'] + df['岗位工资'] + df['绩效工资'] - df['五险一金']
        # 计算员工的‘时薪’
        df['时薪'] = (df['基本薪资'] + df['岗位工资'] + df['绩效工资']) / df['应出勤天数（天）'] / 8
        # 计算员工的‘通勤工资’
        df['通勤工资'] = df['工作日加班（小时）'] * df['时薪'] + df['周末加班（小时）'] * df['时薪'] * 1.5 + df['法定假日加班（小时）'] * df['时薪'] * 2 - \
                     df['时薪'] * df['请假（小时）']
        # 计算员工的总工资
        df['总工资'] = df['基本工资'] + df['通勤工资']

        # 为了方便，只取‘部门’、‘总工资’列
        # 对‘部门’进行分组，计算各部门员工的‘平均薪资’，然后进行降序排序（默认正序排序），最后保留两位小数，并转为 Series (取‘总工资’列) ，
        series = df[['部门', '总工资']].groupby('部门').mean().sort_values(by='总工资', ascending=False).round(2)['总工资']
        # 将 Series 的名字改为‘平均薪资’
        series.name = '平均薪资'
        return series


print(Solution().department_salary_summary())
