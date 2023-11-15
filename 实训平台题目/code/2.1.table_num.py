import requests
from bs4 import BeautifulSoup


class Solution:
    '''给定一个由表格构成的网页，返回指定位置中的数字，数字类型要转换为 int 类型。

    后台给出指定位置，位置由行（row）和列（col）构成，如 row = 2, col = 1, 表示第二行第一列，对应的数字是 249；

    程序返回的数字必须是 int 类型，类型不正确将导致结果不正确；
    后台给出的所有的位置都在表格中，无需考虑边界情况；
    表格的第一行是列名，由 A-Z 构成，共 26 列；第一列是行索引，由 1-30 构成，共 30 行。'''

    def table_num(self, row: int, col: int) -> int:
        html = requests.get('http://72.itmc.org.cn/JS001/open/show/random-num/index.html')
        # print(html.text)
        soup = BeautifulSoup(html.text, "html.parser")
        # print(soup)
        table = soup.find('table')

        # 获取表格中的行和列数据
        rows = table.find_all('tr')
        cols = rows[row].find_all('td')

        # 获取指定位置的数据并转换为 int 类型
        data = cols[col].text
        return int(data)

print(Solution().table_num(29, 20))
print(Solution().table_num(23, 15))
print(Solution().table_num(10, 11))
