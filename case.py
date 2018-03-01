import unittest
import api
import requests
import json

class TestCaseDemo(unittest.TestCase):

    def setUp(self):
        print 'Case Before'

  
    def tearDown(self):
        print 'Case After'

        
    def chqtest_Case1(self):
        apistring=api.getjson('./api.txt')
        url='http://capi.cxland.cn/user/getVideoHistory'
        t=api.getresponse(url,apistring)
        j = json.dumps(t).decode('unicode-escape')
        data = json.loads(j)
        self.assertEqual(data["state"]["code"],200,'Result Fail')


    def chqtest_Case2(self):
        a = 2
        b = 3
        self.assertEqual(a*b,6,'Result Fail')
