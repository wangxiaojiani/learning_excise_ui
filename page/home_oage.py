# -*- coding: utf-8 -*-
#@Time      :2019/10/9    15:23
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :home_oage.py
#@Software  :PyCharm
from common.base import Page
class HomePage(Page):
    # 登录按钮
    login_button = "//a[text()='登录']"
    username = "//img[@class='mr-5']/parent::a"

    def click_login_button(self):
        '点击首页登录按钮'
        self.find_element(self.login_button).click()

    def select_username(self):
        '返回用户姓名'
        return self.find_element (self.username).text
