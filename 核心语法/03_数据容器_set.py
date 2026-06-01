"""
集合(set)是无序的 不能被索引，唯一的 不可重复的，可以被修改的容器

s1.intersection(s2) 或者符号 &   取交集（相同的元素）
s1.difference(s2) 或者符号 -     取差集（只出现在第一个集合的元素）
s1.union(s2)  或者符号 |         取并集（所有的元素）
"""
# s1 = {11, 87, 66, 71, 13, "156"}
# s1.add("112")
# s1.remove("112")
# print(s1)

a = {1, 2, 3, 9, 10}
b = {4, 2, 6, 8, 3}

# print(a.intersection(b))
print(f"交集：{a & b}")

# print(a.difference(b))
# c = {s for s in a if s not in b}  # 集合推导式
# print(c)
print(f"差集：{a - b}")

all_set = a | b
print(f"并集：{all_set}")

all_list = [*a, *b]
for item in all_set:
    print(f"{item} 总共出现了 {all_list.count(item)}次")
