"""
对象是基于类进行创建的
命名规范: 大驼峰命名  UserInfo
"""

"""
__dict__ 以字典的形式 存储对象的属性
__init__ 初始化方法 对象创建后自动调用 主要用于设置对象的初始状态
self 是方法的第一个参数,表示当前创建的实例对象
函数写在类里面  我们称为方法
魔法方法是类自动调用的,可以自己定义规则
类属性与实例属性,类属性是所有实例对象共享的
"""


# 定义一个类
class Car:
    # 定义类属性
    wheel = 4
    tax_rate = 0.1

    def __init__(self, brand, name, price):
        # 定义对象的实例属性
        self.brand = brand
        self.name = name
        self.price = price

    # 定义对象的方法
    def running(self):
        print(f"{self.brand}{self.name} 正在高速行驶")

    def total_price(self, discount, rate):
        """
        计算提车的总价格
        :param discount: 折扣
        :param rate: 税率
        :return: 落地价
        """
        total = discount * self.price + self.price * rate
        print(f"提车落地价是: {total}")

    # 定义魔法方法
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"  # 可以直接打印输出的值

    def __lt__(self, other):
        return self.price < other.price  # 可以自定义需要去对比的规则方式

    def __eq__(self, other):
        return self.price == other.price


# 创建对象
c1 = Car("BMW", "5系", 500000)
# print(c1.__dict__)
print(f"设置了__str__后的返回值是: {c1}")

# 使用对象中的方法
c1.running()
c1.total_price(0.75, 0.1)

# 使用魔法方法
c2 = Car("Audi", "A6", 500000)
print(f"c1的价格小于c2的价格吗: {c1 < c2}")
print(f"c1的价格等于c2的价格吗: {c1 == c2}")

# 获取类属性 两种方式
print(c1.wheel)
print(Car.tax_rate)
