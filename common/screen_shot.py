# -*- coding: utf-8 -*-
#@Time      :2019/10/9    11:00
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :screen_shot.py
#@Software  :PyCharm
from selenium import webdriver
import random
import time,os
from common.path import project_path
from common import mylog
logger=mylog.MyLog('WJ')
def insert_img(driver):
    r=''
    for index in range(3):
        r +=str(random.randint(100,1000))
    img_path=os.path.join(project_path,'img','{}.png').format(time.strftime('%y-%m-%d %H-%M-%S_{}').format(r))
    driver.get_screenshot_as_file(img_path)
    logger.info('当前截图文件路径为{}'.format(img_path))

if __name__ =='__main__':
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver)
