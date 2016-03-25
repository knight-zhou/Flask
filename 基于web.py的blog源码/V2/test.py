#coding:utf8
import web
import model                     #导入模块，如果要导入里的属性和方法用 from model import *
# db = web.database(dbn='mysql', db='blog', host='localhost',user='root',pw='root')
# users = db.query('select * from student')
# for i in users:
#     print i.id

ss = model.new_select()      #访问model里的函数
for i in ss:
    print i.id,i.hp









