#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import functools
import time

print('第二题')
def logA(*args):
    text =''
    def decorator(func):
        functools.wraps(func)
        def wrapper(*args1, **kw):
            b = (lambda :time.time())()
            print('%sbegin call \'%s\': %ss' % (text, func.__name__, b))
            f = func(*args1, **kw)
            e = (lambda :time.time())()
            print('%send call \'%s\': %ss' % (text, func.__name__, e))
            print('total time: %.10f' % (e-b))
            return f
        return wrapper
    if len(args) >0 and callable(args[0]):
        return decorator(*args)
    else: #instance(argsp[0],str)) or len(args) == 0
        if len(args) > 0:
            text = '[%s]' % args[0]
        return decorator

@logA('to run')
def test(str):
    print('runing function %s with para \'%s\'' % ('test', str))

@logA()
def test1(str):
    print('running function %s with para \'%s\'' % ('test', str))

@logA
def test2(str):
    print('running function %s with para \'%s\'' % ('test', str))

test('good')
print('--------------')
test1('good')
print('--------------')
test2('good')
print('--------------')