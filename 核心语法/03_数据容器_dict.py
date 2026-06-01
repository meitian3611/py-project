"""
字典(dict)
使用键值对 (key:value)来存储数据
键不能被修改，不能重复
"""
from random import choice

# dict1 = {
#     "王林": 680,
#     "韩立": 690,
#     "紫灵": 640,
#     "梅凝": 620,
# }
# 删除
# dict1.pop("梅凝")
# del dict1["梅凝"]

# 遍历
# for key, value in dict1.items():
#     print(key, value)


# 购物车系统 练习
shopping_cart = dict()
menu = """
########### 购物车系统 ##########
#         1. 添加购物车         #
#         2. 修改购物车         #
#         3. 删除购物车         #
#         4. 查询购物车         #
#         5. 退出购物车         #
###############################
"""
print("欢迎使用购物车系统~")

while True:
    print(menu)
    choice = input("请选择要执行的操作(1-5)：")
    match choice:
        case "1":  # 添加
            goods_name = input("请输入商品名称:")
            goods_price = float(input("请输入商品价格:"))
            goods_num = int(input("请输入商品数量:"))

            # 商品存在 不执行添加逻辑
            if goods_name in shopping_cart:
                print("商品名称已存在! 请重新选择")
                continue
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完成")
                print(shopping_cart)
        case "2":  # 修改
            goods_name = input("请输入要修改的商品名称:")
            if goods_name not in shopping_cart:
                print("没有找到商品名称！")
                continue
            else:
                goods_price = float(input("请输入要修改的商品价格:"))
                goods_num = int(input("请输入要修改的商品数量:"))
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品修改完成")
        case "3":  # 删除
            goods_name = input("请输入要删除的商品名称:")
            if goods_name not in shopping_cart:
                print("没有找到商品名称！")
                continue
            else:
                del shopping_cart[goods_name]
                print("商品删除成功")

        case "4":  # 查询
            for name, info in shopping_cart.items():
                print(f"商品名称：{name},商品价格：{info['price']},商品数量{info['num']}")
        case "5":
            print("成功退出购物车系统")
            break
        case _:
            print("不支持的操作！！！")
