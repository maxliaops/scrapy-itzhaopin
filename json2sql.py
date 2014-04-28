#-*- coding: UTF-8 -*-
import json

data = []
with open('itzhaopin/tencent.json') as f:
    for line in f:
        data.append(json.loads(line))

#print json.dumps(data, ensure_ascii=False)

str = "\r\n"
for item in data:
    #print json.dumps(item)
    str = str + "insert into tencent(name,catalog,workLocation,recruitNumber,detailLink,publishTime) values "
    str = str + "('%s','%s','%s','%s','%s','%s');\r\n" % (item['name'],item['catalog'],item['workLocation'],item['recruitNumber'],item['detailLink'],item['publishTime'])

import codecs
file_object = codecs.open('tencent.sql', 'w' ,"utf-8")
file_object.write(str)
file_object.close()
print "success"

