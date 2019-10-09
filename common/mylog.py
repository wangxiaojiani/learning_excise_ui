# -*- coding: utf-8 -*-
#@Time      :2019/10/9    10:12
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :mylog.py
#@Software  :PyCharm
import logging
from common.path import current_log_path

class MyLog:
    def __init__(self,name):
        self.name=name
    def mylog(self,levelname,msg):
        #设置日志收集器的名字
        logger=logging.getLogger(self.name)
        #设置日志收集器的级别
        logger.setLevel('DEBUG')


        '如果日志收集器不存在渠道则要建立渠道'
        #首先设置日志收集器的格式
        formatter=logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息]:%(message)s-【%(pathname)s】-%(filename)s-%(module)s-%(funcName)s-%(lineno)d')
        #建立控制台渠道
        ch=logging.StreamHandler()
        ch.setFormatter(formatter)
        ch.setLevel('DEBUG')
        #建立文件渠道
        fh=logging.FileHandler(filename=current_log_path,encoding='utf-8')
        fh.setFormatter(formatter)
        fh.setLevel('DEBUG')

        #将日志收集器与渠道对接
        logger.addHandler(fh)
        logger.addHandler(ch)

        if levelname =='DEBUG':
            logger.debug(msg)
        elif levelname=='INFO':
            logger.info(msg)
        elif levelname=='WARNING':
            logger.warning(msg)
        elif levelname=='ERROR':
            logger.error(msg)
        elif levelname=='CRITICAL':
            logger.critical(msg)
        else:
            print('你输入的级别有误')
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self,msg):
        self.mylog('DEBUG',msg)

    def info(self,msg):
        self.mylog('INFO',msg)

    def warning(self,msg):
        self.mylog('WARNING',msg)

    def error(self,msg):
        self.mylog('ERROR',msg)

    def critical(self,msg):
        self.mylog('CRITICAL',msg)
if __name__ =='__main__':
    logger = MyLog ('WJ')

    logger.debug ('dad')
    logger.error ('222')