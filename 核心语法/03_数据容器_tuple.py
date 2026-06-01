"""
元组(tuple)是不可变的（只读），创建了就不能被修改
count()
index()
解包与扩展解包
"""
# t1 = (23,152,3,9)
# a,b,c,d = t1
# print(a,b,c,d)
#
# t2 = (1,2,3,4)
# *a,b,c = t2
# print(a,b,c)

students = (
    ("01", "小梅", 90, 88, 79),
    ("02", "彩仪", 84, 80, 95),
    ("03", "梦停", 81, 78, 87),
    ("04", "美眉", 77, 68, 69),
    ("05", "宝宝", 95, 72, 84),
)
# 输出每个学生总分和平均分
for sid, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total / 3
    print(
        f"{name}："
        f"语文{chinese} "
        f"数学{math} "
        f"英语{english} "
        f"总分{total} "
        f"平均分{avg:.2f}"
    )
print()
subjects = ["语文", "数学", "英语"]

for index, subject in enumerate(subjects, start=2):
    scores = [s[index] for s in students]

    print(
        f"{subject}："
        f"最高分{max(scores)} "
        f"最低分{min(scores)} "
        f"平均分{sum(scores) / len(scores):.2f}"
    )
