#coding:utf-8


import decimal
import datetime

#################################################
#数值转换函数
#################################################
def to_int(text):
    """将字符串转换为int类型，转换失败时默认值为0"""
    try:
        return int(text)
    except:
        return 0

def to_int0(text):
    """将字符串转换为int类型，当int值小于0时，返回0"""
    result = to_int(text)
    if not result or result < 0:
        return 0
    else:
        return result


def to_int1(text):
    """将字符串转换为int类型，当int值小于1时，返回1"""
    result = to_int(text)
    if not result or result < 1:
        return 1
    else:
        return result


def to_float(text):
    """将字符串转换为float类型，转换失败时，返回0.0"""
    try:
        return float(text)
    except:
        return 0.0


def to_float(text):
    """将字符串转换为int类型，当int值小于1时，返回1"""
    try:
        return float(text)
    except:
        return 0.0


def to_demical(text):
    try:
        return decimal.Decimal(text)
    except:
        return 0



#############################################
# 日期型转换函数
#############################################

def to_datatime(text):
    """字符串转时间"""
    if not text:
        return None

    # 定义字典根据时间字符串匹配不同的格式
    time_dict = {
        1: "%Y-%m-%d %H:%M:%S.%f",
        2: "%Y-%m-%d %H:%M",
        3: "%Y-%m-%d %H:%M:%S",
    }

    try:
        if str(text).find('.') > -1:
            return datetime.datetime.strptime(text,time_dict[1])
        elif ':' in text:
            time_list = text.split(':')
            return datetime.datetime.strptime(text,time_dict[len(time_list)])
        else:
            return datetime.datetime.strptime(text,"%Y-%m-%d")

    except:
        return None

def to_date(text):
    """字符串转日期"""
    d = to_datatime(text)
    if d:
        return d.date()


def to_timestamp10(text):
    """将时间格式的字符串转化为长度为10位长度的时间戳"""
    d = to_datatime(text)
    if d:
        return int(d.timestamp())
    else:
        return 0


def to_timestamp13(text):
    d = to_datatime(text)
    if d:
        return int(d.timestamp() * 1000)
    else:
        return 0
















