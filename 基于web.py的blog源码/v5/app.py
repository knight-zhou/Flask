#coding:utf8
import web
import json

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
        form = web.input(name="", greet="")
        greeting = "%s, %s" % (form.greet, form.name)    # 字符串格式化输出
        aaa = form.greet
        bbb = form.name
        ccc = list(eval("(form.greet,form.name)"))        #转换成list
        # ccc = list(eval("(aaa,bbb)"))        #转换成list

        return ccc[0],ccc[1]
        # greeting = "form.greet, form.name"
       # return "you post data is:", greeting      #不渲染，直接输出提交的内容.    使用print返回null值所以一定要用return
        # return "your post name is:",form.name   #只输出名字

        # return type(greeting)         #  这是unicode 类型
        # return greeting[1]   #只输出问候

        # return render.index(greeting = greeting)  #渲染到模板下的index界面





if __name__ == "__main__":
    app.run()