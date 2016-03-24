#coding:utf8
#数据处理模块
import web, datetime
import MySQLdb

#连接数据库请用如下方式.
db = web.database(dbn='mysql', db='blog', host='localhost',user='root',pw='root')

#函数:各种提交，删除更新
def get_posts():
    return db.select('entries', order='id DESC')

def new_select():
    return db.query('select * from student ORDER by id')                    ##函数用return返回值

    # for i in users:
    #     print users.id,users.hp

def get_posts1():
    return db.select('student', order='id DESC')

def get_post(id):
    try:
        return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

#对应blog前台页面的post提交, 插入数据
def new_post(title, text):                       # 传入title和content的两个值,也就是前台页面定义的标签
    db.insert('entries', title=title, content=text, posted_on=datetime.datetime.utcnow())

# def new_post1():                                           #前台页面调用方法可以直接插入数据,没有传参数
#     db.insert('student', id='4', hp='ccc')





def test():
    aa = 5
    print "aa"


def del_post(id):
    db.delete('entries', where="id=$id", vars=locals())

def update_post(id, title, text):
    db.update('entries', where="id=$id", vars=locals(),
        title=title, content=text)