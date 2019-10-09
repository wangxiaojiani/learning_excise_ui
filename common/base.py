# -*- coding: utf-8 -*-
#@Time      :2019/10/9    11:46
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :base.py
#@Software  :PyCharm
"""所有页面的基类"""
from selenium import webdriver
from selenium.webdriver import Chrome
from common.mylog import MyLog
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.screen_shot import insert_img
logger=MyLog('WJ')
class Page:
    def __init__(self,selenium_driver:Chrome):
        self.driver =selenium_driver
        selenium_driver.implicitly_wait(30)


    #等待元素存在
    def wait_eleExist(self,locator,by=By.XPATH,wait_times=40):
        if by not in By.__dict__.values():
            logger.error("定位类型[{0}]不在支持的类型中，请修改定位类型".format(by))
            raise InvalidSelectorException
        #开始事件
        t1=time.time()
        try:
            WebDriverWait(self.driver,wait_times).until(EC.presence_of_element_located((by,locator)))
            t2=time.time()
            logger.info('等待结束，等待开始时间:{}，等待结束时间:{}，等待时间长{}'.format(t1,t2,t2-t1))
        except TimeoutException as e:
            logger.error("等待元素超时，截取当前页面")
            insert_img(self.driver)
            raise e
        except InvalidSelectorException as e:
            logger.error('元素定位表达式[{}]不正确，请修证'.format(locator))
            raise e
        # 等待元素可见

    def wait_eleVisible(self, locator, by=By.XPATH, wait_times=40):
        if by not in By.__dict__.values ():
            logger.error ("定位类型[{0}]不在支持的类型中，请修改定位类型".format (by))
            raise InvalidSelectorException
        # 开始事件
        t1 = time.time ()
        try:
            WebDriverWait (self.driver, wait_times).until (EC.visibility_of_element_located((by, locator)))
            t2 = time.time ()
            logger.info ('等待结束，等待开始时间:{}，等待结束时间:{}，等待时间长{}'.format (t1, t2, t2 - t1))
        except TimeoutException as e:
            logger.error ("等待元素超时，截取当前页面")
            insert_img (self.driver)
            raise e
        except InvalidSelectorException as e:
            logger.error ('元素定位表达式[{}]不正确，请修证'.format (locator))
            raise e

        #等待元素可被点击
    def wait_eleClickable(self, locator, by=By.XPATH, wait_times=40):
        if by not in By.__dict__.values ():
            logger.error ("定位类型[{0}]不在支持的类型中，请修改定位类型".format (by))
            raise InvalidSelectorException
        # 开始事件
        t1 = time.time ()
        try:
            WebDriverWait (self.driver, wait_times).until (EC.element_to_be_clickable((by, locator)))
            t2 = time.time ()
            logger.info ('等待结束，等待开始时间:{}，等待结束时间:{}，等待时间长{}'.format (t1, t2, t2 - t1))
        except TimeoutException as e:
            logger.error ("等待元素超时，截取当前页面")
            insert_img (self.driver)
            raise e
        except InvalidSelectorException as e:
            logger.error ('元素定位表达式[{}]不正确，请修证'.format (locator))
            raise e

        #查找单个元素的封装
    def find_element(self,locator,by=By.XPATH,wait_times=40,type='visible'):
        """
        :param locator:元素定位表达式
        :param by: 元素的定位类型
        :param wait_times: 等待元素存在或者出现的时长 默认为40s
        :param type: 等待的条件，是可见还是元素存在及是否可被点击
        :return: 返回元素的webElement对象
        """
        logger.info('当前元素风味的类型为{}，当前查找元素的表达式为:{}'.format(by,locator))
        if type=='visible':
            logger.info('开始等待元素在页面可见')
            self.wait_eleVisible(locator,by,wait_times)
        elif type=='exist':
            logger.info('开始等待元素在当前页面存在')
            self.wait_eleExist(locator,by,wait_times)
        else:
            logger.info('开始等待元素可被点击')
            self.wait_eleClickable(locator,by,wait_times)
        try:
            ele=self.driver.find_element(by,locator)
            return ele
        except NoSuchElementException as e:
            logger.error('元素查找失败，找不到元素。开始截去当前页面图像')
            insert_img(self.driver)
            raise e

    #处理alert弹出窗口
    def alert_handler(self,action='accept'):
        #等待alert出现
        WebDriverWait(self.driver,10,0.5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        message=alert.text
        if action == 'accept':
            alert.accept()
        else:
            alert.dismiss()
        return message

    #执行js
    def execute_script(self,js):
        return self.driver.execute_script(js)








if __name__=='__main__':
    Page(Chrome()).wait_eleExist('//input',by='xxx')


