# 函数使用与编辑说明文档
def test_01(bottom, height):
    """
    根据三角形的底和高，用来计算三角形的面积
    :param bottom: 底
    :param height: 高
    :return: 面积
    """
    return round(bottom * height / 2, 2)


a = test_01(2, 5)


def test_02(text):
    """
    计算字符串包含元音字母的个数
    :param text: 字符串
    :return: 包含的个数
    """
    str_text = "aeiou"
    list_num = [text.lower().count(i) for i in str_text]
    return sum(list_num)


b = test_02("Student")
print(f"字符串包含元音字母的个数是：{b}")


def test_03(user_list):
    """
    计算列表中的最高分，最低分，平均分
    :param user_list: 所有人员的分数
    :return: 最高分，最低分，平均分
    """
    nums = [user['num'] for user in user_list]

    return max(nums), min(nums), round(sum(nums) / len(nums), 2)


users = [
    {
        "name": "王林",
        "num": 65
    },
    {
        "name": "韩立",
        "num": 85
    },
    {
        "name": "萧炎",
        "num": 70
    },
]
max_num, min_num, avg_num = test_03(users)
print(f"最高分是{max_num}")
print(f"最低分是{min_num}")
print(f"最高分是{avg_num}")
