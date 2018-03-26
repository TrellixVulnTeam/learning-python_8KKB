# -*- coding: utf-8 -*-

import logging
import sys

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("AppName")



# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.DEBUG)

# 输出不同级别的log
logger.debug('this is debug info')
logger.info('this is information')
logger.warn('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critical message')

# 2016-10-08 21:59:19,493 INFO    : this is information
# 2016-10-08 21:59:19,493 WARNING : this is warning message
# 2016-10-08 21:59:19,493 ERROR   : this is error message
# 2016-10-08 21:59:19,493 CRITICAL: this is fatal message, it is same as logger.critical
# 2016-10-08 21:59:19,493 CRITICAL: this is critical message

# 移除一些日志处理器
# logger.removeHandler(file_handler)
