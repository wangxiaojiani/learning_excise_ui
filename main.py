# -*- coding: utf-8 -*-
#@Time      :2019/10/10    1:06
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :main.py
#@Software  :PyCharm
import pytest
import pytest_rerunfailures

if __name__=='__main__':
    # pytest.main(['-s','-m sm','--reruns=2','--reruns-delay=5',r'--html=result\report\test.html'])
    pytest.main (['-s', '-q', '-m sm', '--reruns=2', '--reruns-delay=5', r'--alluredir=result/report/allure/'])
    # pytest.main(['-s','-m sm',r'--junitxml=result\report\test.xml']) #生成xml格式的测试报告
    # pytest.main(['-m login and not demo',r'--resultlog=result\log\testlog.log']) #生成log格式的测试报告