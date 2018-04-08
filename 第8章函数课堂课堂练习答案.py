# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 21:18:13 2018

@author: micro
"""
def f_max(x,y,z):
    maxn=x;
    if y>maxn:
        maxn=y;
        if z>maxn:
            maxn=z
    return maxn

a=input("please input first number:",)
b=input("please input second number:",)
c=input("please input third number:",)
m=f_max(a,b,c)
print("a,b,c中最大值为：",m)



import math
def f_area(x,y,z):
# 海伦公式 p=(x+y+z)/2 S=sqart(p*(p-x)(p-y)(p-z))
    if(x+y>z and x+z >y and z+y>x):
        p=(x+y+z)/2
        temp=p*(p-x)*(p-y)*(p-z)
        S=math.sqrt(temp)
        print("三角形面积为：",S)
    else:
        print("对不起，您输入的边长大小不能构成三角形！")

a=float(input("请输入第一条边：",))
b=float(input("请输入第二条边：",))
c=float(input("请输入第三条边:",))
f_area(a,b,c)