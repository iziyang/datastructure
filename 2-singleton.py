# coding:utf-8

# 单例模式
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            # cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


# 测试
class Myclass(Singleton):
    a = 1


A = Myclass()
B = Myclass()

print id(A), id(B)
