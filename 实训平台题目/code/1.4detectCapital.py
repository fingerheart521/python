"""给定一段英文句子，判断句中单词拼写是否满足以下规则。
除以下特殊情况外，句子中第一个单词首字母必须大写，其它所有单词小写：
1. 如果句中的某个单词或短语，字母全部为大写，则该单词或短语拼写正确。比如“USA”、“UK”、“JUST  DO  IT”等；
2. “Python”、“Java”、“MachineLearning”、“DataMining”四个单词必须为双引号中给出的形式，否则拼写不正确；
3. 如果句中单词为“数字+字母”的混合形式，比如“5G”，该单词所有字母全部大写。"""
import re

# print("1AB".istitle())
# print("1a".isalpha())

print("Python" == "python")


def check_sentence(st):
    words = st.split()  # 将句子分割成单词

    print(words)
    # 首个单词首字母大写，数字开头必须大写
    # 如果首个单词大写，必须全部大写
    word = words[0]
    if word[0].isdigit():
        if len(word[1:]) > 0 and not word[1:].isupper():
            return False
    else:
        if (word.lower() == "Python".lower() and word != "Python") or (
                word.lower() == "Java".lower() and word != "Java") or (
                word.lower() == "MachineLearning".lower() and word != "MachineLearning") or (
                word.lower() == "DataMining".lower() and word != "DataMining"):
            return False
        if not (word.isupper() or (word[0].isupper() and word[1:].islower())):
            return False

    for word in words[1:]:
        if word[0].isdigit():
            if len(word[1:]) > 0 and not word[1:].isupper():
                return False
        else:
            if word.lower() in ["python", "java", "machinelearning", "datamining"]:
                if (word == "Python") or (
                        word == "Java") or (
                        word == "MachineLearning") or (
                        word == "DataMining"):
                    continue
                else:
                    return False
            elif word.islower() or word.isupper():
                continue
            else:
                return False
    return True


# 检查是否包含形如“5G”的单词，这类单词所有字母全部大写
# for word in words:
#     if word.isalpha() and any(char.isdigit() for char in word):
#         if not word.isupper():
#             return False
print("check_sentence start")
print(check_sentence("5G will change the life and working of public"))
print(check_sentence("I love Python"))
print(check_sentence("I love python"))
print(check_sentence("python love me"))
print(check_sentence("JUST DO IT"))
print(check_sentence("I come from HK"))
print(check_sentence("I come from Python"))
print(check_sentence("Machinelearning is so hot"))
print("check_sentence end")


def repeated_substring_pattern(s):
    # 判断字符串s是否可以由它的子串重复多次构成
    if not s:
        return ''

    # 将字符串s与自身拼接后，去掉首尾各一个字符，然后检查原始字符串s是否还存在于拼接后的字符串中
    # 如果存在，那么说明s可以由它的子串重复多次构成，返回子串；否则返回整个字符串s
    return s if s not in (s + s)[1:-1] else repeated_substring_pattern(s[:-1])


# 测试代码
# print(repeated_substring_pattern("abcabc"))  # 输出 "abc"
# print(repeated_substring_pattern("abcd"))  # 输出 "abcd"

import random


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # 生成两个进制
        a1, a2 = random.randint(26, 100), random.randint(26, 100)
        # 生成两个模
        mod1, mod2 = random.randint(10 ** 9 + 7, 2 ** 31 - 1), random.randint(10 ** 9 + 7, 2 ** 31 - 1)
        n = len(s)
        # 先对所有字符进行编码
        arr = [ord(c) - ord('a') for c in s]
        # 二分查找的范围是[1, n-1]
        l, r = 1, n - 1
        length, start = 0, -1
        while l <= r:
            m = l + (r - l + 1) // 2
            idx = self.check(arr, m, a1, a2, mod1, mod2)
            # 有重复子串，移动左边界
            if idx != -1:
                l = m + 1
                length = m
                start = idx
            # 无重复子串，移动右边界
            else:
                r = m - 1
        return s[start:start + length] if start != -1 else ""

    def check(self, arr, m, a1, a2, mod1, mod2):
        n = len(arr)
        aL1, aL2 = pow(a1, m, mod1), pow(a2, m, mod2)
        h1, h2 = 0, 0
        for i in range(m):
            h1 = (h1 * a1 + arr[i]) % mod1
            h2 = (h2 * a2 + arr[i]) % mod2
        # 存储一个编码组合是否出现过
        seen = {(h1, h2)}
        for start in range(1, n - m + 1):
            h1 = (h1 * a1 - arr[start - 1] * aL1 + arr[start + m - 1]) % mod1
            h2 = (h2 * a2 - arr[start - 1] * aL2 + arr[start + m - 1]) % mod2
            # 如果重复，则返回重复串的起点
            if (h1, h2) in seen:
                return start
            seen.add((h1, h2))
        # 没有重复，则返回-1
        return -1


print(Solution().longestDupSubstring("abcabcd"))

# print(Solution().longestDupSubstring("abc"))
# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/longest-duplicate-substring/solutions/1171003/zui-chang-zhong-fu-zi-chuan-by-leetcode-0i9rd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


'''如果一个长度为 nnn 的字符串 sss 可以由它的一个长度为 n′n'n ′  的子串 s′s's ′  重复多次构成，那么：
nnn 一定是 n′n'n ′  的倍数；

s′s's ′  一定是 sss 的前缀；

对于任意的 i∈[n′,n)i \in [n', n)i∈[n ′ ,n)，有 s[i]=s[i−n′]s[i] = s[i-n']s[i]=s[i−n ′ ]。

也就是说，sss 中长度为 n′n'n ′  的前缀就是 s′s's ′
 ，并且在这之后的每一个位置上的字符 s[i]s[i]s[i]，都需要与它之前的第 n′n'n ′
  个字符 s[i−n′]s[i-n']s[i−n ′ ] 相同。

因此，我们可以从小到大枚举 n′n'n ′ ，并对字符串 sss 进行遍历，进行上述的判断。注意到一个小优化是，因为子串至少需要重复一次，所以 n′n'n 
′  不会大于 nnn 的一半，我们只需要在 [1,n2][1, \frac{n}{2}][1, 2n ] 的范围内枚举 n′n'n ′  即可。

作者：力扣官方题解
链接：https://leetcode.cn/problems/repeated-substring-pattern/solutions/386481/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> str:
        n = len(s)
        length = 1
        found = False
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    length = i
                    found = True
                    break

        return s[0:length] if found else s
    def patternRepeatedSubstring(self, s: str) -> str:
        # 字串 ss 初始值
        ss = ''
        # 遍历 s 中的每个字符
        for i in s:
            # 每次对字串 ss 加上一个字符，然后判断 ss 是否为 s 的字串
            ss += i
            # 字串 ss 在 s 中的数量 == 字符串 s 的长度 / 字串 ss 的长度
            # 如 s 为‘abcabc’时，那么字串为‘abc’。字串在 s 中的数量：s.count(ss) = 2；两长度比：len(s) / len(ss) = 2。所以关系成立
            if s.count(ss) == len(s) / len(ss):
                return ss
        # 当 s 中不含有字串或字符串 s 为空字符串时，返回原字符串 s
        return s


print(Solution().repeatedSubstringPattern("abcdeabcde"))
print(Solution().repeatedSubstringPattern("abcdabcd"))
print(Solution().repeatedSubstringPattern("abcabc"))
print(Solution().repeatedSubstringPattern("abababab"))
print(Solution().repeatedSubstringPattern("aaaaaa"))
print(Solution().repeatedSubstringPattern("rerererererere"))
