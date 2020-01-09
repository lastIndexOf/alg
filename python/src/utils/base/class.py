
class static_cls(object):
    total_property = 11

    def __init__(self):
        self.not_static_property = 22

    def is_not_static(self, test: str):
        print(isinstance(test, str))

    @staticmethod
    def is_static(*args):
        print(args)


s = static_cls()


static_cls.total_property = 121231

s.is_not_static(test=12)
