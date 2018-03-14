#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import json                                
import requests


# 打开一个文件

def getjson(path):
    try:
        fo = open(path,'r')
        apistring=fo.read()
        return apistring
    except IOError:
        print "Error: no flie"

# post方法(python的格式要严格遵守否则会报错，比如try...except的缩进对齐)

def getresponse(url, datas=None):
    try:
        response = requests.post(url, data=datas)
        json=response.json()
        return json
    except:
        print "Error: 404"
    
        
if __name__ == "__main__":

     apistring=getjson('./api.txt')
     url='http://capi.cxland.cn/user/getVideoHistory'
     t=getresponse(url,apistring)
     j = json.dumps(t).decode('unicode-escape')
     print j

     print( '\n')

     data = json.loads(j)
     print "code = %s " % data["state"]["code"]
     print "name = %s " % data["data"]["list"][0]["name"]
