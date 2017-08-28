# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:20:34 2017

@author: quanqi.yue
"""
###数字转换成汉字，在anaconda中输入时需要切换到英文，否则会报错
import datetime
begin = datetime.datetime.now()
number = list(str(int(input())))
begin = datetime.datetime.now()
unit = {'0':'千', '1':'', '2':'十', '3': '百'}
chinese = ['零','一','二','三','四','五','六','七','八','九']
liang = ['','零','万', '亿','兆']

for i in range(1, len(number) + 1):
	if number[-i] == '0':
		if i % 4 == 1 or i == len(number):
			number[-i] = ''
		elif number[-i + 1] in liang:
			number[-i] = ''
		else:
			number[-i] = '零'
	else:
		number[-i] = chinese[int(number[-i])] + unit[str(abs(-i) % 4)]

#for i in range(1, len(number) + 1):
	if i == 5:
		number[-i] += '万'
	elif i == 9:
			number[-i] += '亿'
	elif i == 13:
			number[-i] += '兆'

	number[-i] = number[-i].replace('一十', '十')
print(''.join(number))
end = datetime.datetime.now()
time = end - begin 
print(time,end)