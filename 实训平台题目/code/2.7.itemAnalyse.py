'''
任务详情
请使用 杭州大牌女装.txt 文本完成提取文本中权重最高的 5 个关键词的任务。

任务要求
1. 程序以数组的形式返回五个关键词，关键词类型是 str；
2. 使用结巴库内置的TextRank 算法抽取关键词，只返回关键词，不必返回权重。关键词的词性必须是名词和动词；
3. 返回的5个关键词至少要有4个关键词与系统内置的答案一致；
4. 返回关键词不需要考虑顺序；
5. 杭州大牌女装.txt使用 requests 库读取，UTF-8编码，链接（http://72.itmc.org.cn:80/JS001/data/user/14978/77/fj_5392_hangzhou_top_woman_wear.txt）；
6. Jieba库词性表及说明.xlsx 链接（http://72.itmc.org.cn:80/JS001/data/user/14978/77/fj_Jieba词性表及说明.xlsx），作为参考。
'''
import requests
import jieba.analyse


class Solution:
    def itemAnalyseMine(self) -> list:
        url = 'http://72.itmc.org.cn:80/JS001/data/user/14978/77/fj_5392_hangzhou_top_woman_wear.txt'
        # 从URL读取文本文件
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text

        # 使用jieba的TextRank算法提取关键词
        keywords = jieba.analyse.textrank(text, topK=5, withWeight=False, allowPOS=('n', 'v'))
        return keywords

    def itemAnalyse(self) -> list:
        # 内容采集
        res = requests.get('http://72.itmc.org.cn:80/JS001/data/user/4438/77/fj_5392_hangzhou_top_woman_wear.txt')
        # 编码转换
        res.encoding = 'utf-8'

        # 对名词、动词进行权重分析
        # 取权重排名前 5 的词语
        return jieba.analyse.textrank(res.text, topK=5, allowPOS=('n', 'v'))


print(Solution().itemAnalyse())
