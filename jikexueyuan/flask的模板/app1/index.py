#coding:utf8
#模板和路由是基础必须熟练掌握
#flask 的官方首页 http://jinja.pocoo.org/docs/dev/

from flask import Flask,render_template
app = Flask(__name__)

# 
# ##python中有html代码,代码乱不好维护
# @app.route('/')
# def hello():
#     return '<h1>hello world !!!</h1>'

##渲染到模板文件的html下
# @app.route('/')
# def hello_world():
#     return render_template("index.html")

#后台传值渲染到html界面上,传复杂的对象给模板引擎进行渲染，相当于我通过python脚本获取到的值，渲染网页界面上。
#这样就好理解了，通过渲染的模式我们就可以通过脚本的值发到传到html页面上
@app.route('/')
def hello_world():
    content = "aaaa"
    return render_template("index2.html",content = content)

#上面是通过一个简单的字符串，传到模板引擎，下面吧一个user对象传到模板引擎进行渲染然后网页呈现









if __name__=='__main__':
    app.run()

