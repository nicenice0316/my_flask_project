# 求最长递增子序列
# [1, 5, 2, 4, 3]
# 求连续子序列的最大和 9
# [3,-4,2,-1,2,6,-5,4]

# 记忆化搜索
memo = {}


def L(nums, i):
    # 数组中，从i开始的最长子序列。如果后面的
    if i in memo:
        return memo[i]
    if i == len(nums) - 1:
        return 1
    max_len = 1
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            max_len = max(max_len, L(nums, j) + 1)
    memo[i] = max_len
    return max_len


def length_of_LIS(nums):
    """
    [1, 5, 2, 4, 3]
    L(0) = max{L(1), L(2), L(3), L(4)} +1
    L(1) = max{L(2), L(3), L(4)} +1
    L(2) = max{L(3), L(4)} +1
    L(3) = max{L(4)} +1
    L(4) = 1
    然后从下往上计算
    """
    n = len(nums)
    L = [1] * n
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                L[i] = max(L[i], L[j] + 1)
    return max(L)


def fun_1(nums):
    """
    一、暴力搜索
    从1出发，当前最长序列长度是 3。从5出发，最长是1
    2出发，是2,4是1， 3是1
    每一个保存下来[3,1,2,1,1],结果最大值就是最长子序列长度
    """

    return max(L(nums, i) for i in range(len(nums)))


if __name__ == '__main__':
    nums = [1, 5, 2, 4, 3]
    # res = fun_1(nums)
    res = length_of_LIS(nums)
    print(res)
