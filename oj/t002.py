# 求最长递增子序列
# [1, 5, 2, 4, 3]
import math
import itertools
import collections


def fun(num_list):
    # 从第n个数出发
    memo = {}
    # for i in range(len(num_list) - 1):
    # if i ==
    # if num_list[i] <

    return


# 路灯问题
# 输入 [50, 70, 20, 70]
# 输出 20
# 输入 [50, 70, 20, 125]
# 输出 5
def fun2():
    n = 4
    # r_list = [50, 70, 20, 70]
    # r_list = [50, 70, 20, 125]
    r_list = [0, 0, 0, 300]
    s_e_list = []
    # 1、转化为区间列表
    for i in range(n):
        if i == 0:
            start = 0
            end = r_list[0]
        else:
            start = 100 * i - r_list[i]
            end = 100 * i + r_list[i]
        s_e_list.append([start, end])
    # 2、区间列表排序
    sort_list = sorted(s_e_list, key=lambda x: x[0])

    # 3、遍历，求未覆盖区域
    res = 0
    start_index = 0
    end_index = 0
    for j in range(n):
        now_s = sort_list[j][0]
        now_e = sort_list[j][1]
        if j == 0:
            end_index = now_e
            continue
        if now_s > end_index:
            res += (now_s - end_index)
            start_index = now_s
            end_index = now_e
        else:
            end_index = now_e if now_e >= end_index else end_index
    print(res)


def fun3(n):
    if n < 3:
        return 'false'
    if n == 3:
        return 'true'
    if n % 3 == 0:
        return fun3(n / 3)
    else:
        return 'false'


def fun4():
    numbers = [2, 3, 4]
    target = 6
    i, j = 0, len(numbers) - 1
    while i < j:
        now = numbers[i] + numbers[j]
        if now < target:
            i += 1
        elif now > target:
            j -= 1
        else:
            return [i + 1, j + 1]


def fun5():
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    matrix = [[1]]

    target = 2
    up, down = 0, len(matrix) - 1
    while up <= down:
        u_mid = up + (down - up) // 2

        if matrix[u_mid][0] == target:
            return True
        elif matrix[u_mid][0] < target:
            up = u_mid + 1
        elif matrix[u_mid][0] > target:
            down = u_mid - 1
    # print(down)
    left, right = 0, len(matrix[0]) - 1
    while left <= right:
        l_mid = left + (right - left) // 2
        print('666', l_mid)
        if matrix[down][l_mid] == target:
            return True
        elif matrix[down][l_mid] < target:
            left = l_mid + 1
        elif matrix[down][l_mid] > target:
            right = l_mid - 1
    return False


if __name__ == '__main__':
    # num_list = [1, 5, 2, 4, 3].sort()
    # enumerate
    # nums = [-1, 0, 1, 2, -1, -4]
    # s = 'a a a a '
    # n = 8
    strs_list = ["abca", "abc", "abca", "abc", "abcc"]
    min_len = max([len(i) for i in strs_list])

    print(min_len)



    #
    # temp_list = temp.split()
    # sss = ['i', 'h']
    # sss.insert(1, ' ')
    # print(sss)
    # print(''.join(sss))

    # temp_list.reverse()
    # print(temp_list)

    # str_counter = dict(collections.Counter(test_str))
    # # print(str_counter)
    # for k, v in str_counter.items():

    # for i in a:
    #     if sum(i) == 0:
    #         print(i)
    # print(a[0])
    # b = list(filter(lambda x: sum(x) == 0, a))
    # print(b)

    # fun(num_list)
    # s = fun3(45)

    # print(s)
    # print(res)
