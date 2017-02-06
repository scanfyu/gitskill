class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, AttributeError):
        if AttributeError=='score':
            return 99                              #s.score
        if AttributeError=='age':
            return lambda:25                       #s.age()