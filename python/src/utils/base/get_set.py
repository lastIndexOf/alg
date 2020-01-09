class attr(object):
    def __init__(self):
        self.name = 'name'

    def __get__(self, instance, cls):
        print('in attr get', self, instance, cls)
        return 111

    def __set__(self, instance, cls):
        print('in attr get', self, instance, cls)
        return 111


class test(object):
    __p = 1

    @staticmethod
    def stat(a):
        print(a)

    def __init__(self, legs):
        self.__legs = legs

    @property
    def arm(self):
        return self.__legs / 2


t = test(4)

print(t.arm)
test.stat(123123)
t.stat(12321312)