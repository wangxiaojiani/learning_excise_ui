# -*- coding: utf-8 -*-
#@Time      :2019/10/10    0:31
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :Conftest.py
#@Software  :PyCharm
import pytest
from page.login_page import LoginPage
from page.home_oage import HomePage
from selenium.webdriver import Firefox
@pytest.fixture(scope='class')
def init_driver():
    print('开始执行login类用例')
    driver=Firefox()
    driver.maximize_window()
    po=LoginPage(driver)
    h_po=HomePage(driver)
    yield driver,po,h_po
    driver.quit()
    print('loggin类结束用例结束')

