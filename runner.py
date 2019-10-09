# -*- coding: utf-8 -*-
#@Time      :2019/10/9    16:17
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :runner.py
#@Software  :PyCharm

import unittest
from test_case import login_sta
from HTMLTestRunnerNew import HTMLTestRunner
import time
from common.path import current_report_path
#创建测试套件的对象
suit=unittest.TestSuite()
loader=unittest.TestLoader()
suit.addTest(loader.loadTestsFromModule(login_sta))
now =time.strftime('%Y-%m-%d %H-%M-%S')
file_path=current_report_path + '/'+now+ r'_test_report.html'

with open(file_path,'wb') as f:
    runner=HTMLTestRunner(stream=f,description='这是练习的测试用例',verbosity=2,title='输出测试报告',tester='wj')
    runner.run(suit)
