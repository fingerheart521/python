'''
任务详情
给定内地某日票房排行榜，输入指定影片名称 movie_name，如：'金刚川'。完成以下任务：
1. 任务一：获取指定影片的上映天数。如“金刚川”上映20天，返回 20；“一日成交”上映首日，返回0，“翱翔雄心”点映，返回 -1；
2. 任务二：获取指定影片的综合票房（万元）。如“金刚川”，返回 432.33；
3. 任务三：获取指定影片的排片占比。如“金刚川”，返回 0.248。

任务要求
1. 程序接收 str 类型的变量 movie_name，返回 list 类型的变量；
2. 返回列表包含参数如下：[任务一：int, 任务二：float，任务三：float]；
3. 任务一中，如果是上映天数是“上映首日”，返回0；如果上映天数是“点映”，返回 -1；
4. 任务三中需要将百分比形式转换为小数点形式。如 '24.8%' 需要转换为 0.248；如果票房 <0.1%，返回 0.001；
5. 票房信息排行榜在下方给出，utf-8编码。
'''

import re
from bs4 import BeautifulSoup
import requests


class Solution:
    def remove_punctuation(self, text):
        # 使用正则表达式去除标点符号,\w匹配字母、数字和下划线，\s匹配空格，[^]取反，表示匹配除了这些字符之外的所有字符，也就是标点符号。re.sub方法将匹配到的标点符号替换为空字符串，从而得到一个没有标点符号的文本。
        punctuation_pattern = r'[^0-9\.]'
        no_punctuation = re.sub(punctuation_pattern, '', text)
        return no_punctuation

    def BoxOfficeSpiderMine(self, movie_name: str) -> list:
        response = requests.get('http://72.itmc.org.cn/JS001/open/show/box_office_on_a_certain_day.html')
        response.encoding = 'utf-8'
        text = response.text
        result = []

        soup = BeautifulSoup(text, "html.parser")
        table = soup.find('table')
        movieName = table.find(string=movie_name)
        releaseInfo = movieName.find_parents(class_="name-wrap")[0].find("span", class_="releaseInfo").text
        if releaseInfo == "上映首日":
            result.append(0)
        elif releaseInfo == "点映":
            result.append(-1)
        else:
            result.append(int(self.remove_punctuatsion(releaseInfo)))

        tds = movieName.find_parents("tr")[0].find_all("td")
        boxDesc = tds[1].find(class_="boxDesc-wrap").text
        result.append(float(boxDesc))

        countRate = self.remove_punctuation(tds[1].find(class_="countRate-wrap").text)
        result.append(round(float(countRate) / 100, 3))
        return result

    def BoxOfficeSpider(self, movie_name: str) -> list:
        # 下载网页源代码
        res = requests.get('http://72.itmc.org.cn/JS001/open/show/box_office_on_a_certain_day.html')
        # 编码转换
        res.encoding = 'utf-8'
        # 网页解析，注意bs4
        soup = BeautifulSoup(res.text, 'html.parser')

        # 因为网页源代码部分标签不完整，所以不能用之前先查找电影名所在的节点来进行其他信息的查找的方法
        # 只能进行遍历，判断其电影名是否是 movie_name
        # 如果是的话，再进行其他信息的查找
        for i in soup.find('tbody', class_='table-body').find_all('tr'):
            # tr节点包含某个电影的所有信息
            # 判断tr节点中是否存在目标电影名 movie_name 所在的节点
            # 如果tr节点中存在目标电影，则进行信息查找
            if i.find('p', class_='movie-name').string == movie_name:
                # 上映时间
                if '点映' in i.find('span', class_='releaseInfo').string:
                    date = -1
                elif '首日' in i.find('span', class_='releaseInfo').string:
                    date = 0
                else:
                    date = int(i.find('span', class_='releaseInfo').string.replace('上映', '').replace('天', ''))

                # 综合票房
                sales = float(i.find('div', class_='boxDesc-wrap red-color').string)

                # 排片占比
                # 百分号转换、小于号去除
                # 因为精度问题，如果不保留小数，则结果不准确，所以进行小数的保留，数据都是三位的，所以保留三位小数
                rat = round(
                    float(i.find('div', class_='countRate-wrap').string.replace('%', '').replace('<', '')) / 100, 3)
        return [date, sales, rat]


print(Solution().BoxOfficeSpider("金刚川"))
print(Solution().BoxOfficeSpider("一日成交"))
print(Solution().BoxOfficeSpider("翱翔雄心"))
