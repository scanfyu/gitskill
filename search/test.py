

# str.find(str, beg=0, end=len(string)) 方法介绍
'''
text = "all zip files are zipped" 
print text.find('zip',text.find('zip') + 1)
'''

page = ('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=') # 找到链接所在位置
start_quote = page.find('"', start_link) # 链接前引号位置
end_quote = page.find('"', start_quote + 1) # 链接结尾的引号
url = page[start_quote+1 : end_quote] # 输出引号之间的内容

print url

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
