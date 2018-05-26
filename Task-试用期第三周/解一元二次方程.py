# -*- coding: utf-8 -*-
def getInputs():
    a = input("请输入此方程的二次的系数：")
    b = input("请输入此方程的一次的系数：")
    c = input("请输入此方程的常数：")
    return a,b,c
def notRoot():
    print("此方程没有实数根")
def oneRoot(a,b):
    x=-b/(2*a)
    print("此方程的根为{}".format(x))
def twoRoot(a,b,c):
    x1=(-b+pow(b*b-4*a*c,0.5))/(2*a)
    x2=(-b-pow(b*b-4*a*c,0.5))/(2*a)
    print("此方程的实数根为{} {}".format(x1,x2))
def main():
    a,b,c=getInputs()
    if b*b-4*a*c<0:
        notRoot()
    elif b*b-4*a*c==0:
        oneRoot(a,b)
    else:
        twoRoot(a,b,c)
main()

