#!/usr/bin/env python
#-*- coding=utf-8 -*-

import random

name = open('namelist.txt', 'r')
dic = dict()
for line in name:
	line = line.strip().split('.')
	dic[line[0]] = line[1]
print(dic)
name.close()


num = random.randint(1,3)
name_picked = dict['1']
print(name_picked)
print(num)
