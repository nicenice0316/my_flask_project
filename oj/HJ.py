import itertools

def fun_13():
    a = 'I am a boy'
    n_list = a.split()
    n_list.reverse()

    print(n_list)
    print(' '.join(n_list))


def fun_16():
    target_cost, target_count = 1000, 5
    price_list = [[800, 2, 0], [400, 5, 1], [300, 5, 1], [400, 3, 0], [500, 2, 0]]
    for i in price_list:
        if i[2] == 0:
            print(i[0] * i[1], i[0])
        else:
            father_obj = price_list[i[2] - 1]
            aaa = i[0] * i[1] + father_obj[0] * father_obj[1]
            print(aaa, i[0])


def fun_66():
    temp_dict_1 = {'reset': 'reset what'}
    temp_dict_2 = {'reset board': 'board fault', 'board add': 'where to add',
                   'board delete': 'no board at all', 'reboot backplane': 'impossible',
                   'backplane abort': 'install first'}

    # input_cmd_list = ['reset', 'reset board', 'board add', 'board delet', 'reboot backplane', 'backplane abort']
    input_cmd_list = ['r b']
    res = []
    for input_cmd in input_cmd_list:
        temp_list = input_cmd.split(' ')
        if len(temp_list) == 1:
            temp_res = 'unknown command'
            for k in temp_dict_1.keys():
                if k.startswith(temp_list[0]):
                    temp_res = temp_dict_1[k]
                    break
            res.append(temp_res)
        elif len(temp_list) == 2:
            temp_res = 'unknown command'
            temp_k_list = []
            for k in temp_dict_2.keys():
                k1, k2 = k.split(' ')[0], k.split(' ')[1]
                if k1.startswith(temp_list[0]) and k2.startswith(temp_list[1]):
                    temp_k_list.append(k)
            if len(temp_k_list) == 1:
                temp_res = temp_dict_2[temp_k_list[0]]
            res.append(temp_res)
    print(res)


def fun_41():
    n = 3
    weight_list = [108, 29, 185]
    nums_list = [5, 2, 1]
    temp_list = []
    for i in range(len(weight_list)):
        for j in range(nums_list[i]):
            temp_list.append(weight_list[i])
    # set_res = {0, }
    # res_list = []
    # temp = 0
    # while temp_list:
    #     for i in temp_list:

    # for x in range(1, len(temp_list) + 1):
    #     temp = list(itertools.combinations(temp_list, i))
    #     for y in temp:
    #         set_res.add(sum(y))
    # print(len(set_res))

def fun_test():
    res_list = [29, 29, 108, 108, 108, 108, 108, 185]
    n = 8
    dp = []


if __name__ == '__main__':
    fun_41()
