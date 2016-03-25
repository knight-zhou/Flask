#coding:utf8
#这里可以是 其他通过脚本获取的一些变量，然后再blog.py引用并显然到html界面上
import os
name = 'tttt'
city = 'shenzhenccc'
#cwd= os.getcwd()

def Cwd():
    return os.getcwd()      #要想在入口文件获取值必须用return，不能用print, retrun用于访问对象,记住函数要有返回值就可以了

# Cwd()