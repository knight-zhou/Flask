#coding:utf8

from flask import Flask
from django.utils.decorators import method_decorator
app = Flask(__name__)

#路由
@app.route('/')
def hello():
    return 'ddd'

# @app.route('/user')
# def user():
#     return 'hello user'

#使用参数
#访问方式 curl http://127.0.0.1:5000/users/12345

# @app.route('/users/<id>')
# def user_id(id):
#     return 'hello user: '+id

#post参数
#http://127.0.0.1:5000/user 

@app.route('/user',methods = ['POST'])
def hello_user():
    return 'hello post user'




if __name__=='__main__':
    app.run()