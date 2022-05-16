def rmb_in_words(num):
    obj_number = {
        '0': "零", '1': "壹", '2': "贰", '3': "叁", '4': "肆", '5': "伍", '6': "陆", '7': "柒", '8': "捌", '9': "玖",
    }
    arr_inner = ["", "拾", "佰", "仟"]
    arr_outer = ["", "万", "亿", "兆", "京"]
    arr_when_without_zero = arr_outer + ["元", "零"]
    arr_splited_number = list(str(round(num, 2)).split("."))
    above_zero, below_zero = arr_splited_number if len(arr_splited_number) == 2 else [arr_splited_number[0], '0']
    print(below_zero)

    def number_above_zero(remained_arr, curr_str, outer_idx, inner_idx):
        if len(remained_arr) == 0:
            return "人民币" + curr_str
        if inner_idx >= len(arr_inner):
            inner_idx = 0
            outer_idx += 1
        last_char = curr_str[0]
        curr_char = obj_number[remained_arr[-1]]
        remained_arr = remained_arr[:-1]
        if (last_char in arr_when_without_zero or inner_idx == 0) and curr_char == "零":
            curr_char = ""
        if curr_char != "" and curr_char != "零":
            curr_char += arr_inner[inner_idx]
        if inner_idx == 0:
            curr_char += arr_outer[outer_idx]
        return number_above_zero(remained_arr, curr_char + curr_str, outer_idx, inner_idx + 1)

    def number_below_zero(arr_below):
        if arr_below == '0':
            return "整"
        elif len(arr_below) == 1:
            return "整" if arr_below == ["0"] else f"{obj_number[arr_below[0]]}角整"
        elif len(arr_below) == 2:
            xtyCents, cent = map(lambda x: obj_number[x], arr_below)
            return f'{xtyCents}{"" if xtyCents == "零" else "角"}{cent}分'
        else:
            raise ValueError()

    return number_above_zero(above_zero, "元", 0, 0) + number_below_zero(below_zero)

if __name__ == '__main__':
    # arr_numbers = [1001,
    #                1001.0,
    #                100000.00,
    #                10001.12,
    #                10101.3,
    #                10000001.4,
    #                1234567890.12, ]
    # res_words = list(map(rmb_in_words, arr_numbers))
    # print(res_words)
    # try:
    #     assert res_words == ['人民币壹仟零壹元整',
    #                          '人民币壹仟零壹元整',
    #                          '人民币壹拾万元整',
    #                          '人民币壹万零壹元壹角贰分',
    #                          '人民币壹万零壹佰零壹元叁角整',
    #                          '人民币壹仟万零壹元肆角整',
    #                          '人民币壹拾贰亿叁仟肆佰伍拾陆万柒仟捌佰玖拾元壹角贰分']
    #     print("测试通过")
    # except AssertionError:
    #     print("测试失败")
    print(rmb_in_words(1001))
    print(rmb_in_words(1001.0))
    print(rmb_in_words(100000.00))
    print(rmb_in_words(10001.12))
    print(rmb_in_words(10101.3))
    print(rmb_in_words(10000001.4))
    print(rmb_in_words(1234567890.12))
