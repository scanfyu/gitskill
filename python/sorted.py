# -*- coding: utf-8 -*-
# 按姓名排序

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(i):
    return i[0] #按姓名排序

L2 = sorted(L, key = by_name)
print(L2)


# -*- coding: utf-8 -*-
# 按成绩排序

def by_score(t):
    return t[1] #按成绩排序

L3 = sorted(L, key = by_score)
print(L3)
