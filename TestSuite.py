import unittest
from case import TestCaseDemo
import HTMLTestRunnerCN

# 指定并启动测试集合

    
if __name__ == '__main__':

    # 添加测试集合Case,并启动
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo('chqtest_Case1'))
    suiteTest.addTest(TestCaseDemo('chqtest_Case2'))
 
    # 直接启动集合
 #   runner = unittest.TextTestRunner()
 #   runner.run(suiteTest)
    filePath ='F:\\Report.html'       #确定生成报告的路径
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'TestReport', 
        )
    # 运行测试用例
    result=runner.run(suiteTest)

    # 获取结果失败用例数
    print result
    print result.failure_count
    print result.success_count
    print result.error_count

    runner1 = unittest.TextTestRunner()
    result1 =runner1.run(suiteTest)

    result2=result1.printErrors()

    print result2
