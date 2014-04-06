# coding=utf-8
# import time
from tastypie.serializers import Serializer

class TimeFormatSerializer(Serializer): 
    def format_datetime(self, data):
        return data.strftime("%Y-%m-%d %X %Z")
        # return time.mktime(data.timetuple())
    
    def format_date(self, data):
        return data.strftime("%Y-%m-%d")