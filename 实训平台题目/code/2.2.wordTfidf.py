'''
任务详情
根据提供的商品文本信息，对商品的标题内容、属性内容和描述内容进行分词（不包含标题和商品的属性名），完成文本分析工作。
请根据以上要求，将以下所需的函数补充完整。
本任务提供了 jieba 中文分词库和 requests 库。

任务要求
1. 构建函数 wordTfidf()，对商品中除停用词外的关键词，计算其TF-IDF值；
2. 返回文本中 TF-IDF 最大的前5个关键词，返回结果为 list 数据类型；
3. 只保留词性为 n、nr、ns 的关键词；
4. 下方给出的文本编码为UTF-8。
'''
import requests
import jieba
from jieba import analyse


class Solution:

    def wordTfidf1(self) -> list:
        html = requests.get('http://72.itmc.org.cn/JS001/data/user/14978/61/fj_chiffon_lady_dress.txt')
        html.encoding = 'utf-8'
        # print(html.encoding)
        # print(html.text)

        s = html.text.splitlines()
        # print("s[4:-3]", s[4:-3])
        # print("s[-1]", s[-1])
        return jieba.analyse.extract_tags(html.text, topK=5, allowPOS=['n', 'nr', 'ns'])

    def wordTfidf(self) -> list:
        # 内容采集。因为采集的对象是txt文件，所以不需要解析，编码转换后直接可以使用
        res = requests.get('http://72.itmc.org.cn/JS001/data/user/14978/61/fj_chiffon_lady_dress.txt')
        # 编码转换
        res.encoding = 'utf-8'

        # 因为要对内容进行筛选，所以先将整体内容进行按行分隔
        s = res.text.splitlines()

        # 将‘商品标题’的内容取出
        ss = s[1]

        # 将‘商品属性’的内容取出
        # 注意冒号前面的内容不需要，只取冒号后的内容（冒号有两种形式）
        # 还要注意下，在连接文本内容时，要加上分隔符号，不然会分析错误
        for i in s[4:-3]:
            if ':' in i:
                ss = ss + ',' + i.split(':')[-1]
            if '：' in i:
                ss = ss + ',' + i.split('：')[-1]

        # 将‘商品描述’的内容取出
        ss = ss + ',' + s[-1]
        # 权重分析，并返回
        # analyse.tfidf(ana_text, topK=5, allowPOS=('nr', 'ns', 'n'))一样可以返回
        # 返回的是 list
        return analyse.extract_tags(ss, topK=5, allowPOS=('n', 'nr', 'ns'))


print(Solution().wordTfidf1())
print(Solution().wordTfidf())
