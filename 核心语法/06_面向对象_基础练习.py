"""
面向对象的编程思想-教务管理系统
"""


# 定义学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        score = self.chinese + self.math + self.english
        return f"""
        姓名: {self.name}
        语文: {self.chinese}
        数学: {self.math}
        英语: {self.english}
        总分: {score}"""

    # 修改操作
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


# 定义教务管理系统类
class EduManagement:
    sys_version = 1.0
    sys_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    # 添加学生信息
    def add_student(self):
        name = input("请输入学生的姓名: ")

        # 判断学生是否存在,不能重复添加
        for s in self.student_list:
            if s.name == name:
                print("该名学生已经存在!!!")
                return

        chinese = int(input("请输入语文成绩: "))
        math = int(input("请输入数学成绩: "))
        english = int(input("请输入英语成绩: "))

        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print("添加学生信息成功~")
        else:
            print("成绩需要在 0-100 之间!!!")

    # 修改学生信息
    def update_score(self):
        name = input("请输入需要修改的学生姓名: ")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                print(f"当前学生信息: {s}")

                chinese = int(input("请输入语文成绩: "))
                math = int(input("请输入数学成绩: "))
                english = int(input("请输入英语成绩: "))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("修改学生信息成功~")
                    print(f"修改后学生信息: {s}")
                    return
                else:
                    print("成绩需要在 0-100 之间!!!")
                    return

        print("没有找到对应的学生!")

    # 删除学生成绩
    def delete_score(self):
        name = input("请输入需要删除的学生姓名: ")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除学生信息成功~")
                return

        print("没有找到对应的学生!")

    # 查询学生成绩
    def query_score(self):
        name = input("请输入需要查询的学生姓名: ")
        # 判断学生是否存在
        for s in self.student_list:
            if s.name == name:
                print(f"查询学生的成绩: {s}")
                return

        print("没有找到对应的学生!")

    # 展示全部的学生成绩
    def query_students(self):
        for s in self.student_list:
            print(s)

    # 运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.sys_version}")
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("# 1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统  #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")

            choice = input("请输入要执行的操作指令(1-6): ")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_score()
                    case "3":
                        self.delete_score()
                    case "4":
                        self.query_score()
                    case "5":
                        self.query_students()
                    case "6":
                        print("bye~")
                        break
                    case _:
                        print("指令不正确,请重试")
                        continue
            except Exception:
                print("程序运行出错啦, 请重试~")


### 测试代码  执行当前文件才触发的逻辑
if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()
