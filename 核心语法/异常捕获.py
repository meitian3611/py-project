"""
异常的处理
Exception: 捕获全部异常

--------------------------
try:
    代码逻辑
except Exception:
    捕获到异常后的处理方式
finally:
    无论代码正常还是异常都会执行到这里 (非必须)
"""

try:
    print("- - - - - - - - - -")
    print(my_name)
    print("- - - - - - - - - -")
except Exception as e:
    print(f"程序运行出错啦! 报错信息是: {e}")
finally:
    print("- - - - - - - - - - -")