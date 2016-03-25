#coding:utf8
import json
import simplejson
import re
s = "greet=aaa&name=knight"
s1 = s.replace('&',',')
# print type(s1)
s2 = s1.replace('=',':')
# print type(s2)
print s2
s21 = json.dumps(s2)
print type(s21)



'''
s3 = {
    'name':'knight',
    'greet':'aaa'
}
s4 = "{'name':'knight','greet':'aaa'}"

print type(s4)
s5 = eval((s4))
# print type(s5)
print s5
print s5['name']
'''