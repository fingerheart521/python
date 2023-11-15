# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出“和”为目标值的两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案，数组中元素不能重复输入。
# 请根据上面的要求，编写相应的算法，将右边的函数 twoSum() 补充完整。
#
# 举例
# 给定 nums = [2, 7, 11, 15]，target = 9；
# nums[0] + nums[1] = 2 + 7 = 9，返回[0, 1]。
# 你可以使用哈希表来解决这个问题。首先，遍历数组，将每个元素的值和它的索引存入哈希表。
# 然后，再次遍历数组，对于每个元素，计算目标值与该元素的差值。在哈希表中查找该差值对应的索引，如果找到，则返回该索引和当前元素的索引。
def twoSum(nums, target):
    # 创建哈希表
    hashmap = {}
    # 遍历数组，将每个元素的值和它的索引存入哈希表
    for i, num in enumerate(nums):
        hashmap[num] = i
    # 再次遍历数组，计算目标值与该元素的差值，并在哈希表中查找该差值对应的索引
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap and hashmap[complement] != i:
            # 找到差值对应的索引，返回该索引和当前元素的索引
            return [i, hashmap[complement]]
    return None


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        # 辅助值
        flag = True
        # 遍历数组nums
        for i in range(len(nums)):
            # 遍历 i 位置后面的数值，依次判断 i 位置的数值 与 其后面数值的和是否等于目标值 target
            for j in range(i + 1, len(nums)):
                # 如果相等，则将结果保存到a、b中
                if nums[i] + nums[j] == target:
                    # 取第一次满足要求的下标及下标和
                    if flag:
                        sum_ = i + j
                        i_, j_ = i, j
                        flag = False
                    # 如果有两个及以上满足的情况，取下标和最小的情况
                    if sum_ > (i + j):
                        i_ = i
                        j_ = j
        return [i_, j_]

    def twoSum(self, nums: list, target: int) -> list:
        # 遍历数组nums
        for i in range(len(nums)):
            # 遍历 i 位置后面的数值，依次判断 i 位置的数值 与 其后面数值的和是否等于目标值 target
            for j in range(i + 1, len(nums)):
                # 如果相等，则将结果保存到a、b中
                if nums[i] + nums[j] == target:
                    return [i, j]
