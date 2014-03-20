# coding=utf-8
import datetime
import time
from django.utils.timezone import utc
now = datetime.datetime.now()
now2 = datetime.datetime.utcnow()
now3 = datetime.datetime.utcnow().replace(tzinfo=utc)
now4 = datetime.datetime.now().replace(tzinfo=utc)
# print now
# print now2
# print now3
# print now4
print time.localtime()  # 根据当前时区得到一个time.struct_time对象
print time.gmtime()  # 根据UTC时区得到一个time.struct_time对象
print time.mktime(time.gmtime())  # 将一个time.struct_time对象转换成时间戳格式
print time.asctime(time.gmtime())  # 将一个time.struct_time对象转换成字符串形式，根据当前时区。
print time.strftime('%Y-%m-%d %X %Z', time.gmtime())
print time.timezone

'''
show variables like '%time_zone%';
set time_zone = '+0:00';
'''