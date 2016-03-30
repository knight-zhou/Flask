#coding:utf8
from flask import Flask, render_template
from models import User       

app = Flask(__name__)


@app.route('/')
def hello_world():
    content = "Hello world,knight"
    return render_template("index.html",content=content)

##这样用户名就传到了前段页面
@app.route('/user')
def user_index():
    user = User(1, 'knight-zhou')
    return  render_template("user_index.html", user=user)


#来一个更复杂的例子，如果前段页面用户id为1，那么久返回knight-zhou，不为1就返回不存在 
#http://127.0.0.1:5000/query_user/3
@app.route('/query_user/<user_id>')    
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1,'knight-zhou')
    return render_template("user_id.html",user=user)   




if __name__ == '__main__':
    app.run()
