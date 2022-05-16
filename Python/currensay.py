from decimal import Decimal


def num2money_format(change_number):
    """
    .转换数字为大写货币格式( format_word.__len__() - 3 + 2位小数 )
    change_number 支持 float, int, long, string
    """
    format_word = ["元",
                   "拾", "佰", "仟", "万",
                   "拾", "佰", "仟", "亿",
                   "拾", "佰", "仟", "万",
                   "拾", "佰", "仟"]

    format_word_decimal = ['分', '角']

    format_num = {'0': "零", '1': "壹", '2': "贰", '3': "叁", '4': "肆", '5': "伍", '6': "陆", '7': "柒", '8': "捌", '9': "玖"}

    res = []  # 存放转换结果

    if '.' not in change_number:
        # 输入的数字没有'.'，为整元，没有角和分
        k = len(change_number) - 1
        for i in change_number:
            res.append(format_num[i])
            res.append(format_word[k])
            k = k - 1

    elif '.' in change_number:
        float_2_change_num = Decimal(float(change_number)).quantize(Decimal("0.00"))
        # 如果输入的字符串有“.”，则将其转换为浮点数后，四舍五入取两位小数
        # print(float_2_change_num)
        # print(type(float_2_change_num))

        depart = str(float_2_change_num).split('.')
        # 将四舍五入得到的浮点数整数部分和小数部分拆开，实现操作为：先将浮点数转为字符串类型，再以“.”为分隔符分开
        # print(depart)

        int_part = depart[0]  # 整数部分
        # print(int_part)

        decimal_part = depart[1]  # 小数部分
        # print(decimal_part)

        k = len(int_part) - 1
        for i in int_part:  # 整数部分转换
            res.append(format_num[i])
            res.append(format_word[k])
            k = k - 1

        m = len(decimal_part) - 1
        for i in decimal_part:  # 小数部分转换
            res.append(format_num[i])
            res.append(format_word_decimal[m])
            m = m - 1

    return ''.join(res)  # 返回结果

print('This script is shit!!!')
your_money = input()
result = num2money_format(your_money)
print(result)