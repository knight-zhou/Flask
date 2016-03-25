#coding:utf8
import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):                             #get方式请求url跳到hello_from.html界面
        return render.hello_form()            #渲染到模板下的hello_from界面,从而能指定url获取post数据

    def POST(self):                                            #通过post方式获取数据
        # form = web.input(name="Nobody", greet="Hello")
        form = web.input(name="", greet="")

        greeting = "%s, %s" % (form.greet, form.name)    # 声明一个元祖
        return "you post data is:", greeting      #不渲染，直接输出提交的内容.    使用print返回null值所以一定要用return
        # return "your post name is:",form.name   #只输出名字

        # return type(greeting)         #  这是unicode 类型
        # return greeting[1]   #只输出问候

        # return render.index(greeting = greeting)  #渲染到模板下的index界面

if __name__ == "__main__":
    app.run()