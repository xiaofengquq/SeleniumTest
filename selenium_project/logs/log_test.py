# 注意，如果不想用pytest运行，则py文件的文件名不能以test开头

# 定义一个详细的日志格式
# %(asctime)s - 按照ISO 8601格式的时间戳
# %(levelname)s - 日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
# %(filename)s - 日志消息发生的文件名
# %(lineno)d - 日志消息发生的文件中的行号
# %(module)s - 日志消息发生的模块名
# %(funcName)s - 日志消息发生的函数名
# %(message)s - 日志消息本身
my_format = '%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(module)s - %(funcName)s - %(message)s'

import logging

if __name__ == '__main__':
    # 设置日志配置
    logging.basicConfig(
        # 日志文件名称
        filename='my.log',
        # 设置日志级别，只能打印大于等于当前级别的日志
        level=logging.DEBUG,
        # 日志文件内容格式
        format=my_format
    )
    # 日志级别 从低到高
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')
    logging.critical('critical')
