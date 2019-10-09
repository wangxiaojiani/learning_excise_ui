# -*- coding: utf-8 -*-
#@Time      :2019/10/9    15:37
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :login_sta.py
#@Software  :PyCharm
import unittest
from selenium.webdriver import Chrome,ChromeOptions
from ddt import ddt,data
from page.home_oage import HomePage
from page.login_page import LoginPage
from test_data import login_data
@ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '每个测试脚本执行前需要运行的前置操作'
        pass
    @classmethod
    def tearDownClass(cls):
        '每个测试脚本执行后需要运行的清理工作'
        pass

    def setUp(self):
        print('开始执行用例')
        self.base_url='http://120.78.128.25:8765'
        self.option=ChromeOptions()
        self.option.binary_location=r'C:\Users\1\AppData\Local\Programs\Python\Python37\Scripts\chromedrive.exe'
        self.driver=Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.po=LoginPage(self.driver)
        self.h_po=HomePage(self.driver)

    def tearDown(self):
        print('测试用例执行完毕')
        self.driver.close()

    @data(*login_data.login_info_error)
    def test_login_error(self,case):
        '登录失败用例'
        self.po.login(case['account'],case['pwd'])
        self.assertEqual(self.po.empty_hint(),case['expect_result'])

    # @data(*login_data.login_pwd_error)
    # def test_login_empty_error(self,case):
    #     '登录错误用例'
    #     self.po.login(case['account'],case['pwd'])
    #     self.assertEqual(self.po.pwd_error_hint(),case['expect_result'])
    #
    # @data(*login_data.login_success_info)
    # def test_loginsuccess(self,case):
    #         self.po.login(case['account'],case['pwd'])
    #         self.assertTrue(case['expect_result'] in self.h_po.select_username())

