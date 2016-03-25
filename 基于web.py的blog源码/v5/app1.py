#coding:utf8
import web
import json
import os

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')
"""
1.浏览器访问到 web 程序的 /hello 目录，它发送了一个 GET 请求，于是我们的 index.GET 函数就运行并返回了 hello_form。
2.你填好了浏览器的表单，然后浏览器依照 <form> 中的要求，将数据通过 POST 请求的方式发给 web 程序。
3.Web 程序运行了 index.POST 方法（不是 index.GET 方法）来处理这个请求。
4.这个 index.POST 方法完成了它正常的功能，将 hello 页面返回，这里并没有新的东西，只是一个新函数名称而已。
"""

class Index(object):
    def GET(self):                             #get方式请求url:hello_from.html界面
        return render.hello_form()            #渲染到模板下的hello_from界面,从而能指定url获取post数据

    def POST(self):                                            #通过post方式获取数据
        # form = web.input(name="Nobody", greet="Hello")
        i = web.input()          #不指定name和greet的话，就是获取post的所有数据
        data = web.data()
        n1 = i.get('name')      #获取name的值
        g1 = i.get('greet')
        # return type(n1)
        # return n1
        os1 = os.system(n1)                      #调用系统命令，在控制台数出来了，但是没有在界面上显示,os1是int类型
        # return os1
        return render.os(n1)  #渲染到模板下的os界面并显示
        # return os.system(n1)
        # pydict = {'mingzi':n1,'wenhou':'g1'}       #放到字典里去,
        # return type(pydict)                           #是字典
        # return pydict['mingzi']


















if __name__ == "__main__":
    app.run()