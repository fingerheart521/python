'''
任务详情
根据下方提供的某知名网站视频信息数据，构造一个打分模型，并根据分值挖掘高质量视频主，要求输入视频主的名字author，返回对应的UP主分层。

IFL模型
针对视频主的视频信息构建了IFL模型，以评估视频的质量，以视频主进行分组计算。
I (Interaction_rate)
I 值反映的是平均每个视频的互动率，互动率越高，表明其视频更能产生用户的共鸣，使其有话题感。
I = (总弹幕数 + 总评论数) / (总播放量 * 统计范围内视频数量) * 100。
F (Frequence)
F 值表示的是每个视频的平均发布周期，每个视频之间的发布周期越短，说明内容生产者创作视频的时间也就越短，创作时间太长，不是忠实粉丝的用户可能将其遗忘。
F = (统计范围内最晚发布视频时间 - 最早发布视频时间) / 发布视频的数量。
如果 F 的值为 0，表示该视频主仅发布一条视频。那么将 F 的值重新赋值为 F 的最大值 + 1，如原有数据中，F 的最大值是 100，那么就将 F 的最大值设置为 100 + 1 = 101。
L (Like_rate)
L值表示的是统计时间内发布视频的平均点赞率，越大表示视频质量越稳定，用户对up主的认可度也就越高。
L = (点赞数 * 1 + 投币数 * 2 + 收藏数 * 3 + 分享数 * 4) / (播放量 * 发布视频数) * 100。

维度打分
维度确认的核心是分值确定，按照设定的标准，我们给每个视频主的 I/F/L 值打分，分值的大小取决于我们的偏好，
即我们越喜欢的行为，打的分数就越高 ：
- I 值。表示 up 主视频的平均评论率，这个值越大，就说明其视频越能使用户有话题，当I值越大时，分值越大。
- F 值。表示视频的平均发布周期，我们当然想要经常看到，所以这个值越大时，分值越小。
- L 值。表示发布视频的平均点赞率，S 值越大时，质量越稳定，分值也就越大。

视频主分层 我们根据每一项指标是否高于平均值，把UP主划分为8类，我们根据案例中的情况进行划分，具体如下表
视频主分类	            I值是否大于平均值	F值是否小于平均值	L值是否大于平均值	解释
高质量视频主	            1	1	1	用户活跃高，更新周期短，视频质量高
高质量拖更视频主	        1	0	1	用户活跃高，更新周期长，视频质量高
高质量内容高深视频主	    0	1	1	用户活跃低，更新周期短，视频质量高
高质量内容高深拖更视频主	0	0	1	用户活跃低，更新周期长，视频质量高
接地气活跃视频主	        1	1	0	用户活跃高，更新周期短，视频质量低
活跃视频主	            0	1	0	用户活跃低，更新周期短，视频质量低
接地气视频主	            1	0	0	用户活跃高，更新周期长，视频质量低
还在成长的视频主	        0	0	0	用户活跃低，更新周期长，视频质量低

数据链接已经在下方给出(http://72.itmc.org.cn:80/JS001/data/user/14978/94/fj_B_video_web_data.csv)：
各字段表示含义如下：
字段名	含义
pubdate	发布时间
bv	BV号
url	视频链接
title	标题
author	作者
description	视频简介
tag	标签
favorites	收藏
coins	投币
danmu	弹幕
likes	点赞
reply	评论
views	播放量
share	分享
任务要求
1. 程序接收 str 类型的变量 author，返回结果的数据类型是str类型；
2. 便于数据美观，IFL 的值需要保留小数点后两位（四舍五入）；
3. 数据中可能存在重复数据；
4. 某知名视频网站视频数据为逗号分割的 csv 文件，utf-8 编码。

测试用例
输入：'龙爪洪荒'
输出：'高质量拖更视频主'

输入：'AO摆渡人'
输出：'活跃视频主'
'''
from math import ceil

import pandas as pd
from numpy import int64


