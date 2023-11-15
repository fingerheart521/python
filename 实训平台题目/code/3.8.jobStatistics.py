'''
任务详情
请根据任务下方提供的用户职位统计信息表，完成以下任务：
职位表中每个字段含义如下：
字段	说明
user_id	用户序号
age	用户年龄
gender	用户性别
occupation	用户职位
zip_code	用户邮编
编写一个职位统计函数 jobStatistics()，给定表格里的任一职位，统计其以下信息
1. 任务一：统计该职位女性用户的百分占比（结果保留两位小数），输出数据类型为 str；
2. 任务二：统计该职位女性用户百分占比在所有职位女性用户百分占比中的排名（降序），输出数据类型为 int。
将以上2个结果保存在 数组(list) 中，按顺序返回。

任务要求
1. 程序接收一个 str 类型的变量 op，返回一个 list 类型的变量；
2. "gender" 列中，"F" 代表女性，"M" 代表男性；
3. 返回结果格式如下：[任务一: str, 任务二: int]。

测试用例
输入：'artist'
输出：[ '46.43%', 4]
解释：该职位中女性用户占据该职位所有用户的46.43%，该职位女性占比排名在所有职位女性占比排名中位列第 4

输入：'student'
输出：['30.61%', 10]
解释：该职位中女性用户占据该职位所有用户的30.61%，该职位女性占比排名在所有职位女性占比排名中位列第 10
'''
import pandas as pd


class Solution:
    def jobStatisticsMine(self, occupation: str) -> list:
        url = 'http://72.itmc.org.cn:80/JS001/data/user/14978/67/fj_jobstatics.xlsx'
        df = pd.read_excel(url)

        df_occupation = df[df['occupation'] == occupation]
        # df_gender_count = df_occupation.groupby('gender').count().reset_index()
        count_female = df_occupation[df_occupation['gender'] == 'F'].shape[0]
        count_male = df_occupation[df_occupation['gender'] == 'M'].shape[0]
        ratio_female = f'{count_female / (count_female + count_male) * 100:.2f}%'

        # 计算女性用户百分占比在所有职位中的排名
        all_female_ratios = df.groupby('occupation')['gender'].apply(lambda x: (x == 'F').mean() * 100)
        print(df.groupby('occupation')['gender'])
        # print(all_female_ratios)
        # print(type(all_female_ratios))
        rank = int(all_female_ratios.rank(ascending=False).loc[occupation])
        return [ratio_female, rank]

    def jobStatisticsByBaidu(self, occupation: str) -> list:
        url = 'http://72.itmc.org.cn:80/JS001/data/user/14978/67/fj_jobstatics.xlsx'
        data = pd.read_excel(url)
        # 筛选出指定职位的数据
        selected_data = data[data['occupation'] == occupation]

        # 统计女性用户数量
        female_count = selected_data[selected_data['gender'] == 'F'].shape[0]

        # 统计总用户数量
        total_count = selected_data.shape[0]

        # 计算女性用户百分占比
        female_ratio = female_count / total_count * 100
        female_ratio_str = f'{female_ratio:.2f}%'

        # 计算女性用户百分占比在所有职位中的排名
        all_female_ratios = data.groupby('occupation')['gender'].apply(lambda x: (x == 'F').mean() * 100)
        # print(data.groupby('occupation').count())
        # print(str(data.groupby('occupation').))
        # print((data.groupby('occupation')))
        rank = all_female_ratios.rank(ascending=False).loc[occupation]

        return [female_ratio_str, rank]

    def jobStatistics(self, occupation: str) -> list:
        # 表格链接
        url = 'http://72.itmc.org.cn:80/JS001/data/user/4438/67/fj_jobstatics.xlsx'
        # 读取表格
        chipo = pd.read_excel('http://72.itmc.org.cn:80/JS001/data/user/4438/67/fj_jobstatics.xlsx')

        # 将指定的职位信息‘occupation’数据挑选出来
        chipo_1 = chipo[chipo['occupation'] == occupation]

        # 计算指定职位信息数据中‘女’性的数量：len(chipo_1[chipo_1['gender'] == 'F'])
        # 计算指定职位信息数据总数量：len(chipo_1)
        # 计算‘女’性占比，以百分号的形式返回，且保留两位小数
        proportion = '{:.2%}'.format(len(chipo_1[chipo_1['gender'] == 'F']) / len(chipo_1))

        # 将数据表按照‘职位’（occupation）、‘性别’（gender）分组：chipo.groupby(['occupation','gender'])
        # 计算每组数据‘user_id’列中数据的个数即每组数据的个数：.count()，返回的结果为层次化索引的 DataFrame
        #                         user_id  age  zip_code
        # occupation    gender
        # administrator   F         36      36     36
        #                 M         43      43     43
        # artist          F         13      13     13
        #                 M         15      15     15
        # doctor          M          7       7      7
        # educator        F         26      26     26
        #                    .....
        # 因为没有缺失值，数据数量相同，所以然后随便选取一列：['user_id']，返回的是一个 Series，依旧是层次化索引
        # occupation     gender
        # administrator  F          36
        #                M          43
        # artist         F          13
        #                M          15
        # doctor         M           7
        # educator       F          26
        #           ......
        # 将返回结果进行行列转换，将数据的行‘旋转’为列：.unstack()，将‘gender’转为列索引，行索引为‘occupation’，列索引为‘F’、‘M’
        # gender         F      M
        # occupation
        # administrator  36.0  43.0
        # artist         13.0  15.0
        # doctor         NaN    7.0
        # educator       26.0   69.0
        #          ......
        # 旋转后数据中存在缺失值，将缺失值填充为 0，方便后续比重计算
        df = chipo.groupby(['occupation', 'gender']).count()['user_id'].unstack().fillna(0)

        # 创建‘占比’列，并计算其数据：‘女’性数量 / 总数量
        df['占比'] = df['F'] / (df['F'] + df['M'])

        # 对列‘占比’数据进行排名，并降序排序：df['占比'].rank(ascending = False)，索引不变，数据为具体的排序
        # occupation
        # administrator     5.0
        # artist            4.0
        # doctor           21.0
        # educator         11.0
        # engineer         20.0
        #        ......
        # 因为题目中并没有说存在排名相同的情况，所以各个职位女性用户的占比必定不会相同，所以直接调用 rank 方法默认排名即可
        # 找到指定岗位‘occupation’的占比排名情况：[occupation]
        # 将数据类型转为 int
        # 以列表形式返回
        return [proportion, int(df['占比'].rank(ascending=False)[occupation])]


print(Solution().jobStatisticsMine("artist"))
print(Solution().jobStatistics("student"))
print(Solution().jobStatistics("doctor"))
# print(Solution().jobStatisticsByBaidu("artist"))
# print(Solution().jobStatisticsByBaidu("student"))
