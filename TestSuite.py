# -*- coding: utf-8 -*

import unittest
from makecase.case import TestCaseDemo
from common import emailto
import HTMLTestRunnerCN
import datetime
import time, os, sys,json,requests
import argparse,sys




TODAY = datetime.date.today()
CURRENTDAY = TODAY.strftime('%Y-%m-%d')
    
if __name__ == '__main__':

    
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo('chqtest_Case1'))
    suiteTest.addTest(TestCaseDemo('chqtest_Case2'))
 
    filePath ='./result/%s Report.html'%CURRENTDAY       
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'TestReport', 
        )
    
    result=runner.run(suiteTest)
    fp.close()


    # 发送邮件

    if result.failure_count>0:
        Status='- Failed'
    else:
        Status='- Passed'
        
    reuslt_file = open(filePath)
    result_data = reuslt_file.read()
    emailto.Send_Mail(result_data, filePath, Status)



    
    print result
    print result.failure_count
    print result.success_count
    print result.error_count

    runner1 = unittest.TextTestRunner()
    result1 =runner1.run(suiteTest)

    result2=result1.printErrors()

    print result2
