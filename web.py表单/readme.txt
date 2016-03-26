http://webpy.org/form

web.py有提供表单的模块，必须按照他们的写，表单的填写在python中写。
当然你可以渲染到html 写表单然后post处理，但是取到的是input的值不是json对象。
模板页面下面的文件用jquery去渲染的话，又不支持 python真麻烦



json对象可以通过:
jquery 序列化表单