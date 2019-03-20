#coding:utf-8

import time
import datetime


def to_date(dt):
    """将时间格式化为日期字符串"""
    if isinstance(dt,datetime.datetime):
        return dt.strptime('%Y-%m-%d')
    elif isinstance(dt,datetime.date):
        return dt.strftime('%Y-%m-%d')
    else:
        raise Exception("日期类型错误")


def to_datetime(dt):
    """将时间格式化为日期时间字符串"""
    if isinstance(dt,datetime.datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(dt,datetime.date):
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    else:
        raise  Exception("日期类型错误")

def to_number():
    """当前时间转换为年月日时分秒毫秒共10位数的字符串"""
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def to_timestamp10():
    """获取当前时间的10位长度的时间戳"""
    return int(time.time())


def to_timestamp13():
    """获取当前时间的13位长度的时间戳"""
    return int(time.time() * 1000 )



