# coding=utf-8
from tastypie.serializers import Serializer
from django.utils import dateformat
from tastypie.utils.timezone import make_aware, make_naive, aware_datetime

class TimeFormatSerializer(Serializer): 
    def format_datetime(self, data):
        return data.strftime("%Y-%m-%d %X %Z")