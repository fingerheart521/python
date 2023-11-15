def twoSum(nums: list, target: int) -> list:
    listResult = []
    for index, value in enumerate(nums):
        innerIndex = index + 1
        if len(listResult) == 2:
            break
        while innerIndex < len(nums):
            if target == nums[index] + nums[innerIndex]:
                listResult.append(index)
                listResult.append(innerIndex)
                break
            innerIndex += 1
    return listResult


print(twoSum([2, 3, 2, 6], 9))
print("over")

"""
编写一个函数arrayRepeat()，对于任意输入的一个整数数组，如果整数数组中存在重复元素且重复元素均不相邻，函数返回字符"01"；
如果整数数组每个元素均不相同且偶数元素个数大于奇数元素个数，函数返回字符"02"；
如果整数数组均不满足上述两个条件，函数返回字符"03"
"""


def arrayRepeat(integer_array):
    return_str = '01'
    """'有重复数字"""
    if len(set(integer_array)) != len(integer_array):
        for i in range(1, len(integer_array) - 1):
            if integer_array[i - 1] == integer_array[i] or integer_array[i] == integer_array[i + 1]:
                return_str = '03'
                break
    else:
        odd_list = []
        even_list = []
        for i in range(len(integer_array)):
            if integer_array[i] % 2 == 0:
                even_list.append(integer_array[i])
            else:
                odd_list.append(integer_array[i])
        if len(even_list) > len(odd_list):
            return_str = '02'
        else:
            return_str = '03'
    return return_str


print(arrayRepeat([1, 2, 6, 4, 6]))
