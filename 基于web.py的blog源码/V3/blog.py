#coding:utf8
import web
import model


### Url mappings
#第一部分是匹配URL的正则表达式，像/、/help/faq、/item/(\d+)等(\d+将匹配数字)。
#定义urls的元祖

urls = (
    '/', 'Index',                        #这行表示我们要URL/(首页)被一个叫index的类处理, #请求的映射在urls元组中，如上图中GET ip:port/，会直接调用index类的GET方法
    '/help','Help',                       #定义用一个help的url，由Help类去处理

)


### Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates/')  #这会告诉web.py到你的模板目录中去查找模板。不要加base


class Index:

    def GET(self):
        """ Show page """
        posts = model.get_posts()       #引用model下的getpost方法
        return render.index(posts)      #posts渲染到index.html页面上


#定义Help类
class Help:
    def GET(self):                   #当有人用GET请求/时，这个GET函数随时会被web.py调用,GET 方式请求URL，class index中包含了一个GET方法，用来处理与index相应的url的GET请求的，
        """ Show page """
         # return render.ss()
        ss = model.new_select()
        return render.help(ss)                          # 把 ss 渲染到help.html
        # return ss
        #return "this is help page....0324-1611"                       #读取数据库的内容







app = web.application(urls, globals())             #现在我们需要创建一个列举这些url的application。

if __name__ == '__main__':
    app.run()