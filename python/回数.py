# -*- coding: utf-8 -*-
# 找到回数

def is_palindrome(n):
    s=str(n)
    return s==s[::-1] and len(s)!=1
# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

# -*- coding: utf-8 -*-
def is_palindrome(n):
    s_n = str(n)
    # 个位数，不是回数
    if len(s_n) < 2:
        return False
    # 使用python切片，如果这个字符串正着和反着是一样的，则是回数
    if s_n == s_n[::-1]:
        return True

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

# 测试到10000

a=list(filter(lambda x:x>10 and str(x)==str(x)[::-1],range(1,10000)))
print(a)