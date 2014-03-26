# coding=utf-8
from tastypie.serializers import Serializer

class TimeFormatSerializer(Serializer): 
    def format_datetime(self, data):
        return data.strftime("%Y-%m-%d %X %Z")