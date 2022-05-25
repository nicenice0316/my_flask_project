# 求最长递增子序列
# [1, 5, 2, 4, 3]


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


if __name__ == '__main__':
    # num_list = [1, 5, 2, 4, 3]
    # fun(num_list)
    fun2()
    # print(res)
