#coding:utf8
#数据处理模块
import web, datetime
import MySQLdb

#连接数据库请用如下方式.
db = web.database(dbn='mysql', db='blog', host='localhost',user='root',pw='root')

#函数:各种提交，删除更新，用于首页展示的,对于前台Index类
def get_posts():
    return db.select('student', order='id DESC')     #倒序查询

def new_select():
    return db.query('select * from student ORDER by id')                    ##函数用return返回值

    # for i in users:
    #     print users.id,users.hp

def get_posts1():
    return db.select('student', order='id DESC')


def test():
    aa = 5
    print "aa"


