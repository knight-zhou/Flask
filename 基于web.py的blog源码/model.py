#coding:utf8
#数据处理模块
import web, datetime

#连接数据库请用如下方式.
db = web.database(dbn='mysql', db='blog', host='localhost',user='root',pw='root')

#函数:各种提交，删除更新
def get_posts():
    return db.select('entries', order='id DESC')

def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text):
    db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
    db.delete('entries', where="id=$id", vars=locals())

def update_post(id, title, text):
    db.update('entries', where="id=$id", vars=locals(),
        title=title, content=text)