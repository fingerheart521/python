'''
任务详情
采用Python自带的函数库进行数据操作，完成任务下方《爱丽丝梦游仙境》英文文本词频的分析。
请将右边的函数  aliceText() 补充完整，使其能够输出某个单词的词频。

任务要求
1. 不得直接使用 Jieba 库对文本进行分词；
2. 函数 aliceText() 接收一个英文单词 word，str 数据类型；返回该单词的词频，int 数据类型；
3. 只保留单词长度大于等于 3 的单词的词频统计；
4. 英文单词不区分大小写；
5. 不同时态和单复数的英文单词为不同英文单词，不需要合并词频统计。如果文本中没有该单词，词频为0；
6. 文本可以使用 requests 库进行读取，UTF-8 编码方式，否则无法正确读取文本。
'''
import re
import requests
from collections import Counter


class Solution:
    def remove_punctuation(self, text):
        # 使用正则表达式去除标点符号,\w匹配字母、数字和下划线，\s匹配空格，[^]取反，表示匹配除了这些字符之外的所有字符，也就是标点符号。re.sub方法将匹配到的标点符号替换为空字符串，从而得到一个没有标点符号的文本。
        punctuation_pattern = r'[^a-zA-Z\s]'
        no_punctuation = re.sub(punctuation_pattern, ' ', text)
        return no_punctuation

    def aliceTextMine(self, word: str) -> int:
        # 从网络上获取《爱丽丝梦游仙境》的英文文本
        response = requests.get('http://72.itmc.org.cn:80/JS001/data/user/14978/76/fj_alice_adventure.txt')
        response.encoding = 'utf-8'
        text = response.text
        # text="V--ADVICE FROM A CATERPILLAR"

        # 将文本转化为小写，便于不区分大小写地统计词频
        text = self.remove_punctuation(text.lower())

        # 使用 Python 的 split() 函数将文本分割为单词列表
        words = text.split()

        # 使用 Counter 对单词列表进行词频统计
        word_counts = Counter(words)
        word_counts_sorted = sorted(word_counts, reverse=True)
        # 如果单词长度大于等于3，返回对应单词的词频，否则返回0
        word = word.lower()
        if len(word) >= 3:
            return word_counts[word]
        else:
            return 0

    def aliceText(self, word: str) -> int:
        # 下载文件内容
        res = requests.get('http://72.itmc.org.cn:80/JS001/data/user/4438/76/fj_alice_adventure.txt')
        # 编码转换
        res.encoding = 'utf-8'

        # 为了后续方便拆分，判断筛选文本内容res.text中是否有这些符号，如果有话，就将其替换为空格
        # 当然这样做可能会遗漏某些符号
        # 最好还是用 re 来进行替换，将不是下列字符的其他字符替换为空格，再替换换行符，如：
        # text = re.sub('[^A-Za-z1-9\']', ' ', rep.text).replace('\n', ' ')
        s = res.text
        for i in [',', '-', '.', '!', '?', '\r', '\n', '\ufeff', ';', ':', '"', '_']:
            if i in res.text:
                s = s.replace(i, ' ')

        # 将筛选后的文本内容用空格进行分割
        li = s.split(' ')
        # 筛选出长度大于等于 3 的词汇
        # 在这里要将所有词汇小写
        li = [i.lower() for i in li if len(i) >= 3]

        # 创建一个字典，为了对单词进行计数统计
        # 字典的get方法就实现了这一操作，查找某个‘键’，如果存在，就返回对应的值，不存在返回 0，或其他自定义的内容
        dict_ = {}
        for i in li:
            dict_[i] = dict_.get(i, 0) + 1

        # 查找 word 出现的次数，如果不存在返回 0
        # 注意，这里也要将 word 小写化，与‘键’相对应
        return dict_.get(word.lower(), 0)


# print(Solution().aliceText('Pictures'.lower()))
# print(Solution().aliceText('nothing'.lower()))
# print(Solution().aliceText('caterpillar'.lower()))
print(Solution().aliceText('ADVIcE'.lower()))
