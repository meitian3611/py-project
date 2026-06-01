# 导入内置模块 导入自定义模块 导入包

"""
--------模块的导入与使用-----------
import 模块名                    import random                     random.randint(1, 100)
import 模块名 as 别名             import random as rd                rd.randint(1, 100)
from 模块名 import 功能名         from random import randint          randint(1, 100)
from 模块名 import 功能名 as 别名  from random import randint as rdt     rdt(1, 100)

--------注意路径问题,可以使用绝对路径来导入-------
"""

"""
        导入内置模块
"""
from random import randint

rd_num = randint(1, 100)
print(rd_num)

"""
        导入自定义模块
        
"""
from module.my_fun_1 import *

print(adds(1, 2))

"""
        导入包的指定模块
        from utils import *     这种导入包的方式,需要在__init__添加指定文件
        
"""
from utils import utils_fun_1

utils_fun_1.func1()
utils_fun_1.func2()

from utils import *

utils_fun_1.func1()
utils_fun_2.func1()

"""
        导入具体的模块功能
        
"""
from utils.utils_fun_2 import func1, func2

func1()
func2()

"""
        注意路径问题,可以使用绝对路径来导入
        
"""
from 核心语法.utils.utils_fun_2 import func1, func2

func1()
func2()
