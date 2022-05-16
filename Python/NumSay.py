def amount_say_cn(num):
	num_dict = list('零壹贰叁肆伍陆柒捌玖')
	num_unit = list('仟佰拾亿仟佰拾万仟佰拾元')
	result = ''
	num_flag = False
	zero_flag = False
	if_int = False
	count = 0
	count2 = 8
	num = str(num)
	

# TODO:finish this function later
def num_say_en(num):
	pass

if __name__ == '__main__':
	print(num_say_cn(10001.23))