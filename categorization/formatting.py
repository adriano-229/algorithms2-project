import math
import operator


def remove_keys(dic_list):
    lst = []
    for dic in dic_list:
        lst.append(list(dic.values()))
    return lst


def associate_names(names_lst, ele_lst):
    dic = {}
    # if len(names_lst) != len(ele_lst):
    #     raise Exception("associate_names error!")
    for i in range(len(names_lst)):
        dic[names_lst[i]] = ele_lst[i]
    return dic


def format_percentage(value, decimals=2):
    width = decimals + 3
    return f"{value:>{width}.{decimals}f} %"


def sort_present_dicc(dicc):
    tot = 0
    for value in dicc.values():
        tot += value
        if tot == 0:
            tot = math.ulp(0.0)
    for file, value in dicc.items():
        dicc[file] = (value / tot) * 100
    lst = dicc.items()
    lst = sorted(lst, key=operator.itemgetter(1), reverse=True)
    shown = 0
    for file, ans in lst:
        if ans == 0:
            break
        shown += 1
        print(f"{format_percentage(ans)} — {file}")
    return bool(shown)
