'''
任务详情
根据任务详情下方提供的网页（数量为1），完成商品搜索结果分析。
请将右侧的函数 itemSearch() 补充完整，使其能完成以下功能：
对于网页中出现的任一网店名称 ，函数返回以下信息，请将以上获取的信息保存在数组中，按顺序返回。

任务要求
该网店对应商品，是否参与满减促销（非满件促销），返回值为 True 或 False；
该网店对应商品的价格，是否存在会员价，如果存在，则返回会员价，返回类型为 float（保留1位小数），如果不存在，返回原始价格；
该网店对应商品的评论数，返回类型为 int；
如果该网店存在两个及以上商品，返回价格较高的商品信息；如果商品价格相同，返回搜索结果最靠前的商品信息；
链接地址在下方专题地址中给出，点击链接可以直接获取。

测试用例
输入："花花公子官方旗舰店"    输出：[False, 139.0, 4400]
解释：该网店价格最高的商品未参加满减促销活动，对应价格为139.0，商品评论数为4400

输入："陌芙丝欧旗舰店"           输出：[True, 139.0, 12000]
解释：该网店价格最高的商品参加满减促销活动，对应价格为139.0，商品评论数为12000

输入："合众服饰专营店"           输出：[True,118.0,10000]
解释：该网店价格最高的商品参加满减促销活动，对应价格为118.0，商品评论数为10000

说明
1. 会员价格是商品价格右边小字出现的价格信息；
2. 评论数为“1万+”就代表评论数为“10000”；
3. 函数接收“网店名称”这一变量，返回类型为数组；
4. 不得修改函数的名称；
5.“满减促销”和“满件促销”是不一样的概念；
6. 网页中存在相同店铺名称的商品，请注意甄别。

'''

import re

from bs4 import BeautifulSoup
import requests


class Solution:
    def convert_str_to_num(self, str_num):
        pattern = re.compile(r'(\d+(\.\d+)?万\+?|\d+)')
        match = pattern.search(str_num)
        if match:
            if '+' in match.group():
                number = int(float(match.group().replace('万+', '')) * 10000)
            elif '万' in match.group():
                number = int(float(match.group().replace('万', '')) * 10000)
            else:
                number = int(match.group())
            return number
        else:
            return int(str_num)

    def itemSearchMine(self, shop_name: str) -> list:
        url = 'http://72.itmc.org.cn/JS001/open/show/ecjd.html'
        # 从URL读取文本文件
        response = requests.get(url)
        response.encoding = 'utf-8'
        text = response.text
        result = []

        soup = BeautifulSoup(text, "html.parser")
        goods = soup.select("[id='J_goodsList'] ul li a:-soup-contains('" + shop_name + "')")
        # max = []
        for item in goods:
            li = item.find_parent("li")
            discount = len(li.select("i[data-tips='本商品参与满减促销']")) > 0

            pricePlus = li.select('.p-price span.price-plus-1') or li.select('.p-price strong')
            price = round(float(pricePlus[0].text.replace('￥', '')), 1)

            comment = self.convert_str_to_num(li.select('.p-commit a')[0].text)

            if len(result) == 0 or result[1] < price:
                result.clear()
                result.append(discount)
                result.append(price)
                result.append(comment)
        return result

    def itemSearch(self, shop_name: str) -> list:
        # 下载网页源代码
        res = requests.get('http://72.itmc.org.cn/JS001/open/show/ecjd.html')
        # 编码转换
        res.encoding = 'utf-8'
        # 网页解析
        soup = BeautifulSoup(res.text, 'html.parser')

        # 找到所有shop_name 店的商品信息
        pros_tag = soup.find_all('a', title=shop_name)

        # 为了判断商品价格，创建一个列表
        li = []
        # 遍历每一个商品信息
        for j in pros_tag:
            # 会员价
            vip_pr_tag = j.parent.parent.parent.find('span', class_='price-plus-1')
            # 判断是否存在会员价，如果存在，将价格float后放入列表 li 中，默认保留一位小数
            if vip_pr_tag:
                li.append(float(vip_pr_tag.em.string[1:]))
            else:
                # 如果会员价不存在，将原价 float 后放入列表 li 中，默认保留一位小数
                li.append(float(j.parent.parent.parent.find('div', class_='p-price').i.string))

        # 找到价格最高的商品信息
        # max(li)返回价格最高的商品的索引
        # pros_tag[li.index(max(li))]返回价格最高的商品的价格节点
        # .parent.parent.parent返回价格最高的商品的信息节点
        pro_tag = pros_tag[li.index(max(li))].parent.parent.parent

        # 判断商品是否满减
        # 因为属性'data-tips'中有‘-’，书写不规则，所以利用 attrs 来进行查找
        if pro_tag.find('i', attrs={'data-tips': '本商品参与满减促销'}):
            pref = True
        else:
            pref = False

        # 价格，之前已经找出来了，直接写上
        pr = max(li)

        # 评论数
        # 评论数有两种书写形式，一种如‘1.3万+’，一种如‘9876+’，要分别进行判断采集
        commit_str = pro_tag.find('div', class_='p-commit').a.string
        # 如果有‘万’字，去掉‘万+’后，乘 10000
        if '万' in commit_str:
            commit = int(float(commit_str[:-2]) * 10000)
        # 在这里要注意，因为有的评价节点的文本中可能包含换行符，所以，这里不能用索引获取，可以用split方法
        else:
            commit = int(commit_str.split('+')[0])
        return [pref, pr, commit]


print(Solution().itemSearch("潮龙涧男装专营店"))
print(Solution().itemSearch("花花公子官方旗舰店"))
print(Solution().itemSearch("陌芙丝欧旗舰店"))
print(Solution().itemSearch("合众服饰专营店"))
