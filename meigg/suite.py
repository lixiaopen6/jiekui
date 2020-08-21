import unittest,os
from HTMLTestRunner_cn import HTMLTestRunner
import datetime
from meigg.UI.test_yongli.test_shouye import test_sss
suite=unittest.TestSuite()
i = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
report_name='小鹏的测试报告{0}'.format(i)
report_title='小鹏的测试报告{0}'.format(i)
report_desc='一灯老师要的，啥都有'
report_path='./report/'   #保存路径
report_file=report_path+'report3.html'  #保存文件名称
if not os.path.exists(report_path):    #判断是否存在该文件夹
    os.mkdir(report_path)
else:
    pass
with open(report_file, 'wb')as report:     #打开文件命名为report
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_sss))#测试文件
      #测试文件
    runner=HTMLTestRunner(stream=report,title=report_title,description=report_desc)
    runner.run(suite)
report.close()

