# LeetCode 1 两数之和
'''
方法一 暴力破解
两层循环，第二层循环要从i+1开始，减少循环次数，不然会超时
用时3308s
'''


def twoSum1(nums, target: int):
    result = [0 for i in range(2)]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result[0] = i
                result[1] = j
                return result


'''
方法二 哈希表法（字典）
空间换时间
把nums中的值与下标一一对应，然后用get（）方法返回字典内值为target-num1的下标，为了防止返回的自身下标，要保证j！=i，
用时40s
enumerate(nums)为python内置函数，返回列表nums中每个元素的下标及值
'''


def twoSum2(nums, target: int):
    hashmap = {}
    for index, num in enumerate(nums):
        hashmap[num] = index
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]


nums = [3, 3]
# [2,7,11,15]
target = 6

result = twoSum2(nums, target)
print(result)
