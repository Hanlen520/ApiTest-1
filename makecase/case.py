#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import common.api
import requests
import json

class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print 'Case Before'

  
    def tearDown(self):
        print 'Case After'

        
    def chqtest_Case1(self):
        apistring=common.api.getjson('./data/api.txt')
        url='http://capi.cxland.cn/user/getVideoHistory'
        t=common.api.getresponse(url,apistring)
        j = json.dumps(t).decode('unicode-escape')
        data = json.loads(j)
        # 初始化测试数据库的测试数据（这里加一个插入语句的方法）
        self.assertEqual(data["state"]["code"],200,'Result Fail')


    def chqtest_Case2(self):
        a = 2
        b = 3
        self.assertEqual(a*b,4,'Result Fail')
