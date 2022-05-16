#数字转换成人民币大写,支持12位整数2位小数
from random import *#引入随机模块
#基本字符
float_unit_list=list('角分')#小数位大写列表
rmb_list=list('零壹贰叁肆伍陆柒捌玖')#人民币数字大写列表
unit_list=list('仟佰拾亿仟佰拾万仟佰拾元')#每一位的单位列表
special_index_list=[3,7,-1]#亿 万 元 单位列表
num_list=list(range(0,10))#数字列表
input_num_list=[]#数字串列表
num_dict={}#数字串字典
#模拟多次数字随机输入,可以改为input()
def random_nums():
	input_num_int=''#将输入值分为整数 小数点 小数 三部分
	input_num_point=''
	input_num_float=''
	for b in sample(num_list[1:],1):#第一位不能是0
		input_num_int+=str(b)
	for a in range(1,randint(1,12)):
		for b in sample(num_list,1):#从num_list该样本中随机提取一位数字
			input_num_int+=str(b)
	if choice([0,1])==1:#是否小数
		input_num_point='.'
		for a in range(0,randint(1,2)):
			for b in sample(num_list,1):
				input_num_float+=str(b)
	return input_num_int+input_num_point+input_num_float#返回一串数字
for n in range(100):#随机100个数字串,将每串数字添加到数字串列表
	input_num_list.append(random_nums())
#数字处理
def num_progress(num):
	num_int_list=[]#处理时 把数字串分为 整数 小数列表
	num_float_list=[]
	rmb_num_int_list=[' 'for n in range(12)]#整数大写占位列表
	zheng=''#整
	rmb_num_float_list=[' ',' ']#小数大写占位列表
	result_int=''#结果整数值
	result_float=''#结果小数值
	if '.' not in num:#如果没有小数
		if len(num)>12:#如果输入值超过十二位提示错误
			return 'More than 12 digit integer cannot be converted! You entered a %s digit integer.'%len(num)
			#'%s'%* 表示把*转换为str后应用在%s处
		if len(num)<12:#如果小于十二位就先添加(12-输入值)这么多个的占位符
			num_int_list.extend(list(' ' for n in range(12-len(num))))
		num_int_list.extend(list(num))#添加输入值,列表形式
		num_float_list.extend([' ',' '])#没有小数,小数部分两个占位符
		zheng='整'#没有小数时,人民币大写格式为***元整
	if '.' in num:#如果有小数
		num_split_list=num.split('.')#以小数点分隔
		if len(num_split_list[0])>12:#如果输入值整数位超过十二位提示错误
			return 'More than 12 digit integer cannot be converted! You entered a %s digit integer.'%len(num_split_list[0])
		if len(num_split_list[-1])>2:#如果输入值小数位超过十二位提示错误
			return 'More than 2 digit decimal cannot be converted! You entered a %s digit decimal.'%len(num_split_list[-1])
		if len(num_split_list[0])<12:#同上 不赘述
			num_int_list.extend(list(' ' for n in range(12-len(num_split_list[0]))))
		num_int_list.extend(list(num_split_list)[0])
		num_float_list.extend(list(num_split_list)[-1])
		if len(num_float_list)==1:#小数位数是1的时候,添加一个占位符
			num_float_list.extend(' ')
	#数字转汉字
	for s in range(12):#循环12次,因为整数有12位
		if num_int_list[s]!=' ':#除了占位符外
			rmb_num_int_list[s]=rmb_list[int(num_int_list[s])]+unit_list[s]#数字+单位
	#处理特殊情况
	for s in range(11):#对于前11位
		if num_int_list[s]=='0' and num_int_list[s+1]=='0':#如果两个0连写,减少一个0
			rmb_num_int_list[s]=' '
		if s not in [3,7] and num_int_list[s]=='0' and num_int_list[s+1]!='0':#剔除亿位和万位后如果有零要去除单位
			rmb_num_int_list[s]=rmb_num_int_list[s][0]
	for s in special_index_list:
		if num_int_list[s]=='0':
			rmb_num_int_list[s]=unit_list[s]#亿 万 元 单位时特殊情况
	for s in range(2):#循环2次,因为小数有2位
		if num_float_list[s]!=' ':#除了占位符外
			rmb_num_float_list[s]=rmb_list[int(num_float_list[s])]+float_unit_list[s]#数字+单位
			if num_float_list[0]=='0' and num_float_list[1]!='0':#如果有零要去除单位
				rmb_num_float_list[0]=rmb_num_float_list[0][0]
			if num_float_list[0]=='0' and num_float_list[1]==' ':#如果角为0没有分去除小数
				rmb_num_float_list[0]=' '
			if num_float_list[1]=='0':#如果 分 单位为0 去除0
				rmb_num_float_list[1]=' '
	#结果
	for n in range(12):#循环12次,因为整数有12位
		if rmb_num_int_list[n]!=' ':#除了占位符外
			result_int+=rmb_num_int_list[n]#整数结果
		if '亿万'in result_int:#如果 亿 万 这两个单位在前面的程序中处理后连到了一块 将 亿万 替换成 亿
			result_int=result_int.replace('亿万','亿')
	for n in range(2):#循环2次,因为小数有2位
		if rmb_num_float_list[n]!=' ':#除了占位符外
			result_float+=rmb_num_float_list[n]#小数结果
	return result_int+zheng+result_float#数字转换成人民币大写的结果
for num in input_num_list:#将数字串列表中的每一个添加到数字串字典,一一对应其转换结果
	num_dict[num]=num_progress(num)
print('input numbers\t|the results')
for key,value in num_dict.items():
	print('{0:16}|{1:30}'.format(key,value))#format()对齐
	#{0:16}中的0表示key的占位,16表示key的占位长度.{1:30}表示value的占位,30表示value的占位长度
#By Tonymot
#播放数上500评论区置顶放源码
#如果觉得本视频有用请一键三连支持一波~