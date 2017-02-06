# -*- coding: utf-8 -*-
# 链式调用

class Chain(object):
    
    def __init__(self, path=''):
        self._path = path
        
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
        
    def __str__(self):
        return self._path
        
    __repr__ = __str__