class Solution:

    def videoMining(self, author: str) -> str:
        data = pd.read_csv('http://72.itmc.org.cn:80/JS001/data/user/14978/94/fj_B_video_web_data.csv')
        # 去重
        data.drop_duplicates()

        print("总数：", data.shape[0], len(data), "去重后：", data.drop_duplicates().shape[0])
        # count_video = data.drop_duplicates().shape[0]
        # count_danmu = data['danmu'].sum()
        # count_reply = data['reply'].sum()
        # count_views = data['views'].sum()
        # print(count_video, count_danmu, count_reply, count_views)

        # 将 pubdate 转换为时间戳
        data['pubdate'] = pd.to_datetime(data['pubdate']).astype(int64) / 10 ** 9
        # print(data['pubdate'])
        # data_groupby = data.groupby('author')
        # 计算 IFL 值
        data['I'] = (data['danmu'] + data['reply']).astype(float) / (
                data['views'] * data.size) * 100
        data['F'] = (data['pubdate'].max() - data['pubdate'].min()) / len(data)
        data.loc[data['F'] == 0, 'F'] = data['F'].max() + 1
        data['L'] = (data['likes'] * 1 + data['coins'] * 2 + data['favorites'] * 3 + data['share'] * 4).astype(
            float) / (data['views'] * len(data)) * 100

        # 对 IFL 值进行四舍五入
        data[['I', 'F', 'L']] = data[['I', 'F', 'L']].round(2)
        # print(data[['I', 'F', 'L']])

        # 计算平均值
        averages = data[['I', 'F', 'L']].mean().round(2)
        print(averages)
        author_data = data[data['author'] == author]
        print(author_data[['I', 'F', 'L']])
        author_averages = author_data[['I', 'F', 'L']].mean()
        print(author_averages)
        if author_averages['I'] > averages['I'] and author_averages['F'] < averages['F'] and author_averages['L'] > \
                averages['L']:
            return '高质量视频主'
        elif author_averages['I'] > averages['I'] and author_averages['F'] >= averages['F'] and author_averages['L'] > \
                averages['L']:
            return '高质量拖更视频主'
        elif author_averages['I'] <= averages['I'] and author_averages['F'] < averages['F'] and author_averages['L'] > \
                averages['L']:
            return '高质量内容高深视频主'
        elif author_averages['I'] <= averages['I'] and author_averages['F'] >= averages['F'] and author_averages['L'] > \
                averages['L']:
            return '高质量内容高深拖更视频主'
        elif author_averages['I'] > averages['I'] and author_averages['F'] < averages['F'] and author_averages['L'] <= \
                averages['L']:
            return '接地气活跃视频主'
        elif author_averages['I'] <= averages['I'] and author_averages['F'] < averages['F'] and author_averages['L'] <= \
                averages['L']:
            return '活跃视频主'
        elif author_averages['I'] > averages['I'] and author_averages['F'] >= averages['F'] and author_averages['L'] <= \
                averages['L']:
            return '接地气视频主'
        else:
            return '还在成长的视频主'

        # 视频主分类函数

    def classify_video_host(self, author):
        # 加载数据
        data = pd.read_csv('http://72.itmc.org.cn:80/JS001/data/user/14978/94/fj_B_video_web_data.csv')

        # 将 pubdate 转换为时间戳
        data['pubdate'] = pd.to_datetime(data['pubdate']).astype(int64) / 10 ** 9

        # 对每个视频主进行分组计算 IFL 值
        grouped_data = data.groupby('author')
        interactions = grouped_data[['danmu', 'reply']].sum()
        views = grouped_data['views'].sum()
        num_videos = grouped_data.size()
        average_interaction_rate = (interactions['danmu'] + interactions['reply']) / (views * num_videos) * 100
        frequence = (grouped_data['pubdate'].max() - grouped_data['pubdate'].min()) / num_videos
        grouped_data.loc[frequence == 0, 'frequence'] = frequence + 1
        likes = grouped_data[['likes', 'coins', 'favorites', 'share']].sum()
        average_like_rate = (likes['likes'] * 1 + likes['coins'] * 2 + likes['favorites'] * 3 + likes['share'] * 4) / (
                views * num_videos) * 100

        # 将 IFL 值保留两位小数（四舍五入）
        average_interaction_rate = average_interaction_rate.round(2)
        frequence = frequence.round(2)
        average_like_rate = average_like_rate.round(2)

        author_averages = pd.DataFrame({
            'I': average_interaction_rate[author],
            'F': frequence[author],
            'L': average_like_rate[author]
        })
        print(author_averages)
        if author_averages['I'] > average_interaction_rate.mean() and author_averages['F'] < frequence.mean() and \
                author_averages['L'] > average_like_rate.mean():
            return '高质量视频主'
        elif author_averages['I'] > average_interaction_rate.mean() and author_averages['F'] >= frequence.mean() and \
                author_averages['L'] > average_like_rate.mean():
            return '高质量拖更视频主'
        elif author_averages['I'] <= average_interaction_rate.mean() and author_averages['F'] < frequence.mean() and \
                author_averages['L'] > average_like_rate.mean():
            return '高质量内容高深视频主'
        elif author_averages['I'] <= average_interaction_rate.mean() and author_averages['F'] >= frequence.mean() and \
                author_averages['L'] > average_like_rate.mean():
            return '高质量内容高深拖更视频主'
        elif author_averages['I'] > average_interaction_rate.mean() and author_averages['F'] < frequence.mean() and \
                author_averages['L'] <= average_like_rate.mean():
            return '接地气活跃视频主'
        elif author_averages['I'] <= average_interaction_rate.mean() and author_averages['F'] < frequence.mean() and \
                author_averages['L'] <= average_like_rate.mean():
            return '活跃视频主'
        elif author_averages['I'] > average_interaction_rate.mean() and author_averages['F'] >= frequence.mean() and \
                author_averages['L'] <= average_like_rate.mean():
            return '接地气视频主'
        else:
            return '还在成长的视频主'

    def videoMiningCorrect(self, author: str) -> str:
        # 读取数据表
        df = pd.read_csv('http://72.itmc.org.cn:80/JS001/data/user/14978/94/fj_B_video_web_data.csv')

        # 删除重复项
        df.drop_duplicates(inplace=True)
        # 将‘pubdate’列转换成时间序列
        df['pubdate'] = pd.to_datetime(df['pubdate'])

        # 计算各个视频主的总值，数据汇总，不能合并的数据会被抛弃
        df_total = df.groupby('author', as_index=False, dropna=True).sum(numeric_only=True)
        # print(df_total)

        # 将作者‘author’列设置为索引，丢弃‘author’列
        df_total.set_index('author', inplace=True, drop=True)
        # print(df_total)

        # 添加新列‘count’，值为各个视频主的视频总数量
        df_total = df_total.assign(count=df['author'].value_counts())
        # print(df_total)

        # 构建 I 值
        df_total['I'] = (df_total['danmu'] + df_total['reply']) / (df_total['views'] * df_total['count']) * 100

        # 计算F值
        time_diff = df.groupby('author')['pubdate'].max() - df.groupby('author')['pubdate'].min()
        df_diff = time_diff.dt.total_seconds()
        df_total = df_total.assign(time_diff=df_diff)
        df_total['F'] = df_total['time_diff'] / df_total['count']
        df_total.loc[df_total['F'] == 0, 'F'] = df_total['F'].max() + 1
        print(df_total)

        # 计算L值
        df_total['L'] = (df_total['likes'] + df_total['coins'] * 2 + df_total['favorites'] * 3 + df_total[
            'share'] * 4) / (df_total['views'] * df_total['count']) * 100

        # 计算均值，并判断每个视频主的I、L是否大于均值，F是否小于均值，如果满足，则 * 1
        df_total['df_I'] = (df_total['I'] > df_total['I'].mean()) * 1
        df_total['df_F'] = (df_total['F'] < df_total['F'].mean()) * 1
        df_total['df_L'] = (df_total['L'] > df_total['L'].mean()) * 1

        # 将IFL综合分析
        df_total['IFL'] = (df_total['df_I'] * 100) + (df_total['df_F'] * 10) + (df_total['df_L'] * 1)

        # 创建判断函数
        def transform_label(x):
            if x == 111:
                label = '高质量视频主'
            elif x == 101:
                label = '高质量拖更视频主'
            elif x == 11:
                label = '高质量内容高深视频主'
            elif x == 1:
                label = '高质量内容高深拖更视频主'
            elif x == 110:
                label = '接地气活跃视频主'
            elif x == 10:
                label = '活跃视频主'
            elif x == 100:
                label = '接地气视频主'
            elif x == 0:
                label = '还在成长的视频主'
            return label

        # 根据IFL应用上述判断函数，创建‘人群类型’（视频主分类）列
        df_total['人群类型'] = df_total['IFL'].apply(transform_label)
        print(df_total[df_total.index == author]['人群类型'][author])
        print(type(df_total[df_total.index == author]['人群类型']))
        # 找到指定 author 的‘人群类型’(视频主分类)，然后将其提取出来，进行返回
        return df_total[df_total.index == author]['人群类型'].to_list()[0]

solution = Solution()
# print(solution.videoMining("龙爪洪荒"))
# print(solution.classify_video_host("龙爪洪荒"))
print(solution.videoMiningCorrect("龙爪洪荒"))
