# match case
"""
text = input("请输入你的操作指令：")
match text:
    case "上" | "w":
        print("角色向上移动")
    case "下" | "s":
        print("角色向下移动")
    case "左" | "a":
        print("角色向左移动")
    case "右" | "d":
        print("角色向右移动")
    case _:
        print("指令输入错误")
"""

# while循环语法
"""
total = 0
num = 1

while num <= 100:
    if num % 2 == 0:
        total += num
    num += 1

print(f"1-100之间偶数的和是: {total}")
print(f"1-100之间偶数的和是: {sum(range(2, 101, 2))}")
"""

# for循环
""" 
total = 0
for i in range(100, 501):
    if i % 3 == 0:
        total += i
print(total)
print(sum(range(1, 101, 2)))
"""

"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()

for i in range(1, 9):
    for j in range(1, 9):
        if i % 2 != 0:
            if j % 2 == 0:
                print("■", end=" ")
            else:
                print("□", end=" ")
        else:
            if j % 2 != 0:
                print("■", end=" ")
            else:
                print("□", end=" ")
    print()
"""

import random
radom_num = random.randint(1, 100)

while True:
    user_num = int(input("输入你猜的随机数: "))

    if user_num == radom_num:
        print(f"恭喜你猜对了，随机数为{radom_num}")
        break
    elif user_num > radom_num:
        print(f"输入的数字猜大了")
        continue
    else:
        print(f"输入的数字猜小了")


