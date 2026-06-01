# global 关键字  改变外部全局变量
num = 100


def test_num():
    """
    改变全局变量的方式 global关键字
    :return:
    """
    global num
    num = 200


test_num()


# 不固定的参数
def test_num2(*args, **kwargs):
    """
    不固定参数的传递方式
    :param args: 位置参数 *args
    :param kwargs: 关键字参数 **kwargs
    :return:
    """
    print(args, kwargs)


test_num2(1, 2, 3, name="xiao", age=20)


# 函数形式的参数
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def test_num3(a, b, calc):
    """
    把其它函数作为参数进行传递调用
    :param a:
    :param b:
    :param calc: 函数
    :return:
    """
    return calc(a, b)


calc_num = test_num3(10, 20, add)

# 匿名函数------lambda的使用
data_list = ["aa", "b", "cccc", "def", "h", "da"]
data_list.sort(key=lambda item: len(item), reverse=True)


# data_list.sort(key=len) # 另一种方式


# 递归函数
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)

jc_num = jc(7)
print(jc_num)


