import unittest
from case import TestCaseDemo
import HTMLTestRunnerCN

# ָ�����������Լ���

    
if __name__ == '__main__':

    # ��Ӳ��Լ���Case,������
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo('chqtest_Case1'))
    suiteTest.addTest(TestCaseDemo('chqtest_Case2'))
 
    # ֱ����������
 #   runner = unittest.TextTestRunner()
 #   runner.run(suiteTest)
    filePath ='F:\\Report.html'       #ȷ�����ɱ����·��
    fp = file(filePath,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'TestReport', 
        )
    # ���в�������
    result=runner.run(suiteTest)

    # ��ȡ���ʧ��������
    print result
    print result.failure_count
    print result.success_count
    print result.error_count

    runner1 = unittest.TextTestRunner()
    result1 =runner1.run(suiteTest)

    result2=result1.printErrors()

    print result2
