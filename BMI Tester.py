#!/usr/bin/env python3
#this programme is used to test your BMI
#ver1.0 Copyright Leslie_Leung
height=float(input('Please input your height\n'))
weight=float(input('Please input your weight\n'))
BMI=weight/(height*height)
print('Your BMI is',BMI)
if BMI<18.5:
	print("a")
elif BMI>=18.5 and BMI<25:
	print("b")
elif BMI>=25 and BMI<28:
	print("c")
elif BMI>=28 and BMI<32:
	print("d")
else:
	print("e")
