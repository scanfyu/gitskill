

# str.find(str, beg=0, end=len(string)) 方法介绍
''' 
text = "all zip files are zipped" 
print text.find('zip',text.find('zip') + 1)
'''

'''
寻找第二个
def find_second(search, target):
    first = search.find(target)
    return search.find(target, first + 1)
'''

page = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=') # 找到链接所在位置
start_quote = page.find('"', start_link) # 链接前引号位置
end_quote = page.find('"', start_quote + 1) # 链接结尾的引号
url = page[start_quote+1 : end_quote] # 输出引号之间的内容

print url

# 寻找下一个出现位置
danton = "De l'audance,"

print find_second(danton, 'audance')

# def <name>(<parameters>输入/input-> <name>, <name>, ...):
#     <block>

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print s[:-2] + t[-3:]

# 测试并获得一个数的整数部分，四舍五入
x = 3.14
y = 25.6

num = x + 0.5
s = str(num)
point = s.find('.')
print s[:point]

# 寻找第一个字母是D的
def is_friend(name):
    return name[0] == 'D' or name[0] == 'N'

print is_friend('Diane')

# 输出最大值
def biggest(a, b, c):
    return bigger(bigger(a, b), c)

max(a, b, c)

def bigger(a, b):
    if a > b:
        return a
    else:
        return b

# while 介绍
i = 0
while i < 10:
    print i
    i = i + 1