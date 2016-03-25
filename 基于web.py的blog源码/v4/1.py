#coding:utf8
aaa = u'77'
bbb = u'888'
# print type(aaa)

ccc = list(eval("(aaa,bbb)"))
print type(ccc)

# ccc0= ccc[0]
# ccc1 = ccc[1]
print "名字是：",ccc[0]
print "问候是:",ccc[1]
# print ccc0

print "name is:%s  is %s" %(ccc[0],ccc[1])

print "name is:",ccc[0],"fdfd",ccc[1]