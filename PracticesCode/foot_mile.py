#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
    英制单位-平方英尺和公制单位-平方米互换

    Version：0.1
    Author：Tester
'''

value = float(input('请输入房间大小：'))
unit = input('请输入单位（sq.m或sq.ft）：')
if unit == 'sq.ft':
    print('%f平方英尺 = %f平方米' %(value,value*0.0929))
elif unit == 'sq.m':
    print('%f平方米 = %f平方英尺'%(value,value*10.7639))
else:
    print('请输入有效地单位')
