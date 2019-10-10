# -*- coding: utf-8 -*-
#@Time      :2019/10/9    15:37
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :login_sta.py
#@Software  :PyCharm
import unittest,pytest
from selenium.webdriver import Chrome
from ddt import ddt,data
from page.home_oage import HomePage
from page.login_page import LoginPage
from test_data import login_data

@pytest.mark.demo
@pytest.mark.usefixtures('init_driver')
class TestLogin:
    base_url='http://120.78.128.25:8765'

    # @classmethod
    # def setUpClass(cls):
    #     '每个测试脚本执行前需要运行的前置操作'
    #     pass
    # @classmethod
    # def tearDownClass(cls):
    #     '每个测试脚本执行后需要运行的清理工作'
    #     pass
    #
    # def setUp(self):
    #     print('开始执行用例')
    #
    #     self.base_url='http://120.78.128.25:8765'
    #     self.driver=Chrome(r'C:\Users\1\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    #     self.driver.maximize_window()
    #     self.driver.get(self.base_url)
    #     self.po=LoginPage(self.driver)
    #     self.h_po=HomePage(self.driver)
    #
    # def tearDown(self):
    #     print('测试用例执行完毕')
    #     self.driver.close()

    # @data(*login_data.login_info_error)
    @pytest.mark.sm
    @pytest.mark.parametrize('case',login_data.login_info_error)
    def test_login_error(self,case,init_driver):
        '登录失败用例'
        init_driver[0].get(self.base_url)

        init_driver[1].login(case['account'],case['pwd'])
        assert init_driver[1].empty_hint()==case['expect_result']

    # @data(*login_data.login_pwd_error)

    @pytest.mark.st
    @pytest.mark.parametrize('case',login_data.login_info_error)
    def test_login_empty_error(self,case,init_driver):
        '登录错误用例'
        init_driver[0].get(self.base_url)
        init_driver[1].login(case['account'],case['pwd'])
        assert init_driver[1].pwd_error_hint()==case['expect_result']

    @pytest.mark.sa
    @pytest.mark.parametrize('case',login_data.login_success_info)
    # @data(*login_data.login_success_info)
    def test_loginsuccess(self,case,init_driver):
        init_driver[0].get(self.base_url)
        init_driver[1].login(case['account'],case['pwd'])
        assert  case['expect_result'] in init_driver[2].select_username()
#
# if __name__=='__main__':
#     pytest.main(['-s','-m sm','--reruns=2','--reruns-delay=5',r'--html=result\report\test.html'])
