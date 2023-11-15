"""
任务详情
下方的网页为微信公共号数据分析展示页，地址：http://72.itmc.org.cn/JS001/open/show/weixindata.html，网页数量为1。
请根据网页给出的信息，完成以下任务，将右边的函数 weixinData() 补充完整。
给定原创排行榜里任一微信公众号的名称，请判断该公众号是否满足以下条件：
1.“头条平均阅读”数 > 90000
2.“原创平均阅读”数 > 80000
3.“预估活跃粉丝”数 < 300万
如果满足，函数 weixinData() 返回大写英文单词“YES”，否则返回“NO”。

任务要求
1. 函数接收 str 数据类型的微信公众号名称 name；
2. 函数返回为英文字符“YES”或“NO”，返回参数为 str 数据类型；
3. 不得修改函数 weixinData() 的名称；
4. 题目所需网站链接已经在下方给出，编码方式为UTF-8。
"""
import re
import requests
from bs4 import BeautifulSoup


class Solution:

    def convert_str_to_num(self, str_num):
        pattern = re.compile(r'(\d+(\.\d+)?万|\d+万\+|\d+)')
        match = pattern.search(str_num)
        if match:
            if '万' in match.group():
                number = float(match.group().replace('万', '')) * 10000
            elif '+' in match.group():
                number = int(match.group().replace('万+', '')) * 10000
            else:
                number = int(match.group())
            return number
        else:
            return str_num

    def weixinData(self, name: str) -> str:
        # 从此处开始编写代码
        url = 'http://72.itmc.org.cn/JS001/open/show/weixindata.html'
        html = requests.get(url)
        html.encoding = "utf-8"
        soup = BeautifulSoup(html.text, "html.parser")
        table = soup.find_all('table')
        account = table[1].find(string=name)
        #print(account)
        tds = account.find_parent("tr").find_all("td")
        fans = tds[3].text
        readerTouTiao = tds[4].text
        readerOriginal = tds[7].text
        # print(fans, readerTouTiao, readerOriginal)
        # print(self.convert_str_to_num(fans), self.convert_str_to_num(readerTouTiao),
        #       self.convert_str_to_num(readerOriginal))
        # 1.“头条平均阅读”数 > 90000
        # 2.“原创平均阅读”数 > 80000
        # 3.“预估活跃粉丝”数 < 300万
        if self.convert_str_to_num(fans) < 3000000 and self.convert_str_to_num(
                readerTouTiao) > 90000 and self.convert_str_to_num(readerOriginal) > 80000:
            return "YES"
        else:
            return "NO"
        pass  # 请返回正确结果
        # 代码编写结束
    def weixinData2(self, name: str) -> str:
        # 提供的代码是 import bs4，所以要 bs4.BeautifulSoup 这样书写
        res = requests.get('http://72.itmc.org.cn/JS001/open/show/weixindata.html')
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')

        # 先找到公众号名称所在的节点
        # 然后再找到三条信息所在的公共节点
        target_tag = soup.find('span',string = name).parent.parent.parent

        # 判断‘头条平均阅读’信息。
        # 如果信息中有‘万’，则数据均是 10万+ ，所以一定大于90000，所以略过，进行下一条要求的判断
        # 如果信息中不存在‘万’，则正常比较，如果大于90000，则略过，继续下一条要求的判断，否则直接返回 ‘NO’
        if '万' in target_tag.find_all('td')[4].string:
            pass
        else:
            if int(target_tag.find_all('td')[4].string) <= 90000:
                return 'NO'

        # 判断‘原创平均阅读’信息
        # 判断方法类似上一条
        if '万' in target_tag.find_all('td')[7].string:
            pass
        else:
            if int(target_tag.find_all('td')[7].string) <= 80000:
                return 'NO'

        # 判断‘预估活跃粉丝’信息
        # 这是最后一条要求，所以如果不满足的话直接返回‘NO’即可，不用再继续进行判断了
        if float(target_tag.find_all('td')[3].string.replace('万','')) >= 300:
            return 'NO'
        # 当都满足的时候，返回 ‘YES’
        return 'YES'


print(Solution().weixinData("占豪"))
print(Solution().weixinData("智合"))
print(Solution().weixinData("Vista看天下"))

