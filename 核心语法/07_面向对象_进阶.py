"""
封装:
    将数据(属性)和操作数据的方法绑定在一起, 形成一个独立的单元(类), 保护数据不被外部访问, 通过访问修饰符实现封装
    1. 私有属性: 在属性名前面加双下划线__
    2. 私有方法: 在方法名前面加双下划线__
注意: python中是没有真正的私有机制的, 强行获取还是能够取到私有方法和属性
    例如: car._Car__owner
"""


class Car:
    __owner = "mtt"  # 私有属性
    wheel = 4
    tax_rate = 0.1

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def running(self):
        print(f"{self.__owner}的 {self.brand}{self.model} 正在高速行驶")

    # 私有方法
    def __get_owner(self):
        return self.__owner[0:1] + "**"


"""
继承
    描述两个类之间的关系, 子类继承父类, 就可以获取和使用父类的属性和方法
    calss FueCar(Car):  括号中填入需要继承的父类, 不填默认继承最高级别的object
    重写: super().方法名 或者 父类名.方法名(self)
多继承
    使用逗号分开, 第一个继承的父类优先级高
    class WenJieCar(Car,AiDriver)
"""


class FueCar(Car):
    fuel_types = "燃油"

    def running(self):
        # 重写父类方法
        # super().running() # 调用父类的方法
        Car.running(self)  # 调用父类方法, 这种方式更加清晰
        print(f"{self.brand} {self.model}正在以{self.fuel_types}方式行驶")


class AiDriver:
    def running(self):
        print("智能驾驶")


class WenJieCar(Car, AiDriver):
    def __init__(self, brand, model, price):
        Car.__init__(self, brand, model, price)

    def running(self):
        Car.running(self)
        AiDriver.running(self)
        print("子类--")


"""
多态
    同一个方法存在多种不同的形态,行为和表现
"""


class MtCar(Car):
    def running(self):
        print(f"{self.brand} {self.model}正在行驶")


def handle_car(car: Car):
    car.running()


#     Duck Typing 鸭子类型
#     多个类中存在同名的方法, 都可以是多态, 不依赖于继承关系
class Duck:
    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(f"{self.name}正在游泳")


class Dog:
    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(f"{self.name}正在游泳")


class Pig:
    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(f"{self.name}正在游泳")


def handle_swimming(duck: Duck):
    duck.swimming()


if __name__ == '__main__':
    car = Car("BMW", "X5", 100000)
    fue_car = FueCar("BMW", "X5", 100000)
    wen_jie_car = WenJieCar("BMW", "X3", 230000)

    handle_car(MtCar("Audi", "A4", 250000))

    handle_swimming(Duck('鸭子'))
    handle_swimming(Dog('狗'))
    handle_swimming(Pig('猪'))
