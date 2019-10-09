# -*- coding: utf-8 -*-
#@Time      :2019/10/9    10:45
#@Author    :xj
#@Email     :1027867874@qq.com
#@File      :path.py
#@Software  :PyCharm

import  os

#获取当前目录路径
current_dir_path=os.path.dirname(__file__)
#获取项目工程路径
project_path=os.path.split(current_dir_path)[0]
#日志输出目录
current_log_path=os.path.join(project_path,'result','log','test_log.text')

#报告输出跟目录
current_report_path=os.path.join(project_path,'result','report')
#输出当前文件名称
print(os.path.basename(__file__))




