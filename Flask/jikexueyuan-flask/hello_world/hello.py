#coding:utf8

from flask import Flask
app = Flask(__name__)

#б╥си
@app.route('/')
def hello():
    return 'hello wolrd'


if __name__=='__main__':
    app.run()