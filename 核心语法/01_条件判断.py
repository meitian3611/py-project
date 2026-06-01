# total_amount = 10000
# get_amount = 0
# password = "1234567"
#
# user_password = input("请输入你的密码：")
# if user_password == password:
#     get_amount = float(input("取出金额："))
#     print(f"剩余金额是：{total_amount - get_amount}")
# else:
#     print("密码错误,请重试")
#

userId = "mmt"
password = "8888"

username = input("Enter your username: ")
if username != userId:
    print("用户名错误")
    exit()
user_password = input("Enter your password: ")

if user_password != password:
    print("密码错误")
    exit()

if username == userId and password == user_password:
    print("Welcome " + username)
else:
    print("请输入正确的用户名和密码")
