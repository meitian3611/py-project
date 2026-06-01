"""
1. 字符串是不能被索引下标修改，有序的，可迭代性的（可遍历）
2. 所有字符串相关的方法，都不会改变原来的字符串
"""
text = "hello python"

# find() 返回第一次索引的位置 没有就是-1
print(text.find('py'))

# count() 统计指定字符串出现的次数
print(text.count('h'))

# upper()转大写 lower()转小写
print(text.upper())
print(text.lower())

# split() 按指定内容分割成列表
print(text.split())

# strip() 去除首尾空白字符或者指定字符
print(text.strip())

# replace 替换指定字符串
print(text.replace("python", "world"))

# startswich()/endswith 检查是否指定字符开头或者结尾 返回布尔值
print(text.startswith("hello"))
print(text.endswith("python"))

# in 运算符  判断元素是否存在
print("hello" in text)



# 小练习  回文判断
test = "上海自来水来自海上"
print(f"这是一段回文：{test}" if test == test[::-1] else "不是回文")

# 小练习 字符串反转大写 记录在列表中
a = [input(f"输入第{s + 1}个字符串:")[::-1].upper() for s in range(5)]
for i in a:
    print(i)
