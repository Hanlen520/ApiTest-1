import unittest
from case import TestCaseDemo
import HTMLTestRunnerCN

# 指定并启动测试集合

if __name__ == '__main__':

    # 添加测试集合Case,并启动
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo('chqtest_Case1'))
    suiteTest.addTest(TestCaseDemo('chqtest_Case2'))
 
    # 直接启动集合,enenene
 #   runner = unittest.TextTestRunner()
 #   runner.run(suiteTest)
    filePath ='F:\\Report.html'       #确定生成报告的路径
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'TestReport', 
        )
    # 运行测试用例
    runner.run(suiteTest)
