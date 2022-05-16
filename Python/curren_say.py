import re
from decimal import Decimal

trans_dict = {
	'零':0,'壹':1,'贰':2,'叁':3,'肆':4,'伍':5,
	'陆':6,'柒':7,'捌':8,'玖':9,'拾':10,
	'佰':100,'仟':1000,'万':10000,'亿':100000000,
	'角':0.1,'分':0.01
	}

def curren_say_cn(amount):
	format_word = ["元",
	"拾", "佰", "仟", "万",
	"拾", "佰", "仟", "亿",
	"拾", "佰", "仟", "万",
	"拾", "佰", "仟"]
	format_word_decimal = ['分', '角']
	format_num = {'0': "零", '1': "壹", '2': "贰", '3': "叁", '4': "肆", '5': "伍", '6': "陆", '7': "柒", '8': "捌", '9': "玖"}
	result = []
	if '.' not in amount:
		k = len(amount) - 1
		for i in amount:
			result.append(format_num[i])
			result.append(format_word[k])
			k -= 1



def curren_say_en(amount):
	pass