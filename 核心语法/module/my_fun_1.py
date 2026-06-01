__all__ = ['adds', 'subs']  # 指定控制被 from utils import * 引入的功能


def adds(a, b):
    return a + b


def subs(a, b):
    return a - b


def test1():
    print("----" * 10)



if __name__ == '__main__':          # __name__   当前文件的名称值为 __main__
    # 只在这个文件执行,其它文件调用不会触发
    test1()
