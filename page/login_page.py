# -*- coding: utf-8 -*-
#@Time      :2019/10/9    15:06
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :login_page.py
#@Software  :PyCharm
"登录页面交互细节的封装（元素以及行为）"
from common.base import Page
from page.home_oage import HomePage

class LoginPage(Page):
    def __init__(self,selenium_driver):
        super(LoginPage, self).__init__(selenium_driver)
        self.p_home=HomePage(self.driver)


    """定位器 定位封装相当于属性"""
    #帐号输入框
    account="//input[@name='phone']"
    #密码输入框
    pwd="//input[@name='password']"
    #登录按钮
    login_button="//button[@class='btn btn-special']"
    #手机号提示信息定位(手机号为空，或者格式不正确时),或者密码为空时提示信息定位
    empty_pm="//div[@class='form-error-info']"
    #密码不正确师提示信息定位
    pwd_error_pm="//div[@class='layui-layer-content']"

    """行为封装"""
    def type_account(self,username):
        '输入账号'
        self.find_element(self.account).send_keys(username)
    def type_pwd(self,password):
        '输入密码'
        self.find_element(self.pwd).send_keys(password)

    def click_login_button(self):
        '点击登录按钮'
        self.find_element(self.login_button).click()

    def empty_hint(self):
        '手机号为空或者格式不正确或者密码为空时，提示信息文本输出'
        return self.find_element (self.empty_pm).text

    def pwd_error_hint(self):
        '密码错误时，登录后提示信息提取'
        return self.find_element (self.pwd_error_pm).text

    #设置统一的登录入口
    def login(self,username,password):
        #点击首页登录按钮
        self.p_home.click_login_button()
        #判断页面是否跳转成功
        self.wait_eleVisible(self.account)
        #输入用户名及密码
        self.type_account(username)
        self.type_pwd(password)
        #点击登录
        self.click_login_button()









