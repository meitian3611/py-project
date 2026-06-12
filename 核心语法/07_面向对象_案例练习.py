"""
    面向对象方式的 图书管理系统
    抽象类 - 是一种只能被继承的类, 不能被实例化, 作用就是规定子类必须要实现某些方法, 强制子类遵守统一的代码规范
    python中的抽象类: 需要导入abc模块中的 ABC类 , abstractmethod抽象方法
"""
from abc import ABC, abstractmethod
import json


# 图书类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id  # 图书编号
        self.title = title  # 图书名称
        self.author = author  # 作者
        self.total_num = total_num  # 总数
        self.__current_num = total_num  # 当前数量

    # 借书
    def borrow_book(self):
        if self.__current_num > 0:
            self.__current_num -= 1
            return True
        return False

    # 还书
    def return_book(self):
        self.__current_num += 1

    # 获取当前数量
    def get_current_num(self):
        return self.__current_num


# 会员类 - 抽象类
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id  # 会员编号
        self.name = name  # 姓名
        self.__password = password  # 密码
        self.__borrowed_books = []  # 借阅的图书列表

    # 借书
    def borrow_book(self, book: Book):
        # 判断当前会员的借阅数量已经到了最大值
        if len(self.__borrowed_books) >= self.get_max_books():
            print("当前可借阅数量已经到了最大值")
            return False

        # 判断当前会员是否已经借阅了该书
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}借阅成功,书籍名称: {book.title}")
            return True
        else:
            print("借阅失败,书被借完了")
            return False

    @abstractmethod
    def get_max_books(self) -> int:
        # 抽象方法 -  等待子类去实现这个方法
        pass

    # 还书
    def return_book(self, book: Book):
        if book in self.__borrowed_books:
            if isinstance(book, Book):
                book.return_book()
            self.__borrowed_books.remove(book)
            print(f"还书成功,书籍名称: {book.title}")
        else:
            print("还书失败,没有借过该书")

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books


# 普通会员
class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3


# VIP会员
class VipMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level  # 会员等级

    def get_max_books(self) -> int:
        return 6 + self.vip_level


"""
    图书管理系统
    1. 登录
    2. 借书
    3. 还书
    4. 查询已借阅的图书
    5. 退出
"""


class LibraySystem:
    def __init__(self):
        self.books = {}  # 图书 字典格式 { 编号: book对象 }
        self.members = {}  # 会员 字典格式 { 卡号: member对象 }
        self.current_member: Member | None = None  # 当前登录的会员

        # 加载数据, 图书和会员
        self.load_book_data()
        self.load_members()

    def load_book_data(self):
        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book['编号']] = Book(book['编号'], book['标题'], book['作者'], book['数量'])
            print("图书数据加载完成")

    def load_members(self):
        with open("data/user.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                # 是否有会员等级 是否是会员
                if '会员等级' in member:
                    self.members[member['卡号']] = VipMember(member['卡号'], member['用户名'], member['密码'], member['会员等级'])
                else:
                    self.members[member['卡号']] = NormalMember(member['卡号'], member['用户名'], member['密码'])
            print("会员数据加载完成")

    def login(self):
        while True:
            print("----登录系统----")
            member_id = input("请输入会员卡号: ")
            password = input("请输入密码: ")

            # 判断会员卡号是否存在
            if member_id not in self.members:
                print("会员卡号不存在, 请重新输入")
                continue

            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() != password:
                print("密码错误, 请重新输入")
                continue

            print(f"登录成功, 欢迎{member.name}同学~")
            self.current_member = member
            return True

    # 借书
    def borrow_book(self):
        print("----借书系统----")
        # 打印展示所有图书
        for book in self.books.values():
            print(f"编号: {book.book_id}   标题: {book.title}   作者: {book.author}   总数: {book.total_num}   当前数量: {book.get_current_num()}")
        # 选择图书
        book_id = input("请输入要借阅的图书编号: ")
        if book_id not in self.books:
            print("图书编号不存在, 请重新选择")
            return
        self.current_member.borrow_book(self.books[book_id])

    # 还书
    def return_book(self):
        print("----还书系统----")
        # 获取当前会员的已借阅的图书
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) == 0:
            print("您没有已借阅的图书,无需还书")
            return

        # 显示已借阅的图书
        for book in borrowed_books:
            print(f"编号: {book.book_id}   标题: {book.title}   作者: {book.author}")

        book_id = input("请输入要还书的编号: ")
        book = self.books.get(book_id)

        if book is None:
            print("图书编号不存在, 请重新选择")
            return
        self.current_member.return_book(book)

    def query_borrowed_books(self):
        print("----已借阅的图书----")
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) == 0:
            print("您没有已借阅的图书")
        else:
            for book in borrowed_books:
                print(f"编号: {book.book_id}   标题: {book.title} ")

    def run(self):
        if self.login():
            while True:
                print("\n1. 借书")
                print("2. 还书")
                print("3. 查询已借阅的图书")
                print("4. 退出")
                choice = input("请输入要执行的操作(1-4): ")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.query_borrowed_books()
                    case "4":
                        print("退出系统成功!")
                        break
                    case _:
                        print("输入的操作有误, 请重新输入")


if __name__ == '__main__':
    ls = LibraySystem()
    ls.run()
