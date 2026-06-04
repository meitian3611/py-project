"""
文件操作入门

资源释放: with open() 方法
    上下文管理器 核心作用就是确保资源总是被正确的获取和释放,即使是异常也会被正确释放
"""
import json
import csv

# 打开文件
with open("resources/text_info.txt", "r", encoding="utf-8") as f:
    # 读取文件
    content_list = f.readlines()
    for content in content_list:
        print(content.strip())

# 写入文件  没有找到就会创建新文件
with open("resources/text_write.txt", "w", encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑似地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")

# 追加
with open("resources/text_write.txt", "a", encoding="utf-8") as f:
    f.write("--------追加的文本----------")

"""
json模块的使用
    json.dump()  序列化操作 把python的字典对象输出成 json格式进行写入存储
    json.load()  反序列化操作 从文件读取 json格式, 将其反向序列化为 python字典格式
"""

# 写入json数据文件
user_info = {
    "name": "小美",
    "age": 18,
    "gender": "male",
    "hobby": ["reading", "swimming", "coding"]
}
with open("resources/user_info.json", "w", encoding="utf-8") as f:
    json.dump(user_info, f, ensure_ascii=False, indent=2)

# 读取json数据文件
with open("resources/user_info.json", "r", encoding="utf-8") as f:
    user_info = json.load(f)
    print(user_info)

"""  
csv 模块的使用
"""

with open("resources/user_info.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "gender", "hobby"])
    writer.writeheader()  # 写入表头

    # 单行写入
    # writer.writerow({"name": "小美", "age": 18, "gender": "male", "hobby": 'reading,swimming,coding'})
    # writer.writerow({"name": "小王", "age": 19, "gender": "female", "hobby": 'reading,swimming,coding'})
    # writer.writerow({"name": "小张", "age": 20, "gender": "male", "hobby": 'reading,swimming,coding'})

    # 多行写入
    writer.writerows([
        {"name": "小王", "age": 19, "gender": "female", "hobby": 'reading,swimming,coding'},
        {"name": "小张", "age": 20, "gender": "male", "hobby": 'reading,swimming,coding'}
    ])

# 读取
with open("resources/user_info.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("csv文件: ",row)