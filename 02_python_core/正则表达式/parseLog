# coding:utf-8
import re
import pandas as pd
# import cStringIO
from io import StringIO
from itertools import izip

# 以\[.*\]分割  并过滤空白元素
def func_split(ss):
	ss = re.split('\[.*\]', ss)
	return filter(str.strip, ss)


# 校验log文件正确性
def check_log(lst):
	if not lst:  # lst == []
		return False
	check_dct = {
		'[oneTestEnd]': '[oneTest]',
		'[chipInfoEnd]': '[chipInfo]'
	}
	# [oneTest\]|\[oneTestEnd\]|\[chipInfo\]|\[chipInfoEnd\] 任意一个不在 False
	temp = []
	# for one in lst:
	# 	if temp == []:


# 传入str（ONETEST、CHIPINFO...） 返回dict
def str_to_dct(s):
	# （1）将传入字符串以行分割
	# （2）不包含':'的元素被过滤
	# （3）以':'分割，组成字典
	_func = lambda x: re.sub('\s', '', x).split(':')  # 定义匿名函数,功能: 除去所有空白符后以':'分割
	# _lst = zip(*[_func(line) for line in s.splitlines() if ':' in line])  # dict
	# return pd.DataFrame(_lst[1:], columns=_lst[0])
	return [_func(line) for line in s.splitlines() if ':' in line]


def parse_log(path):
	# (1) 判断log文件合法性   （2）将[begin]从文件中截出来
	with open(path) as fp:
		text = fp.read()

	check_lst = re.finditer('\[oneTest\]|\[oneTestEnd\]|\[chipInfo\]|\[chipInfoEnd\]', text)
	check_log(check_lst)

	# 提取[begin]信息
	begin_info = re.findall('\[begin\](.*?)\[\w+\]', text, flags=re.DOTALL)
	# print str_to_dct(begin_info[0])
	# 提取[failBin]同上

	# 将每个芯片的测试信息分别提出来
	chip_info = re.findall('\[oneTest\](.*?)\[chipInfoEnd\]', text, flags=re.DOTALL)

	# 将每个芯片的每个测试项[oneTest]部分以及[chipInfo]部分分割出来
	chip_info = map(func_split, chip_info)

	for one_chip in chip_info:
		chip = one_chip.pop()  # chipInfo 信息
		# print str_to_dct(chip)
		for one_test in one_chip:
			print str_to_dct(one_test)
			print '*'*30
		print '-'*100


if __name__ == '__main__':
	path = 'log.txt'
	parse_log(path)
