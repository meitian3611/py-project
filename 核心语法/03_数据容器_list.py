# arr = [1, 2, 3, "python", "hello", "world", True]
# del arr[2]
# for i in arr:
#     print(i)

# print(arr[0:3:1])  # 截取指定长度 0 ~ 3（不包含3），开始索引：结束索引：步长
# print(arr[:3])  # 简化版本，默认从0开始 步长也默认是1

"""
append-尾插
insert-指定索引前插入元素
remove("hello")-移除第一个匹配到的元素
pop(0)-删除指定索引元素
sort-排序
reverse-反转
"""

# 最小 最大 平均值
"""
user_input = [1, 5, 9, 12, 33, 64, 3, 2, 7, 6]
user_input.sort()
print(min(user_input), max(user_input), sum(user_input) / len(user_input))

users = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 25},
    {"name": "mt", "age": 55}
]
info = max(users, key=lambda x: x["age"])
print(info['name'])
"""

"""
# 合并 去重
list1 = [1, 1, 2, 3, 4, 3]
list2 = [5, 7, 6, 8, 6, 7, 8]

# list1.extend(list2)
# list3 = [*list1, *list2]  # 解包
list3 = list1 + list2

new_list = []
for item in list3:
    if item not in new_list:
        new_list.append(item)

print(new_list)
"""

# 列表推导式 --- 列表名称 = [ 要插入的数据 for i in list_arr if 条件判断]
list_1 = [i ** 2 for i in range(1, 31) if i % 3 == 0 or i % 5 == 0]  # 能被3或5整除并且取这些数字的平方
list_2 = [i for i in [1, -5, -3, 45, 36, 66, -9] if i > 0]  # 提取正数
print(list_1)
print(list_2)
