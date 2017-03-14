#Python3
#python基础
#dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
}
d['Paul'] = 75  # 添加元素
print(d)

# 输出十位大于个位数的数字
for x in range(1,10):
    for y in range(x+1,10):
        print(x*10+y)

# dict访问
# 方法1
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print "Adam:", d.get('Adam')
print "Lisa:",d['Lisa']
if 'Bart' in d:
    print "Bart:",d['Bart']
# 方法2
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in ['Adam', 'Lisa', 'Bart']:
    print "%s: %d"%(key, d[key])

# 遍历dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print "%s : %d"%(key,d[key])

# 小写set集合
L=['Adam', 'Lisa', 'Bart', 'Paul']
M=[]
for x in L:
    y=x.lower()
    M.append(y)
s = set(M)
print 'adam' in s
print 'bart' in s

# 判断用户输入是否在集合中 set
months = set(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'

# 对set数据元素打印
#-*- coding:utf-8 -*-
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0],':',x[1]
# 由于 set 里面的每一个元素都是 tuple 类型数据，所以可以对每个 set 里面的元素使用tuple 元素访问方式访问并读取

# 添加或删除set集合中的元素
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print s

# sum()函数计算1*1 + ... + 100*100
L = xrange(1, 101)
print sum([i*i for i in L])

# def()接受一个List返回每个元素平方和
def square_of_sum(L):
    return sum([i * i for i in L])

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

# 一元二次方程两个解
import math

def quadratic_equation(a, b, c):
    de=b**2-4*a*c
    if de>=0:
        x1=(-b+math.sqrt(de))/(2*a)
        x2=(-b-math.sqrt(de))/(2*a)
        return x1,x2
    else:
        return

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

# 汉诺塔移动
#请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：
#move(n, a, b, c)
#例如，输入 move(2, 'A', 'B', 'C')，打印出：
#A --> B
#A --> C
#B --> C
#-*- coding:utf-8 -*-
# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到b柱子上面去
#-*- coding:utf-8 -*-
def move(n, x, y, z):
    if n==1:
        print x,'-->',z
        return
    move(n-1,x,z,y)#将前n-1个盘子从x移动到y上
    move(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
    move(n-1,y,x,z)#将y上的n-1个盘子移动到z上
move(4, 'A', 'B', 'C')

# 函数默认参数
def greet(name='world'):
    print "Hello,%s." % name

greet()
greet('Bart')

# 可变参数函数 *args
def average(*args):
    if len(args)!=0:
        return sum(args)*1.0/len(args)
    else:
        return 0.0

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)

# 对list进行切片
L = range(1, 101)

print L[:10]
print L[2::3]
print L[4:50:5]

# 利用倒序切片对 1 - 100 的数列取出：
L = range(1, 101)
print L[-10:]  #  最后10个数；
print L[-46::5] # 最后10个5的倍数。

# 利用切片将首字母大写
def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')

# 循环迭代打印7的倍数
for i in range(1, 100)[6::7]:
    print i

# 使用 enumerate() 函数索引元素
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index, '-', name

# 两个表合二为一打印
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index+1, '-', name

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L)+1), L):
    print index, '-', name