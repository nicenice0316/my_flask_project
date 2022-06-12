# 德科机试一星题目 http://www.amoscloud.com/?cat=57

import itertools


def fun_1():
    def check_res(a, b):
        res_a = []
        res_b = []
        for i in range(1, a + 1):
            if a % i == 0:
                res_a.append(i)
        for i in range(1, b + 1):
            if b % i == 0:
                res_b.append(i)
        d = set(res_a) & set(res_b)
        if len(d) > 1:
            return False
        else:
            return True

    n, m = 1, 20
    nums = [i for i in range(n, m + 1)]
    print(nums)
    temp_list = list(itertools.combinations(nums, 3))
    gougu_list = []
    for i in temp_list:
        a = i[0]
        b = i[1]
        c = i[2]
        if a ** 2 + b ** 2 > m ** 2:
            continue
        if a ** 2 + b ** 2 == c ** 2:
            if check_res(a, b) and check_res(a, c) and check_res(b, c):
                gougu_list.append([a, b, c])
    print(gougu_list)


def fun_2():
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    res = []
    for i in nums1:
        for j in nums2:
            res.append(i + j)
    res.sort()
    target_list = res[:k]
    print(res)
    print(target_list)
    print(sum(target_list))


def fun_3():
    pass


def fun_4():
    n = 3
    dp = [0 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 1]
    print(dp[n])


def fun_5():
    max_test_nums = 4
    n = 5
    test_list = [5, 4, 1, 1, 1]
    remain = 0
    count = 0
    for i in test_list:
        if remain > 0:
            if remain + i <= max_test_nums:
                remain = 0
                count += 1
            else:
                count += 1
                remain = remain + i - n
        else:
            if i > max_test_nums:
                remain = i - max_test_nums
                count += 1
            else:
                count += 1
    x, y = divmod(remain, max_test_nums)
    ddd = x if y == 0 else x + 1
    # print(remain)
    print(count + ddd)


def fun_6():
    target_h = 100
    n = 10
    nums_list = [95, 96, 97, 98, 101, 99, 102, 103, 104, 105]
    nums_list.sort(key=lambda x: abs(x - target_h))
    for i in range(n - 1):
        a = abs(nums_list[i] - target_h)
        b = abs(nums_list[i + 1] - target_h)
        if a == b:
            if nums_list[i] > nums_list[i + 1]:
                nums_list[i], nums_list[i + 1] = nums_list[i + 1], nums_list[i]
    print(nums_list)


def fun_7():
    test_str = 'hello world!'
    s = 0
    e = 3
    test_list = test_str.split(' ')
    revers_list = test_list[s:e + 1]
    revers_list.reverse()
    res = test_list[0:s] + revers_list + test_list[e + 1:]
    print(test_list)
    print(res)
    print(' '.join(res))


def fun_8():
    nums_list = [23, 30, 40]
    target_num = 26
    combain_list = itertools.combinations(nums_list, 3)
    res = []
    for i in combain_list:
        if sum(i) > target_num:
            continue
        else:
            res.append(sum(i))
    if res:
        print(max(res))
    else:
        print(-1)


def fun_9():
    str_a = 'fach'
    str_b = 'bbaaccedfg'
    res = set()
    for i in str_b:
        if i in str_a:
            res.add(i)
    res = list(res)
    res.sort(key=lambda x: ord(x))
    res_str = ''.join(res)
    print(res_str)


def fun_10():
    a = 3
    b = 4
    nums = [256, 257, 258, 259, 260, 261, 262, 263, 264, 265]


def fun_11():
    ...


def fun_12():
    nums = [5, 10, 2, 11]
    nums.sort()
    target = 20
    max_count = 0
    for i in range(1, len(nums) + 1):
        temp = itertools.combinations(nums, i)
        for j in temp:
            if sum(j) <= target:
                max_count = i if max_count < i else max_count
    print(max_count)


def fun_13():
    ...


def fun_14():
    start_index = 4
    list_len = 6
    word_list = ['word', 'dd', 'da', 'dc', 'dword', 'd']
    res = word_list[start_index]
    word_list.pop(start_index)

    while True:
        temp = []
        for i in word_list:
            if i.startswith(res[-1]):
                temp.append(i)
        if not temp:
            break
        else:
            # 找到目标并且pop出去
            max_len = max([len(i) for i in temp])
            aa = []
            for i in temp:
                if len(i) == max_len:
                    aa.append(i)
            aa.sort()
            target_item = aa[0]
            res += target_item
            word_list.remove(target_item)
    print(res)


def fun_15():
    ...


def fun_16():
    ...


def fun_17():


if __name__ == '__main__':
    fun_14()
    # a = '6 cab ad abcd cba abc bca abc 1'
    # b = a.split(' ')
    # print(b[1:-2])

    # n = 5
    # check_res(6, 3)
    # print(res)
