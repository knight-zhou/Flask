# coding:utf8
# static目录下的内容直接可以加http://127.0.0.1:5000/static/1.html 进行访问不需要经过路由
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'





if __name__ == '__main__':
    app.run()
